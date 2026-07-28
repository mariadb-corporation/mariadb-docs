#!/usr/bin/env python3
"""Assert that every text/background pair in pdf/style.css meets WCAG 2.1 AA.

    python3 pdf/check_contrast.py

Accessibility is a stated requirement for these PDFs, and contrast is easy to
break by eye -- dimming white to 75% over Blue Azure looks fine on screen and
lands at 4.45:1, under the 4.5:1 floor for body text. The pairs are listed
explicitly here rather than parsed out of the CSS: the point is to state the
intended contract, so a styling change that violates it fails loudly.

Thresholds (WCAG 2.1): 4.5:1 normal text, 3:1 large text (>=18pt, or >=14pt
bold). Exits non-zero on any failure.
"""

import sys

# MariaDB brand palette, slide 26 of the corporate deck.
AZURE = "#0E6488"
SEA = "#96DDCF"
GRANITE = "#424F62"
SEAS = "#00838F"
SEAS_TEXT = "#00707a"   # darkened Open Seas for small text
OCEAN = "#003545"
EEL = "#ABC74A"

INK = "#12242b"
MUTED = GRANITE
WHITE = "#ffffff"
CODE_BG = "#f4f7f8"
COVER_AZURE_DIM = "#d9ece6"

# (description, foreground, background, is_large_text)
PAIRS = [
    # body
    ("body text on white",             INK,     WHITE,   False),
    ("muted text (Granite) on white",  MUTED,   WHITE,   False),
    ("link (Blue Azure) on white",     AZURE,   WHITE,   False),
    ("heading (Blue Azure) on white",  AZURE,   WHITE,   True),
    ("top heading (Deep Ocean)",       OCEAN,   WHITE,   True),
    ("inline code on code tint",       "#14252c", CODE_BG, False),
    ("code block text on tint",        INK,     CODE_BG, False),

    # cover: Blue Azure
    ("cover-azure title",              WHITE,   AZURE,   True),
    ("cover-azure subtitle",           COVER_AZURE_DIM, AZURE, True),
    ("cover-azure meta (10pt)",        COVER_AZURE_DIM, AZURE, False),
    ("cover-azure legal (8.5pt)",      COVER_AZURE_DIM, AZURE, False),
    ("cover-azure link",               WHITE,   AZURE,   False),

    # cover: Sea Fresh
    ("cover-sea title",                OCEAN,   SEA,     True),
    ("cover-sea subtitle",             OCEAN,   SEA,     True),
    ("cover-sea meta (10pt)",          OCEAN,   SEA,     False),
    ("cover-sea legal (8.5pt)",        OCEAN,   SEA,     False),

    # toc
    ("toc entry on white",             INK,     WHITE,   False),
    ("toc deep entry (Granite)",       MUTED,   WHITE,   False),
    ("toc heading (Deep Ocean)",       OCEAN,   WHITE,   True),

    # callouts -- text sits on the tinted background
    ("note text on info tint",         INK,     "#eaf2f6", False),
    ("tip text on success tint",       INK,     "#e4f4ef", False),
    ("warning text on warning tint",   INK,     "#fdf4e6", False),
    ("important text on danger tint",  INK,     "#fceeed", False),
    ("hint label on neutral tint",     INK,     "#f5f7f8", False),

    # tables
    ("table header on Sea Fresh tint", INK,     "#e4f4ef", False),
    ("table cell on white",            INK,     WHITE,   False),

    # tabs and steppers
    ("tab label (Open Seas dk) on white", SEAS_TEXT, WHITE, False),
    ("step label (Deep Ocean)",        OCEAN,   WHITE,   False),
]

# Decorative fills: never carry text, so they are exempt from the text
# thresholds but must still be discernible against what they sit on.
DECORATIVE = [
    ("Electric Eel rule on white",     EEL,     WHITE),
    ("Electric Eel rule on azure",     EEL,     AZURE),
    ("Electric Eel rule on sea fresh", EEL,     SEA),
    ("Sea Fresh step rule on white",   SEA,     WHITE),
]


def _channel(value):
    value /= 255
    return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4


def luminance(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def contrast(fg, bg):
    a, b = luminance(fg), luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def main():
    failures = []
    print(f"{'pair':36} {'ratio':>6}  {'need':>5}  result")
    print("-" * 62)
    for label, fg, bg, large in PAIRS:
        ratio = contrast(fg, bg)
        need = 3.0 if large else 4.5
        ok = ratio >= need
        grade = "AAA" if ratio >= (4.5 if large else 7) else ("AA" if ok else "FAIL")
        print(f"{label:36} {ratio:6.2f}  {need:5.1f}  {grade}")
        if not ok:
            failures.append((label, fg, bg, ratio, need))

    print()
    print("decorative (no text, informational only):")
    for label, fg, bg in DECORATIVE:
        print(f"  {label:34} {contrast(fg, bg):6.2f}")

    print()
    if failures:
        print(f"FAIL: {len(failures)} pair(s) below WCAG AA")
        for label, fg, bg, ratio, need in failures:
            print(f"  {label}: {fg} on {bg} = {ratio:.2f}, needs {need:.1f}")
        return 1
    print(f"PASS: all {len(PAIRS)} text pairs meet WCAG 2.1 AA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
