#!/usr/bin/env python3
"""Finalize script-free page snapshots into a fully self-contained site.

Usage: staticize.py <snap_dir>

Takes the DOM snapshots produced by snapshot.mjs, downloads every remaining
external resource (CSS, fonts, images) into docs/assets/, rewrites the
references, scrubs Wix branding, and installs the pages into docs/.
"""
import hashlib
import pathlib
import re
import subprocess
import sys

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"
CSS_DIR = DOCS / "assets" / "css"
FONT_DIR = DOCS / "assets" / "fonts"
MEDIA_DIR = DOCS / "assets" / "wixstatic"

EXT_RE = re.compile(
    r"https://(?:static\.wixstatic\.com|static\.parastorage\.com|"
    r"siteassets\.parastorage\.com|lh\d\.googleusercontent\.com)/[^\s\"'<>()\\]+"
)


def clean_match(url: str) -> str:
    return url.split("&quot;")[0].split("&#")[0]


def fetch(url: str) -> bytes | None:
    for _ in range(3):
        r = subprocess.run(
            ["curl", "-sfLg", "--max-time", "90", "--retry", "2", url],
            capture_output=True,
        )
        if r.returncode == 0:
            return r.stdout
    return None


def name_for(url: str) -> str:
    base = re.sub(r"[^A-Za-z0-9._-]", "_", url.split("?")[0].split("/")[-1]) or "asset"
    return f"{hashlib.sha1(url.encode()).hexdigest()[:10]}_{base}"[:150]


def localize_css(url: str, seen: dict[str, str]) -> str | None:
    """Download a stylesheet, localize url() refs inside it, return local path."""
    if url in seen:
        return seen[url]
    body = fetch(url)
    if body is None:
        return None
    css = body.decode("utf-8", "replace")
    css = re.sub(r"/\*# sourceMappingURL=[^*]*\*/", "", css)
    for ref in {clean_match(m) for m in EXT_RE.findall(css)}:
        local = localize_binary(ref, seen)
        if local:
            css = css.replace(ref, local)
    dest = CSS_DIR / (name_for(url).rsplit(".", 1)[0] + ".css")
    dest.write_bytes(css.encode())
    seen[url] = f"/assets/css/{dest.name}"
    return seen[url]


def localize_binary(url: str, seen: dict[str, str]) -> str | None:
    if url in seen:
        return seen[url]
    body = fetch(url)
    if body is None:
        print(f"  SKIP {url}")
        return None
    is_font = any(url.endswith(e) or e + "?" in url for e in (".woff", ".woff2", ".ttf", ".otf", ".eot"))
    d = FONT_DIR if is_font else MEDIA_DIR
    dest = d / name_for(url)
    dest.write_bytes(body)
    seen[url] = f"/assets/{'fonts' if is_font else 'wixstatic'}/{dest.name}"
    return seen[url]


def main() -> None:
    snap = pathlib.Path(sys.argv[1])
    for d in (CSS_DIR, FONT_DIR, MEDIA_DIR):
        d.mkdir(parents=True, exist_ok=True)
    seen: dict[str, str] = {}

    for src in sorted(snap.rglob("index.html")):
        rel = src.relative_to(snap)
        html = src.read_text(encoding="utf-8")

        # stylesheets first (their internals need font/image localization)
        for href in set(re.findall(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"', html)
                        + re.findall(r'<link[^>]+href="([^"]+)"[^>]+rel="stylesheet"', html)):
            if href.startswith("https://"):
                local = localize_css(href, seen)
                if local:
                    html = html.replace(href, local)

        # every other external CDN reference (images in src/srcset/inline styles)
        for url in sorted({clean_match(m) for m in EXT_RE.findall(html)}, key=len, reverse=True):
            local = (localize_css(url, seen) if url.split("?")[0].endswith(".css")
                     else localize_binary(url, seen))
            if local:
                html = html.replace(url, local)

        # scrub Wix branding
        html = html.replace(
            "Feeding Our Kids | Codify Kids | United States",
            "CodifyKids | Teaching the world to code, one kid at a time",
        )
        html = re.sub(r"\.?\s*Proudly created with\s*(<[^>]+>)*\s*Wix\.com\s*(</[^>]+>)*", ".", html)
        html = html.replace("Proudly created with Wix.com", "")

        dest = DOCS / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")

        leftovers = sorted(set(re.findall(r'https?://[^\s"\'<>\\)]+', html)))
        ext = [u for u in leftovers if not u.startswith(("https://www.codifykids.org",))
               and "codifykids" not in u
               and not any(h in u for h in ("facebook.com", "twitter.com", "linkedin.com",
                                            "instagram.com", "youtube.com", "wcia.com",
                                            "schema.org", "w3.org", "ogp.me"))]
        print(f"wrote {rel}  (external refs left: {len(ext)})")
        for u in ext[:8]:
            print(f"    ? {u}")


if __name__ == "__main__":
    main()
