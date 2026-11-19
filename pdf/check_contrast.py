#!/usr/bin/env python3
"""Assert that every text/background pair in pdf/style.css meets WCAG 2.1 AA.

    python3 pdf/check_contrast.py

Accessibility is a stated requirement for these PDFs, and contrast is easy to
break by eye -- dimming white to 75% over the previous brand's blue cover looked
fine on screen and landed at 4.45:1, under the 4.5:1 floor for body text. The pairs are listed
explicitly here rather than parsed out of the CSS: the point is to state the
intended contract, so a styling change that violates it fails loudly.

Thresholds (WCAG 2.1): 4.5:1 normal text, 3:1 large text (>=18pt, or >=14pt
bold). Exits non-zero on any failure.
"""

import sys

# MariaDB brand, Enterprise Platform 2027 (https://mariadb-brand-core.vercel.app/).
ULTRAVIOLET = "#8328ED"
WAVE = "#3DD3EE"
KELP = "#26D044"
BEACON = "#FFD401"
TRENCH = "#0C0C0D"
FOAM = "#F8F6FA"
NEUTRAL_100 = "#EBE8F0"
NEUTRAL_300 = "#C5C2CD"
NEUTRAL_700 = "#514E55"

INK = TRENCH
MUTED = NEUTRAL_700
WHITE = "#ffffff"
CODE_BG = FOAM

# Callout tints (pdf/style.css, .hint-*)
INFO_TINT = "#f3ebfd"
SUCCESS_TINT = "#e9f9ec"
WARNING_TINT = "#fff8d6"
DANGER_TINT = "#fceeed"

# (description, foreground, background, is_large_text)
PAIRS = [
    # body
    ("body text on white",             INK,     WHITE,   False),
    ("muted text (neutral 700)",       MUTED,   WHITE,   False),
    ("link (Ultraviolet) on white",    ULTRAVIOLET, WHITE, False),
    ("heading (Trench) on white",      INK,     WHITE,   True),
    ("h5/h6 (neutral 700) on white",   MUTED,   WHITE,   False),
    ("inline code on Foam",            INK,     CODE_BG, False),
    ("link inside a code-tinted cell", ULTRAVIOLET, CODE_BG, False),

    # cover: Ultraviolet
    ("cover-ultraviolet title",        WHITE,   ULTRAVIOLET, True),
    ("cover-ultraviolet eyebrow/meta", WHITE,   ULTRAVIOLET, False),
    ("cover-ultraviolet legal (8.5pt)", WHITE,  ULTRAVIOLET, False),

    # cover: Foam
    ("cover-foam title",               INK,     FOAM,    True),
    ("cover-foam legal (8.5pt)",       INK,     FOAM,    False),

    # toc
    ("toc entry on white",             INK,     WHITE,   False),
    ("toc deep entry (neutral 700)",   MUTED,   WHITE,   False),

    # callouts -- text and links sit on the tinted background
    ("note text on info tint",         INK,     INFO_TINT, False),
    ("tip text on success tint",       INK,     SUCCESS_TINT, False),
    ("warning text on warning tint",   INK,     WARNING_TINT, False),
    ("important text on danger tint",  INK,     DANGER_TINT, False),
    ("hint text on neutral Foam",      INK,     FOAM,    False),
    ("link on info tint",              ULTRAVIOLET, INFO_TINT, False),
    ("link on success tint",           ULTRAVIOLET, SUCCESS_TINT, False),
    ("link on warning tint",           ULTRAVIOLET, WARNING_TINT, False),
    ("link on danger tint",            ULTRAVIOLET, DANGER_TINT, False),

    # tables
    ("table header on neutral 100",    INK,     NEUTRAL_100, False),
    ("link in table header",           ULTRAVIOLET, NEUTRAL_100, False),
    ("table cell on white",            INK,     WHITE,   False),

    # tabs and steppers
    ("tab label (neutral 700)",        MUTED,   WHITE,   False),
    ("step label (Trench)",            INK,     WHITE,   False),
]

# Decorative fills: never carry text, so they are exempt from the text
# thresholds but must still be discernible against what they sit on.
DECORATIVE = [
    ("Ultraviolet rule on white",      ULTRAVIOLET, WHITE),
    ("Beacon rule on Ultraviolet",     BEACON,  ULTRAVIOLET),
    ("Ultraviolet rule on Foam",       ULTRAVIOLET, FOAM),
    ("Kelp tip bar on its tint",       KELP,    SUCCESS_TINT),
    ("Beacon warning bar on its tint", BEACON,  WARNING_TINT),
    ("neutral 300 code/step rule",     NEUTRAL_300, WHITE),
    ("Wave (unused; for reference)",   WAVE,    WHITE),
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
