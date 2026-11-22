"""Render problems.json as a static, filterable HTML catalog."""

from collections import Counter
from pathlib import Path
import json
from xml.etree import ElementTree as ET

from zoom import zoom_sheet


TITLE = "Bongard Problems"
LEVELS = {1: "Very Easy", 2: "Easy", 3: "Moderate", 4: "Hard", 5: "Very Hard"}


def filter_menu(counts):
    nav = ET.Element("nav", {"class": "filters"})
    menu = ET.SubElement(nav, "ul")
    options = [("All", None), ("Unflagged", None), ("Flagged", None),
               *((name, level) for level, name in LEVELS.items()), ("Unrated", None)]
    for label, level in options:
        view = label.lower().replace(" ", "-")
        item = ET.SubElement(menu, "li")
        link = ET.SubElement(item, "a", {"data-show": view})
        if label == "All":
            link.set("class", "active")
            link.set("href", "problems.html")
        else:
            link.set("href", "?show=" + view)
        link.text = f"{label} ({counts[label]})"
        if level is not None:
            link.set("data-difficulty", str(level))
    return nav


def source_row(table, source, label, foundalis=False):
    row = ET.SubElement(table, "tr")
    image_cell = ET.SubElement(row, "td")
    rule_cell = ET.SubElement(row, "td")
    if source is None:
        return
    if path := source.get("image"):
        link = ET.SubElement(image_cell, "a", href=path)
        ET.SubElement(link, "img", src=path, loading="lazy", decoding="async")
    rule = source["rule"]
    if foundalis:
        quote = f'“{rule["left"]}” / “{rule["right"]}”'
    else:
        quote = f'“{rule}”'
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
    for width in ("67%", "33%"):
        ET.SubElement(columns, "col", style=f"width: {width}")
    rows = ET.SubElement(table, "tbody")
    source_row(rows, problem.get("foundalis"), key + "F", foundalis=True)
    source_row(rows, problem.get("oebp"), key + "E")

    row = ET.SubElement(rows, "tr")
    image_cell = ET.SubElement(row, "td")
    derived = problem["derived"]
    if path := derived.get("image"):
        details = ET.SubElement(record, "div", {"class": "details"})
        zoom_sheet(image_cell, details, key, Path(path))
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
