#!/usr/bin/env python3
"""Check local navigation, milestone structure, and document source hygiene.

This is a structural check. Rendered GitHub mathematics must also be inspected.
"""

from __future__ import annotations

import html
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", "build", ".venv", "__pycache__"}


def outside_fences(text: str) -> tuple[str, list[str], bool]:
    """Keep source line numbers while excluding code from links and headings."""
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group().count("\n"),
                  text, flags=re.DOTALL)
    visible, math_blocks, block = [], [], []
    marker, width, language = "", 0, ""
    for line in text.splitlines():
        fence = re.match(r"^[ \t]*(`{3,}|~{3,})(.*)$", line)
        if marker:
            if (fence and fence[1][0] == marker and len(fence[1]) >= width
                    and not fence[2].strip()):
                if language == "math":
                    math_blocks.append("\n".join(block))
                marker, block = "", []
            else:
                block.append(line)
            visible.append("")
        elif fence:
            marker, width = fence[1][0], len(fence[1])
            language = fence[2].strip()
            visible.append("")
        else:
            visible.append(line)
    return "\n".join(visible), math_blocks, bool(marker)


def headings(text: str) -> list[tuple[int, str, int]]:
    """Read native ATX headings and the single-line Setext form used in prose."""
    result = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        atx = re.match(r"^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*)$", line)
        if atx:
            title = re.sub(r"[ \t]+#+[ \t]*$", "", atx[2] or "").strip()
            result.append((len(atx[1]), title, i + 1))
        elif (i and re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", line)
              and lines[i - 1].strip()
              and not re.match(r"^\s*(?:[#>|`~]|[-+*]\s|\d+[.)]\s)", lines[i - 1])):
            result.append((1 if line.lstrip().startswith("=") else 2,
                           lines[i - 1].strip(), i))
    return result


def heading_slug(title: str) -> str:
    """Apply GitHub section-link rules to native heading text.

    See GitHub Docs, "Basic writing and formatting syntax", "Section links".
    Keep Unicode letters, numbers and marks; remove punctuation and symbols
    except literal hyphens/underscores. Spaces become hyphens individually.
    """
    title = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", title)
    title = re.sub(r"<[^>]*>", "", title)
    # Code and escaped punctuation are literal, including their underscores.
    literals = []

    def keep_literal(match: re.Match[str]) -> str:
        literals.append(match[2] if match.lastindex == 2 else match[1])
        return f"\x00{len(literals) - 1}\x00"

    title = re.sub(r"(`+)(.*?)\1", keep_literal, title)
    title = re.sub(r"\\([^\w\s])", keep_literal, title)
    title = re.sub(r"(?<!\w)_{1,3}(.+?)_{1,3}(?!\w)", r"\1", title)
    for i, literal in enumerate(literals):
        title = title.replace(f"\x00{i}\x00", literal)
    title = html.unescape(title).strip().lower()
    return "".join(
        "-" if char == " " else char
        for char in title
        if char in " -_" or unicodedata.category(char)[0] in "LNM"
    )


def document_anchors(text: str) -> set[str]:
    used = set()
    for _, title, _ in headings(text):
        base = heading_slug(title)
        slug, suffix = base, 0
        while slug in used:
            suffix += 1
            slug = f"{base}-{suffix}"
        used.add(slug)
    # Explicit HTML anchors are also supported by GitHub.
    used.update(html.unescape(m[2]) for m in re.finditer(
        r"<a\b[^>]*\b(?:name|id)\s*=\s*([\"'])(.*?)\1",
        text, flags=re.IGNORECASE))
    return used


def local_link_targets(text: str) -> list[tuple[int, str]]:
    """Extract inline/image and reference-definition destinations outside code."""
    prose = re.sub(r"(`+)(.*?)\1", lambda m: " " * len(m.group()), text)
    targets = []
    for match in re.finditer(r"\]\([ \t]*", prose):
        start = end = match.end()
        if end < len(prose) and prose[end] == "<":
            end = prose.find(">", end + 1)
            if end == -1:
                continue
            target = prose[start + 1:end]
        else:
            depth = 0
            while end < len(prose):
                char = prose[end]
                if char == "\\" and end + 1 < len(prose):
                    end += 2
                    continue
                if char == "(":
                    depth += 1
                elif char == ")":
                    if not depth:
                        break
                    depth -= 1
                elif char.isspace() and not depth:
                    break
                end += 1
            target = prose[start:end]
        targets.append((prose.count("\n", 0, match.start()) + 1, target))
    for match in re.finditer(
            r"^ {0,3}\[(?!\^)[^\]]+\]:[ \t]*(?:<([^>\n]+)>|(\S+))",
            prose, flags=re.MULTILINE):
        targets.append((prose.count("\n", 0, match.start()) + 1,
                        match[1] or match[2]))
    return targets


def hygiene_errors(path: Path, text: str, visible: str,
                   math_blocks: list[str], unclosed: bool) -> list[str]:
    errors = []
    label = path.relative_to(ROOT)
    for forbidden in [r"\newcommand", r"\renewcommand", r"\operatorname",
                      "sandbox:", "/workspace/scratch/"]:
        if forbidden in text:
            errors.append(f"{label}: nonportable content {forbidden}")
    if unclosed:
        errors.append(f"{label}: unmatched fenced block")
    if any("<" in block for block in math_blocks):
        errors.append(f"{label}: use \\lt instead of literal < in fenced math")
    for number, line in enumerate(visible.splitlines(), 1):
        if line.lstrip().startswith("|"):
            formulas = re.findall(r"\$`(.*?)`\$", line)
            if any("|" in formula for formula in formulas):
                errors.append(f"{label}:{number}: use named vertical delimiters in table math")
    if path.name.casefold() == "coaching.md" or re.search(r"\bCOACHING\.md\b", text, re.I):
        errors.append(f"{label}: personal coaching-contract path must not enter project documents")
    plain = re.sub(r"[*_`]", "", text)
    rounds = r"\d+(?:\s*[-–—]\s*\d+)?[\s-]*(?:learning\s+)?rounds?\b"
    if (re.search(r"\bIntensity\s*[.:]\s*" + rounds, plain, re.I)
            or re.search(r"\bteaching\s+intensity\b.{0,160}?" + rounds,
                         plain, re.I | re.S)):
        errors.append(f"{label}: personal teaching-intensity round prescription")
    if re.search(r"\bRevise\s*(?:→|⇒|->)\s*Learn\s*(?:→|⇒|->)\s*Test\b", plain, re.I):
        errors.append(f"{label}: personal Revise/Learn/Test contract")
    return errors


def main() -> None:
    errors = []
    links = fragments = 0
    documents = sorted(p for p in ROOT.rglob("*.md")
                       if not any(x in IGNORED for x in p.relative_to(ROOT).parts))
    guide = ROOT / "llms.txt"
    sources = documents + ([guide] if guide.exists() else [])
    contents, visible_sources, anchors = {}, {}, {}
    for path in sources:
        text = path.read_text(encoding="utf-8")
        visible, math_blocks, unclosed = outside_fences(text)
        contents[path] = text
        visible_sources[path] = visible
        anchors[path] = document_anchors(visible)
        errors.extend(hygiene_errors(path, text, visible, math_blocks, unclosed))

    for path, visible in visible_sources.items():
        for number, destination in local_link_targets(visible):
            destination = html.unescape(re.sub(r"\\([^\w\s])", r"\1", destination))
            label = f"{path.relative_to(ROOT)}:{number}"
            try:
                target = urlsplit(destination)
            except ValueError as error:
                errors.append(f"{label}: malformed link {destination}: {error}")
                continue
            if target.scheme or target.netloc:
                continue
            links += 1
            relative = unquote(target.path)
            resolved = ((ROOT / relative.lstrip("/")) if relative.startswith("/")
                        else (path.parent / relative) if relative else path).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"{label}: local target escapes the repository: {destination}")
                continue
            if not resolved.exists():
                errors.append(f"{label}: missing target {relative or destination}")
                continue
            fragment = unquote(target.fragment)
            if fragment:
                if resolved.is_dir():
                    resolved = resolved / "README.md"
                if resolved.suffix.lower() == ".md" or resolved.name == "llms.txt":
                    fragments += 1
                    if resolved not in anchors:
                        if not resolved.exists():
                            errors.append(f"{label}: fragment target has no README.md: {destination}")
                            continue
                        anchors[resolved] = document_anchors(
                            outside_fences(resolved.read_text(encoding="utf-8"))[0])
                    if fragment not in anchors[resolved]:
                        errors.append(f"{label}: missing fragment #{fragment} in "
                                      f"{resolved.relative_to(ROOT)}")

    milestones = ROOT / "learning" / "MILESTONES.md"
    if milestones in visible_sources:
        parsed = headings(visible_sources[milestones])
        found, phases, phase_order, phase = [], {"I": [], "II": []}, [], None
        for level, title, _ in parsed:
            if level == 2:
                match = re.match(r"Phase\s+(II|I)\b", title, re.I)
                phase = match[1].upper() if match else None
                if phase:
                    phase_order.append(phase)
            milestone = re.match(r"(M\d{2})\b", title) if level == 3 else None
            if milestone:
                found.append(milestone[1])
                if phase:
                    phases[phase].append(milestone[1])
        expected = [f"M{i:02d}" for i in range(1, 31)]
        if found != expected:
            errors.append("learning/MILESTONES.md must define exactly M01 through M30 in order")
        if (phase_order != ["I", "II"] or phases["I"] != expected[:14]
                or phases["II"] != expected[14:]):
            errors.append("learning/MILESTONES.md must place M01–M14 in Phase I "
                          "and M15–M30 in Phase II (14/16)")
    else:
        errors.append("learning/MILESTONES.md is missing")
    for entrypoint in ["README.md", "llms.txt", "AGENTS.md", "learning/WATROUS_BRIDGE.md"]:
        path = ROOT / entrypoint
        route = "MILESTONES.md" if path.parent.name == "learning" else "learning/MILESTONES.md"
        if path not in contents or route not in contents[path]:
            errors.append(f"{entrypoint}: milestone route is missing")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Checked {len(documents)} Markdown documents and llms.txt, {links} local links "
          f"({fragments} fragments), and exactly 30 milestones in phases of 14 and 16.")


if __name__ == "__main__":
    main()
