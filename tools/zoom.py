"""Build the catalog zoom views from a derived whole-problem SVG."""

from xml.etree import ElementTree as ET


SVG = "{http://www.w3.org/2000/svg}"


def zoom_sheet(cell, details, heading_id, sheet_path):
    source = ET.parse(sheet_path).getroot()
    container = ET.SubElement(cell, "div", {"class": "derived-sheet"})
    ET.SubElement(container, "img", src=sheet_path.as_posix(), loading="lazy",
                  width=source.attrib["width"], height=source.attrib["height"])
    overlay = ET.SubElement(container, "svg", {
        "class": "sheet-map", "viewBox": source.attrib["viewBox"],
    })
    for link in source.findall(SVG + "a"):
        individual = sheet_path.parent / link.attrib["href"]
        stem = individual.stem
        if not individual.is_file():
            raise FileNotFoundError(individual)
        hotspot = ET.SubElement(overlay, "a", href="#" + stem)
        hit = link.find(f"{SVG}rect[@pointer-events='all']")
        ET.SubElement(hotspot, "rect", hit.attrib)

        view = ET.SubElement(details, "section", id=stem, attrib={"class": "individual"})
        ET.SubElement(view, "h3").text = stem
        ET.SubElement(view, "img", src=individual.as_posix(), loading="lazy",
                      width="320", height="320")
        actions = ET.SubElement(view, "p")
        download = ET.SubElement(actions, "a", href=individual.as_posix(),
                                 download=individual.name)
        download.text = "Download " + individual.name
        download.tail = " · "
        ET.SubElement(actions, "a", href="#" + heading_id).text = "Back to " + heading_id.upper()
