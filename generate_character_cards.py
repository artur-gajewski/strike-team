#!/usr/bin/env python3
"""
Generate character_cards.html from character_cards.json using a Jinja2 template.
Output is written to FINAL/character_cards.html.
"""

import json
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

SCRIPT_DIR = Path(__file__).parent
JSON_FILE = SCRIPT_DIR / "character_cards.json"
TEMPLATE_DIR = SCRIPT_DIR / "templates"
TEMPLATE_NAME = "character_cards_template.html"
OUTPUT_DIR = SCRIPT_DIR / "FINAL"
OUTPUT_FILE = OUTPUT_DIR / "character_cards.html"


def md_bold(text: str) -> str:
    """Convert **text** to <strong>text</strong>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", str(text))


def newline_br(text: str) -> str:
    """Convert newline characters to HTML <br> tags."""
    return str(text).replace("\n", "<br>")


def main() -> None:
    if not JSON_FILE.exists():
        print(f"Error: {JSON_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    with JSON_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,
        keep_trailing_newline=True,
    )
    env.filters["md"] = md_bold
    env.filters["newline_br"] = newline_br

    template = env.get_template(TEMPLATE_NAME)
    html = template.render(**data)

    OUTPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"Generated: {OUTPUT_FILE}")

    pdf_file = OUTPUT_FILE.with_suffix(".pdf")
    HTML(string=html, base_url=str(SCRIPT_DIR)).write_pdf(pdf_file)
    print(f"Generated: {pdf_file}")


if __name__ == "__main__":
    main()
