"""Render problems.json as a static, filterable HTML catalog."""

from collections import Counter
from pathlib import Path
import json
import struct
from xml.etree import ElementTree as ET

TITLE = "Bongard Problems"
LEVELS = {1: "Very Easy", 2: "Easy", 3: "Moderate", 4: "Hard", 5: "Very Hard"}


def filter_menu(counts):
    nav = ET.Element("nav", {"class": "filters"})
    menu = ET.SubElement(nav, "ul")
    options = [("All", None), ("Flagged", None), ("Unflagged", None),
               *((name, level) for level, name in LEVELS.items()), ("Unrated", None)]
    for label, level in options:
        view = label.lower().replace(" ", "-")
        item = ET.SubElement(menu, "li")
        link = ET.SubElement(item, "a", {"data-show": view, "href": "?show=" + view})
        if label == "All":
            link.set("class", "active")
        link.text = f"{label} ({counts[label]})"
        if level is not None:
            link.set("data-difficulty", str(level))
    return nav


def image_link(cell, path):
    link = ET.SubElement(cell, "a", href=path)
    image = ET.SubElement(link, "img", src=path, loading="lazy", decoding="async")
    # Reserve space for the disclosure animation while the image loads.
    if Path(path).suffix.lower() == ".png":
        with Path(path).open("rb") as file:
            file.seek(16)  # Width and height in the PNG header.
            width, height = struct.unpack(">II", file.read(8))
        image.set("width", str(width))
        image.set("height", str(height))


def source_row(table, source, label, name):
    if source is None:
        return
    row = ET.SubElement(table, "tr")
    cell = ET.SubElement(row, "td", {"class": "source-row", "colspan": "2"})
    details = ET.SubElement(cell, "details", {"open": ""} if name == "OEBP" else {})
    summary = ET.SubElement(details, "summary")
    arrow = ET.SubElement(summary, "span", {"class": "triangle"})
    arrow.text = "▼"
    arrow.tail = " " + name
    reveal = ET.SubElement(details, "div", {"class": "source-reveal"})
    columns = ET.SubElement(reveal, "div", {"class": "source-columns"})
    image_cell = ET.SubElement(columns, "div")
    rule_cell = ET.SubElement(columns, "div")
    rule = source["rule"]
    quote = f'“{rule["left"]}” / “{rule["right"]}”' if name == "Foundalis" else f'“{rule}”'
    if path := source.get("image"):
        image_link(image_cell, path)
    ET.SubElement(rule_cell, "p").text = quote
    if extra := source.get("extra"):
        label += f' ({extra["left"]}+{extra["right"]} more)'
    link = ET.SubElement(ET.SubElement(rule_cell, "p"), "a", href=source["url"])
    link.text = label


def problem_section(key, problem, difficulty):
    reason = problem.get("flag_reason")
    section = ET.Element("section", {"class": "problem", "data-flagged": str(bool(reason)).lower()})
    ET.SubElement(section, "hr")
    heading = ET.SubElement(section, "h2", id=key)
    link = ET.SubElement(heading, "a", href=f"#{key}")
    link.text = key
    labels = []
    if reason:
        labels.append("Flagged")
    if difficulty is not None:
        labels.append(LEVELS[difficulty])
        section.set("data-difficulty", str(difficulty))
    if labels:
        link.tail = " · " + " · ".join(labels)

    record = ET.SubElement(section, "div", {"class": "record"})
    table = ET.SubElement(record, "table")
    columns = ET.SubElement(table, "colgroup")
    ET.SubElement(columns, "col")
    ET.SubElement(columns, "col")
    rows = ET.SubElement(table, "tbody")
    source_row(rows, problem.get("foundalis"), key + "F", "Foundalis")
    source_row(rows, problem.get("oebp"), key + "E", "OEBP")

    row = ET.SubElement(rows, "tr")
    image_cell = ET.SubElement(row, "td")
    derived = problem["derived"]
    if path := derived.get("image"):
        image_link(image_cell, path)
    if reason:
        ET.SubElement(image_cell, "p").text = reason
    ET.SubElement(row, "td").text = derived["rule"]
    return section


def html(element):
    ET.indent(element)
    return ET.tostring(element, encoding="unicode", method="html")


def main():
    problems = json.loads(Path("problems.json").read_text(encoding="utf-8"))
    counts = Counter(All=len(problems))
    sections = []
    for key in sorted(problems, key=lambda k: int(k[2:])):
        problem = problems[key]
        difficulty = problem.get("foundalis", {}).get("difficulty")
        counts["Flagged" if problem.get("flag_reason") else "Unflagged"] += 1
        counts[LEVELS[difficulty] if difficulty is not None else "Unrated"] += 1
        sections.append(html(problem_section(key, problem, difficulty)))

    script = Path("tools/catalog.js").read_text(encoding="utf-8").rstrip()
    body = "\n".join([f'<h1 id="bongard-problems">{TITLE}</h1>', html(filter_menu(counts)),
                      *sections, "<script>", script, "</script>"])
    template = Path("tools/page.tpl").read_text(encoding="utf-8")
    print(template.replace("$title$", TITLE).replace("$body$", body), end="")


if __name__ == "__main__":
    main()
