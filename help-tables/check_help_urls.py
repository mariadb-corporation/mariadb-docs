#!/usr/bin/env python3
"""Check that every URL in a generated fill_help_tables.sql resolves directly.

A help-table URL is written into mysql.help_topic and ships with the server, so
it has to be the page's real published address. A URL that only resolves via a
redirect is a URL that stops resolving as soon as that redirect is retired, and
nothing in the docs repo watches for it.

    python3 help-tables/check_help_urls.py [path/to/fill_help_tables.sql]

Exits 1 if any URL does not return 200 without redirecting.
"""
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DEFAULT_SQL = Path(__file__).resolve().parent / "fill_help_tables.sql"
# Every docs URL in the file: both the "URL:" line inside a description and the
# url column of the INSERT. A description long enough to be truncated loses its
# URL: line, so matching only those would skip exactly those topics.
URL_RE = re.compile(r"(https://mariadb\.com/docs/[A-Za-z0-9_./#=-]*)")
WORKERS = 16
TIMEOUT = 30
RETRIES = 1
RETRY_DELAY = 2


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Report the redirect instead of following it — following hides the defect."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def status(url: str):
    """HEAD the URL. Retries once on a network-level error.

    A DNS blip or a timeout is not a finding, and one of them in a run of a
    thousand would otherwise fail the whole check.
    """
    opener = urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(url, method="HEAD")
    for attempt in range(RETRIES + 1):
        try:
            with opener.open(req, timeout=TIMEOUT) as resp:
                return url, resp.status, None
        except urllib.error.HTTPError as e:       # a real answer, including 3xx
            return url, e.code, e.headers.get("Location")
        except Exception as e:                    # network error, DNS, timeout
            if attempt == RETRIES:
                return url, None, str(e)
            time.sleep(RETRY_DELAY)


def main() -> int:
    sql_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SQL
    if not sql_path.exists():
        print(f"No such file: {sql_path} — run markdown_extractor.py first")
        return 2

    urls = sorted(set(URL_RE.findall(sql_path.read_text(encoding="utf-8"))))
    print(f"Checking {len(urls)} distinct URL(s) from {sql_path.name}")

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(status, urls))

    bad = [r for r in results if r[1] != 200]
    for url, code, detail in sorted(bad, key=lambda r: (r[1] is None, r[1] or 0, r[0])):
        if code is None:
            print(f"  ERROR {url}\n        {detail}")
        elif detail:
            print(f"  {code}   {url}\n        -> {detail}")
        else:
            print(f"  {code}   {url}")

    print(f"{len(urls) - len(bad)} direct 200, {len(bad)} not")
    if bad:
        print(
            "A redirecting URL usually means the page is published from a different "
            "place in SUMMARY.md than where it sits on disk; see DOCS-6643."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
