#!/usr/bin/env python3
"""Check local Markdown links/anchors and course structure; no network or writes."""
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "student-workspace", "node_modules", "__pycache__"}
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")


def prose(text):
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value[0]
            elif value[0] == fence:
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines), fence


def anchors(text):
    found = set()
    counts = {}
    body, _ = prose(text)
    for line in body.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", match.group(1))
        title = re.sub(r"<[^>]*>", "", title).replace("`", "").lower()
        slug = "".join(c for c in title if c in "-_ " or unicodedata.category(c)[0] in "LNM")
        slug = slug.replace(" ", "-")
        index = counts.get(slug, 0)
        counts[slug] = index + 1
        found.add(slug if index == 0 else f"{slug}-{index}")
    return found


def main():
    errors = []
    links = 0
    files = sorted(p for p in ROOT.rglob("*.md") if not SKIP.intersection(p.relative_to(ROOT).parts))
    for path in files:
        body, fence = prose(path.read_text())
        if fence:
            errors.append(f"{path.relative_to(ROOT)}: unclosed code fence")
        for match in LINK.finditer(body):
            target = match.group(1).split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not dest.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing {target}")
            elif parsed.fragment and dest.is_file() and dest.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(dest.read_text()):
                    errors.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    modules = sorted((ROOT / "course/modules").glob("*.md"))
    if len(modules) != 12:
        errors.append(f"Expected 12 modules, found {len(modules)}")
    overview = (ROOT / "course/overview.md").read_text()
    for module in modules:
        if f"modules/{module.name}" not in overview:
            errors.append(f"Module absent from overview: {module.name}")
    ignore = (ROOT / ".gitignore").read_text().splitlines()
    if "student-workspace/" not in ignore:
        errors.append("student-workspace/ absent from .gitignore")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(files)} Markdown files, {links} local links/anchors, 12 module entries and workspace ignore.")
    print("External URLs, rendering and real learner behavior are not checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
