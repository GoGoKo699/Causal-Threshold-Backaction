#!/usr/bin/env python3
"""Check local navigation, the fixed milestone map, and source hygiene.

This is a structural check. Rendered GitHub mathematics must also be inspected.
"""

from __future__ import annotations

import re
from pathlib import Path
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", "build", ".venv", "__pycache__"}


def main() -> None:
    errors = []
    links = 0
    documents = [p for p in ROOT.rglob("*.md") if not any(x in IGNORED for x in p.parts)]
    for path in documents:
        text = path.read_text()
        # Link checks include image sources; code examples contain no Markdown links.
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0])
            if relative:
                links += 1
                if not (path.parent / relative).exists():
                    errors.append(f"{path.relative_to(ROOT)}: missing target {relative}")
        for forbidden in [r"\newcommand", r"\renewcommand", r"\operatorname", "sandbox:", "/workspace/scratch/"]:
            if forbidden in text:
                errors.append(f"{path.relative_to(ROOT)}: nonportable content {forbidden}")
        fences = re.findall(r"^```", text, flags=re.MULTILINE)
        if len(fences) % 2:
            errors.append(f"{path.relative_to(ROOT)}: unmatched fenced block")
        math_blocks = re.findall(r"^[ \t]*```math[ \t]*\n(.*?)^[ \t]*```[ \t]*$", text,
                                 flags=re.MULTILINE | re.DOTALL)
        if any("<" in block for block in math_blocks):
            errors.append(f"{path.relative_to(ROOT)}: use \\lt instead of literal < in fenced math")
        for line in text.splitlines():
            if line.lstrip().startswith("|"):
                formulas = re.findall(r"\$`(.*?)`\$", line)
                if any("|" in formula for formula in formulas):
                    errors.append(f"{path.relative_to(ROOT)}: use named vertical delimiters in table math")
    milestones = ROOT / "docs" / "MILESTONES.md"
    if milestones.exists():
        found = re.findall(r"^### (M\d{2})\b", milestones.read_text(), flags=re.MULTILINE)
        expected = [f"M{i:02d}" for i in range(1, 31)]
        if found != expected:
            errors.append("MILESTONES.md must define exactly M01 through M30 in order")
    else:
        errors.append("MILESTONES.md is missing")
    for entrypoint in ["README.md", "llms.txt", "AGENTS.md", "docs/LEARNING.md"]:
        path = ROOT / entrypoint
        if not path.exists() or "MILESTONES.md" not in path.read_text():
            errors.append(f"{entrypoint}: milestone route is missing")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Checked {len(documents)} Markdown documents, {links} local links, and exactly 30 milestones.")


if __name__ == "__main__":
    main()
