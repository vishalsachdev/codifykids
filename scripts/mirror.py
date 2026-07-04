#!/usr/bin/env python3
"""Mirror www.codifykids.org (Wix) into a static site for GitHub Pages.

Fetches every page from the sitemap, downloads media from static.wixstatic.com
into assets/wixstatic/, and rewrites URLs so pages are self-contained except
for the Wix runtime JS/CSS on static.parastorage.com (kept remote).
"""
import hashlib
import pathlib
import re
import subprocess
import sys
import urllib.parse

SITE = "https://www.codifykids.org"
OUT = pathlib.Path(__file__).resolve().parent.parent / "docs"
ASSETS = OUT / "assets" / "wixstatic"

PAGES = [
    "/",
    "/register",
    "/blog-1",
    "/post/2018/10/28/three-camps-down-many-more-to-go",
    "/post/2016/05/08/finding-support-and-help-how-your-community-can-make-a-difference",
    "/post/2020/01/06/new-camp-at-the-champaign-public-library",
    "/post/a-new-type-of-camp-fun-with-ai",
    "/post/2018/10/27/our-hard-work-was-noticed",
]

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def fetch(url: str) -> bytes:
    last = None
    for _ in range(3):
        r = subprocess.run(
            ["curl", "-sfL", "--max-time", "90", "--retry", "2", "-A", UA, url],
            capture_output=True,
        )
        if r.returncode == 0:
            return r.stdout
        last = r
    raise RuntimeError(f"curl failed ({last.returncode}) for {url}")


def local_asset_name(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = urllib.parse.unquote(parsed.path)
    base = path.split("/")[-1] or "asset"
    base = re.sub(r"[^A-Za-z0-9._-]", "_", base)
    # Same media file appears with many transform paths (/v1/fill/...): hash full URL
    h = hashlib.sha1(url.encode()).hexdigest()[:10]
    return f"{h}_{base}"[:150]


def page_out_path(path: str) -> pathlib.Path:
    path = path.strip("/")
    return OUT / "index.html" if not path else OUT / path / "index.html"


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    asset_map: dict[str, str] = {}  # original url -> local rel path from site root
    htmls: dict[pathlib.Path, str] = {}

    wix_re = re.compile(r"https:(?:\\/\\/|//)static\.wixstatic\.com(?:\\/|/)[^\s\"'<>\\)]+")

    for page in PAGES:
        url = SITE + page
        print(f"fetch {url}", flush=True)
        html = fetch(url).decode("utf-8", "replace")
        htmls[page_out_path(page)] = html
        for m in wix_re.findall(html):
            clean = m.replace("\\/", "/")
            asset_map.setdefault(clean, "/assets/wixstatic/" + local_asset_name(clean))

    print(f"{len(asset_map)} unique wixstatic assets", flush=True)
    ok = fail = 0
    for src, dest in sorted(asset_map.items()):
        p = OUT / dest.lstrip("/")
        if p.exists():
            ok += 1
            continue
        try:
            p.write_bytes(fetch(src))
            ok += 1
        except Exception as e:
            print(f"  SKIP {src}: {e}", flush=True)
            asset_map[src] = src  # leave pointing at CDN
            fail += 1
    print(f"assets: {ok} ok, {fail} failed", flush=True)

    for out_path, html in htmls.items():
        for src, dest in asset_map.items():
            if dest == src:
                continue
            html = html.replace(src, dest)
            html = html.replace(src.replace("/", "\\/"), dest.replace("/", "\\/"))
            enc = src.replace("/", "%2F")  # occasionally fully URL-encoded in params
            if enc in html:
                html = html.replace(enc, dest.replace("/", "%2F"))
        # internal links -> root-relative
        html = html.replace(SITE + "/", "/").replace(SITE, "/")
        html = html.replace("https:\\/\\/www.codifykids.org\\/", "\\/")
        # remove the Wix free-plan banner: flip the flag the runtime reads,
        # plus a CSS belt-and-suspenders override
        html = html.replace('"freemiumBanner":true', '"freemiumBanner":false')
        html = html.replace("freemiumBanner=true", "freemiumBanner=false")
        html = html.replace(
            "</head>",
            "<style>#WIX_ADS{display:none!important}"
            ":root,body{--wix-ads-height:0px!important}</style></head>",
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")
        print(f"wrote {out_path.relative_to(OUT)}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
