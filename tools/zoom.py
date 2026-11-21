"""Add a zoom view for every linked example in a Pandoc catalog page."""

from pathlib import Path
import sys
from xml.etree import ElementTree as ET


SVG = "{http://www.w3.org/2000/svg}"


def zoom_sheet(cell, details, heading_id):
    original = cell.find("object")
    sheet_path = Path(original.attrib["data"])
    source = ET.parse(sheet_path).getroot()
    cell.remove(original)
    container = ET.SubElement(cell, "div", {"class": "derived-sheet"})
    ET.SubElement(container, "img", src=sheet_path.as_posix(), loading="lazy",
                  width=source.attrib["width"], height=source.attrib["height"],
                  alt=source.findtext(SVG + "title"))
    overlay = ET.SubElement(container, "svg", {
        "class": "sheet-map", "viewBox": source.attrib["viewBox"],
        "role": "group", "aria-label": source.attrib["aria-label"],
    })
    for link in source.findall(SVG + "a"):
        individual = sheet_path.parent / link.attrib["href"]
        stem = individual.stem
        if not individual.is_file():
            raise FileNotFoundError(individual)
        label = link.findtext(SVG + "title")
        hotspot = ET.SubElement(overlay, "a", href="#" + stem,
                                attrib={"aria-label": "Zoom " + label})
        ET.SubElement(hotspot, "title").text = label
        hit = link.find(f"{SVG}rect[@pointer-events='all']")
        ET.SubElement(hotspot, "rect", hit.attrib)

        view = ET.SubElement(details, "section", id=stem, tabindex="-1",
                             attrib={"class": "individual", "aria-label": label})
        ET.SubElement(view, "h3").text = stem
        ET.SubElement(view, "img", src=individual.as_posix(), loading="lazy",
                      width="320", height="320", alt=label)
        actions = ET.SubElement(view, "p")
        download = ET.SubElement(actions, "a", href=individual.as_posix(),
                                 download=individual.name)
        download.text = "Download " + individual.name
        download.tail = " · "
        ET.SubElement(actions, "a", href="#" + heading_id).text = "Back to " + heading_id.upper()


def add_zoom(page):
    head, opening, rest = page.partition("<main>")
    body, closing, foot = rest.partition("</main>")
    if not opening or not closing:
        raise ValueError("Missing main element in catalog template")
    main = ET.fromstring(opening + body + closing)
    headings = main.findall("h2")
    if headings:
        start, end = headings[0].text, headings[-1].text
        head = head.replace("</title>", f" · {start}–{end}</title>", 1)
    for image in main.iter("img"):
        image.set("loading", "lazy")
        image.set("decoding", "async")
    for index, child in reversed(list(enumerate(main))):
        if child.tag != "table":
            continue
        cell = child.find(".//td[object]")
        if cell is None:
            continue
        heading = main[index - 1]
        if index == 0 or heading.tag != "h2":
            raise ValueError("Missing problem heading before derived sheet")
        details = ET.Element("div", {"class": "details"})
        zoom_sheet(cell, details, heading.attrib["id"])
        main.insert(index + 1, details)
        details.tail = "\n"
    return head + ET.tostring(main, method="html", encoding="unicode") + foot


if __name__ == "__main__":
    page = Path(sys.argv[1])
    page.write_text(add_zoom(page.read_text(encoding="utf-8")), encoding="utf-8")
