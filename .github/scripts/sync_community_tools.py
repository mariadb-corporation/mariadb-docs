#!/usr/bin/env python3
"""Sync the Community Tools docs from their product repos into tools/ (DOCS-6926).

The docs for MariaDB AI Plugins and MariaDB Shell are written in their own repos, under
docs-ref/content/, laid out as this repo's Tools space. This script copies them in, one way:

  docs-ref/content/community/<product>/   ->  tools/community/<product>/   (byte for byte*)
  the product's nav subtree               ->  tools/SUMMARY.md, under Community Tools
  its "## <title>" landing section        ->  tools/community/README.md
  its "### <title>" landing section       ->  tools/README.md, under Community Tools
  the images its pages use                ->  tools/.gitbook/assets/

* With one exception, nothing is rewritten on the way: a link to a page the sync doesn't
publish becomes plain text, and a content-ref to one is dropped. Such a page is either
excluded in the config (an unreleased feature, for example) or in a community/ folder that
isn't a synced product. The source keeps its links, so they come back on their own when the
exclusion goes. A fix to a synced page is made in the product repo, and the next sync brings
it back; a fix made here would be overwritten. That is also why the synced
pages carry no link aliases: expand-gitbook-aliases.yml would rewrite them, and the files
would stop matching their source. The script refuses a page that contains one.

Products, their repos and refs, and per-product exclusions (pages not published yet) are in
.github/community-tools.json. The script records what it synced, per product, under
"synced" in the same file: the source commit and the images it copied. The image list is
what lets the next sync remove an image the product no longer uses.

Usage:
  sync_community_tools.py --src <dir> [--product <key> ...] [--summary <file>]

  --src      directory holding one checkout per product, named after the product key
             (e.g. <dir>/mariadb-shell). The workflow checks them out there.
  --product  sync only these products (default: all in the config, except those on hold).
  --summary  write a Markdown summary of what changed, for the PR body.

Run from the repo root. Exit 0 on success, 1 on a content problem that must be fixed in the
product repo, 2 on a usage or setup error.
"""

import argparse
import fnmatch
import json
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

CONFIG = ".github/community-tools.json"
SPACE = "tools"
COMMUNITY = "community"
SOURCE_ROOT = "docs-ref/content"

# A link alias as dev-docs/link-aliases.md defines it: a link target that starts with
# {name}/ or is exactly {name}.
ALIAS = re.compile(r"\]\(\{[a-z0-9-]+\}(/|\))")
ASSET = re.compile(r"\.gitbook/assets/([^)\s\"'>]+)")
NAV_LINE = re.compile(r"^(\s*)\* \[[^\]]*\]\(([^)]+)\)")
# An inline Markdown link (not an image): [text](target) or [text](target "title").
LINK = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
CONTENT_REF = re.compile(r'\{% content-ref url="([^"]+)" %\}.*?\{% endcontent-ref %\}\n*', re.S)
FENCE = re.compile(r"^\s*(```|~~~)")


class ContentError(Exception):
    """A problem in the synced content. It has to be fixed in the product repo."""


def die(msg, code=2):
    print(f"sync_community_tools: {msg}", file=sys.stderr)
    sys.exit(code)


def excluded(rel, patterns):
    """True if a path relative to the product folder matches an exclude pattern."""
    return any(fnmatch.fnmatch(rel, p) or rel.startswith(p.rstrip("/") + "/")
               for p in patterns)


def unpublished_target(target, page_rel, key, patterns, products):
    """True if a link target on a page resolves to a page the sync doesn't publish: one this
    product excludes, or one in a community/ folder that isn't a synced product. page_rel is
    the page's path relative to the product folder."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith(("#", "/")):
        return False
    path = unquote(target.split("#", 1)[0])
    if not path:
        return False
    # Resolve against the source tree, docs-ref/content/, with the product at community/<key>/.
    resolved = os.path.normpath(os.path.join(COMMUNITY, key, os.path.dirname(page_rel), path))
    parts = resolved.split(os.sep)
    if len(parts) < 3 or parts[0] != COMMUNITY:
        return False
    if parts[1] == key:
        return excluded("/".join(parts[2:]), patterns)
    return parts[1] not in products


def unlink_unpublished(text, page_rel, key, patterns, products):
    """Return (text, count): links to unpublished pages turned into their link text, and
    content-refs to them dropped. Code blocks are left alone."""
    hit = lambda t: unpublished_target(t, page_rel, key, patterns, products)
    count = 0

    def ref(m):
        nonlocal count
        if hit(m.group(1)):
            count += 1
            return ""
        return m.group(0)

    def link(m):
        nonlocal count
        if hit(m.group(2)):
            count += 1
            return m.group(1)
        return m.group(0)

    out, block, fenced = [], [], False

    def flush():
        if block:
            out.append(LINK.sub(link, CONTENT_REF.sub(ref, "".join(block))))
            block.clear()

    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            if not fenced:
                flush()
            fenced = not fenced
            out.append(line)
        elif fenced:
            out.append(line)
        else:
            block.append(line)
    flush()
    return "".join(out), count


def image_used(image):
    """True if any page in the space still refers to the image (the working tree, so pages
    this run just copied count)."""
    for root, _dirs, files in os.walk(SPACE):
        for name in files:
            if name.endswith(".md"):
                with open(os.path.join(root, name), encoding="utf-8") as f:
                    if image in unquote(f.read()):
                        return True
    return False


def git_head(repo_dir):
    return subprocess.run(["git", "-C", repo_dir, "rev-parse", "HEAD"], check=True,
                          capture_output=True, text=True).stdout.strip()


def nav_subtree(lines, target):
    """Return (start, end) of the nav entry linking to target and its children, or None."""
    for i, line in enumerate(lines):
        m = NAV_LINE.match(line)
        if m and m.group(2) == target:
            indent = len(m.group(1))
            end = i + 1
            while end < len(lines):
                n = NAV_LINE.match(lines[end])
                if not lines[end].strip() or (n and len(n.group(1)) <= indent):
                    break
                if not n:
                    break
                end += 1
            return i, end
    return None


def filter_nav(lines, prefix, patterns):
    """Drop nav entries whose page is excluded, together with their children."""
    out, skip_indent = [], None
    for line in lines:
        m = NAV_LINE.match(line)
        indent = len(m.group(1)) if m else 0
        if skip_indent is not None:
            if m and indent > skip_indent:
                continue
            skip_indent = None
        if m and m.group(2).startswith(prefix):
            rel = m.group(2)[len(prefix):]
            if excluded(rel, patterns):
                skip_indent = indent
                continue
        out.append(line)
    return out


def section(text, heading):
    """Return the section that starts with the line `heading`, up to the next heading of the
    same or a higher level, or the licence footer. None if absent."""
    level = len(heading) - len(heading.lstrip("#"))
    lines = text.splitlines()
    try:
        start = lines.index(heading)
    except ValueError:
        return None
    end = start + 1
    while end < len(lines):
        line = lines[end]
        if line.startswith("<sub>"):
            break
        m = re.match(r"^(#+) ", line)
        if m and len(m.group(1)) <= level:
            break
        end += 1
    return start, end, lines


def replace_section(dest_path, src_path, heading):
    """Copy one landing-page section from the source stand-in into our landing page."""
    with open(src_path, encoding="utf-8") as f:
        src = section(f.read(), heading)
    if src is None:
        raise ContentError(f"{src_path} has no '{heading}' section.")
    s_start, s_end, s_lines = src
    block = s_lines[s_start:s_end]
    while block and not block[-1].strip():
        block.pop()

    with open(dest_path, encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    found = section(text, heading)
    if found:
        d_start, d_end, _ = found
        while d_end > d_start and not lines[d_end - 1].strip():
            d_end -= 1
        lines[d_start:d_end] = block
    else:
        # A new product goes last, before the licence footer.
        footer = next((i for i in range(len(lines) - 1, -1, -1)
                       if lines[i].startswith("<sub>")), len(lines))
        while footer > 0 and not lines[footer - 1].strip():
            footer -= 1
        lines[footer:footer] = [""] + block
    new = "\n".join(lines) + "\n"
    new = re.sub(r"\n{3,}", "\n\n", new)
    if new != text:
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(new)


def sync_product(key, cfg, src_repo, state, products):
    title, patterns = cfg["title"], cfg.get("exclude", [])
    src_content = os.path.join(src_repo, SOURCE_ROOT)
    src_dir = os.path.join(src_content, COMMUNITY, key)
    dest_dir = os.path.join(SPACE, COMMUNITY, key)
    if not os.path.isdir(src_dir):
        raise ContentError(f"{cfg['repo']} has no {SOURCE_ROOT}/{COMMUNITY}/{key}/.")

    # 1. The pages, byte for byte. Excluded pages are left out, and links to them unlinked.
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    pages, unlinked = [], 0
    for root, _dirs, files in os.walk(src_dir):
        for name in sorted(files):
            path = os.path.join(root, name)
            rel = os.path.relpath(path, src_dir)
            if excluded(rel, patterns):
                continue
            out = os.path.join(dest_dir, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            shutil.copyfile(path, out)
            if name.endswith(".md"):
                pages.append(out)
                with open(out, encoding="utf-8") as f:
                    text = f.read()
                new, n = unlink_unpublished(text, rel, key, patterns, products)
                if n:
                    with open(out, "w", encoding="utf-8") as f:
                        f.write(new)
                    unlinked += n

    # 2. No link aliases: the alias bot would rewrite them and break the byte-for-byte copy.
    problems = []
    images = set()
    for page in sorted(pages):
        with open(page, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                if ALIAS.search(line):
                    problems.append(f"{page}:{n}: link alias; synced pages need absolute "
                                    "https://mariadb.com/docs/... links")
                for m in ASSET.finditer(line):
                    images.add(unquote(m.group(1)))
    if problems:
        raise ContentError("\n".join(problems))

    # 3. The images the pages use. An image another page in the space already has under the
    #    same name, with different content, is a collision rather than an update.
    previous = set(state.get("assets", []))
    for image in sorted(images):
        src = os.path.join(src_content, ".gitbook", "assets", image)
        dest = os.path.join(SPACE, ".gitbook", "assets", image)
        if not os.path.isfile(src):
            raise ContentError(f"{cfg['repo']}: image .gitbook/assets/{image} is used but "
                               "missing.")
        if (os.path.exists(dest) and image not in previous
                and open(src, "rb").read() != open(dest, "rb").read()):
            raise ContentError(f"tools/.gitbook/assets/{image} already exists with other "
                               "content; rename the image in the product repo.")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(src, dest)

    # 4. The nav subtree, under Community Tools.
    prefix = f"{COMMUNITY}/{key}/"
    with open(os.path.join(src_content, "SUMMARY.md"), encoding="utf-8") as f:
        src_nav = f.read().splitlines()
    span = nav_subtree(src_nav, prefix + "README.md")
    if span is None:
        raise ContentError(f"{cfg['repo']}: SUMMARY.md has no entry for {prefix}README.md.")
    subtree = filter_nav(src_nav[span[0]:span[1]], prefix, patterns)

    summary_path = os.path.join(SPACE, "SUMMARY.md")
    with open(summary_path, encoding="utf-8") as f:
        nav = f.read().splitlines()
    mine = nav_subtree(nav, prefix + "README.md")
    if mine:
        nav[mine[0]:mine[1]] = subtree
    else:
        parent = nav_subtree(nav, f"{COMMUNITY}/README.md")
        if parent is None:
            die(f"{summary_path} has no Community Tools entry.")
        nav[parent[1]:parent[1]] = subtree
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(nav) + "\n")

    # 5. The landing-page sections.
    replace_section(os.path.join(SPACE, COMMUNITY, "README.md"),
                    os.path.join(src_content, COMMUNITY, "README.md"), f"## {title}")
    replace_section(os.path.join(SPACE, "README.md"),
                    os.path.join(src_content, "README.md"), f"### {title}")

    # 6. Images this product used to have and no page in the space uses any more.
    gone = []
    for image in sorted(previous - images):
        path = os.path.join(SPACE, ".gitbook", "assets", image)
        if os.path.exists(path) and not image_used(image):
            os.remove(path)
            gone.append(image)

    return ({"commit": git_head(src_repo), "assets": sorted(images)}, len(pages), gone,
            unlinked)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--src", required=True)
    ap.add_argument("--product", action="append")
    ap.add_argument("--summary")
    args = ap.parse_args()

    if not os.path.isfile(CONFIG) or not os.path.isdir(SPACE):
        die("run from the mariadb-docs repo root.")
    with open(CONFIG, encoding="utf-8") as f:
        config = json.load(f)
    products = config["products"]
    keys = args.product or [k for k, v in products.items() if not v.get("hold")]
    unknown = [k for k in keys if k not in products]
    if unknown:
        die(f"unknown product(s): {', '.join(unknown)}")

    synced = config.setdefault("synced", {})
    report = []
    try:
        for key in keys:
            cfg = products[key]
            src_repo = os.path.join(args.src, key)
            if not os.path.isdir(os.path.join(src_repo, ".git")):
                die(f"no checkout of {cfg['repo']} at {src_repo}.")
            state, count, gone, unlinked = sync_product(key, cfg, src_repo,
                                                        synced.get(key, {}), products)
            old = synced.get(key, {}).get("commit")
            synced[key] = state
            line = (f"- **{cfg['title']}**: {count} pages from "
                    f"[`{cfg['repo']}@{state['commit'][:9]}`]"
                    f"(https://github.com/{cfg['repo']}/commit/{state['commit']})")
            if old and old != state["commit"]:
                line += (f", [changes since `{old[:9]}`]"
                         f"(https://github.com/{cfg['repo']}/compare/{old}...{state['commit']})")
            if cfg.get("exclude"):
                line += f"; not published: {', '.join(f'`{p}`' for p in cfg['exclude'])}"
            if unlinked:
                line += f"; {unlinked} link(s) to unpublished pages turned into plain text"
            if gone:
                line += f"; removed unused images: {', '.join(gone)}"
            report.append(line)
            print(line)
    except ContentError as e:
        print(f"sync_community_tools: fix this in the product repo, then sync again:\n{e}",
              file=sys.stderr)
        sys.exit(1)

    with open(CONFIG, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
        f.write("\n")
    if args.summary:
        with open(args.summary, "w", encoding="utf-8") as f:
            f.write("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
