#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261121.

A one-page newspaper front page summing up Saturday 21 November 2026.
Own code, written fresh in this session. Pillow only, deterministic
(fixed seed, no timestamps, no network). Output: 1024x1024 RGB PNG.
"""
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = Path(__file__).with_name("entry.png")

PAPER = (248, 244, 232)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
RED = (185, 28, 28)
GOLD = (201, 162, 39)
GRAY = (90, 90, 90)
LIGHT = (238, 232, 218)
BLUE = (47, 93, 138)
GREEN = (46, 125, 50)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name, size):
    for cand in (FONT_DIR / name, Path("/usr/share/fonts/truetype/liberation") / name):
        if cand.exists():
            return ImageFont.truetype(str(cand), size)
    return ImageFont.load_default()


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)  # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)  # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, max_w, fill=INK, leading=None):
    x, y = xy
    lh = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def rule(draw, y, x0=28, x1=996, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def night_attack(draw, box):
    x0, y0, x1, y1 = box
    rng = random.Random(21112026)
    # sky gradient: deep navy top to dusk orange near horizon
    steps = 24
    top, bot = (16, 24, 54), (64, 48, 74)
    for i in range(steps):
        t = i / (steps - 1)
        col = tuple(int(top[c] + (bot[c] - top[c]) * t) for c in range(3))
        yy0 = y0 + (y1 - y0) * i // steps
        yy1 = y0 + (y1 - y0) * (i + 1) // steps
        draw.rectangle([x0, yy0, x1, yy1], fill=col)
    # stars
    for _ in range(46):
        sx = rng.randint(x0 + 4, x1 - 4)
        sy = rng.randint(y0 + 4, y0 + int((y1 - y0) * 0.55))
        r = rng.choice([1, 1, 2])
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(235, 235, 220))
    # missile trails
    for (mx, my, ang, ln) in [(x0 + 60, y0 + 150, -32, 120), (x0 + 210, y0 + 110, -24, 100), (x0 + 300, y0 + 190, -40, 90)]:
        import math
        dx, dy = math.cos(math.radians(ang)) * ln, math.sin(math.radians(ang)) * ln
        draw.line([(mx, my), (mx + dx, my + dy)], fill=(255, 190, 90), width=4)
        draw.ellipse([mx + dx - 5, my + dy - 5, mx + dx + 5, my + dy + 5], fill=(255, 220, 130))
    # explosion glow
    ex, ey = x0 + 300, y0 + 205
    for r, col in [(46, (255, 140, 40)), (30, (255, 190, 80)), (16, (255, 235, 160))]:
        draw.ellipse([ex - r, ey - r, ex + r, ey + r], fill=col)
    # skyline silhouette
    base = y1
    cx = x0
    while cx < x1:
        bw = rng.randint(26, 52)
        bh = rng.randint(40, 110)
        draw.rectangle([cx, base - bh, min(cx + bw, x1), base], fill=(10, 14, 30))
        for _ in range(bh // 14):
            wx = rng.randint(cx + 4, max(cx + 5, min(cx + bw - 6, x1 - 6)))
            wy = rng.randint(base - bh + 6, base - 10)
            draw.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 214, 120))
        cx += bw + rng.randint(2, 8)


def chart(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle([x0, y0, x1, y1], fill=(255, 255, 255), outline=(200, 200, 200))
    draw.text((x0 + 8, y0 + 3), "S&P 500  -3.7%", font=SANS_B(14), fill=RED)
    draw.text((x1 - 8, y0 + 3), "NASDAQ  -5.3%", font=SANS_B(14), fill=(90, 90, 90), anchor="ra")
    top, bot = y0 + 20, y1 - 6
    pts = []
    n = 9
    for i in range(n):
        px = x0 + 12 + (x1 - x0 - 24) * i / (n - 1)
        py = top + (bot - top) * (0.08 + 0.84 * (i / (n - 1)) + (0.04 if i % 3 == 0 else -0.02))
        pts.append((px, py))
    draw.line(pts, fill=RED, width=3, joint="curve")
    for px, py in pts:
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)


def scales(draw, box):
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    mid = y0 + int((y1 - y0) * 0.30)
    draw.line([(cx, y0 + 2), (cx, y1 - 6)], fill=NAVY, width=4)
    draw.line([(x0 + 24, mid), (x1 - 24, mid)], fill=NAVY, width=4)
    draw.ellipse([cx - 5, y0 - 2, cx + 5, y0 + 8], fill=GOLD)
    for sx in (x0 + 24, x1 - 24):
        draw.line([(sx, mid), (sx, mid + 8)], fill=NAVY, width=2)
        draw.pieslice([sx - 18, mid + 6, sx + 18, mid + 26], 0, 180, fill=GOLD, outline=NAVY)
    draw.rectangle([cx - 26, y1 - 6, cx + 26, y1 - 2], fill=NAVY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 112], fill=NAVY)
    d.text((W // 2, 12), "THE WORLD", font=SERIF_B(84), fill=(255, 255, 255), anchor="ma")
    d.rectangle([0, 112, W, 116], fill=GOLD)
    d.text((28, 126), "SATURDAY, 21 NOVEMBER 2026", font=SANS_B(25), fill=RED)
    d.text((996, 128), "THE DAY IN ONE PICTURE", font=SANS_B(19), fill=GRAY, anchor="ra")
    rule(d, 152)

    # --- lead story: Russia strikes / Poland ---
    d.text((28, 164), "WAR IN EUROPE", font=SANS_B(20), fill=RED)
    y = para(d, (28, 192), "RUSSIA'S BIGGEST STRIKES HIT KYIV \u2014 MISSILES LAND IN POLAND",
             SERIF_B(37), 570)
    para(d, (28, y + 8),
         "More than 400 drones and 110 missiles fired overnight; at least eight "
         "killed in Kyiv. Warsaw calls the Polish landings a deliberate provocation.",
         SERIF(21), 570)
    night_attack(d, (620, 162, 996, 462))
    d.text((620, 466), "Kyiv under fire overnight \u2014 and a missile in Poland.",
           font=SANS(15), fill=GRAY)
    rule(d, 486)

    # --- row 2: markets | justice ---
    d.text((28, 498), "MARKETS", font=SANS_B(19), fill=RED)
    y = para(d, (28, 524), "AI ROUT DRAGS S&P 500 INTO CORRECTION", SERIF_B(29), 468)
    para(d, (28, y + 6), "Wall Street slides 3.7% as chip stocks plunge; Nvidia falls "
         "13.8% on an SEC probe.", SERIF(20), 468)
    chart(d, (28, 658, 496, 710))
    d.text((528, 498), "JUSTICE \u2014 THE HAGUE", font=SANS_B(19), fill=RED)
    y = para(d, (528, 524), "COURT: MYANMAR GUILTY OF ROHINGYA GENOCIDE", SERIF_B(29), 468)
    para(d, (528, y + 6), "World court rules 9\u20136 \u2014 the first time a state is held "
         "responsible for genocide.", SERIF(20), 468)
    scales(d, (600, 660, 924, 706))
    rule(d, 718)

    # --- row 3: diplomacy | health (text-only, room to breathe) ---
    d.text((28, 730), "DIPLOMACY \u2014 SHENZHEN", font=SANS_B(19), fill=RED)
    y = para(d, (28, 756), "TRUMP, XI AND PUTIN MEET IN SHENZHEN",
             SERIF_B(27), 468)
    para(d, (28, y + 6), "The first three-way summit ends in a 90-minute press conference; "
         "Trump calls the talks \u2018very good\u2019.", SERIF(20), 468)
    d.text((528, 730), "HEALTH", font=SANS_B(19), fill=RED)
    y = para(d, (528, 756), "CANCER PILL MAKES TUMOURS VANISH IN 1 IN 12",
             SERIF_B(27), 468)
    para(d, (528, y + 6), "Trial drug daraxonrasib leaves cancer undetectable on scans in "
         "one in 12 patients.", SERIF(20), 468)
    rule(d, 906)

    # --- bottom strip: four minis ---
    minis = [
        ("UK\u2013EU TRADE & YOUTH DEALS",
         "Checks scrapped from 2028."),
        ("COP31 TALKS STALL",
         "Draft drops fossil fuels."),
        ("VAN GOGH SELLS FOR $190M",
         "Record price at auction."),
        ("VOYAGER 1: ONE LIGHT-DAY",
         "First human object so far."),
    ]
    col_w = 242
    for i, (head, deck) in enumerate(minis):
        x = 28 + i * col_w
        y = para(d, (x, 918), "\u25aa  " + head, SANS_B(15), col_w - 12, leading=19)
        para(d, (x, y + 3), deck, SANS(14), col_w - 12, fill=GRAY, leading=17)

    # --- footer ---
    rule(d, 996, fill=(180, 180, 180))
    d.text((W // 2, 1000), "The World \u2014 Saturday 21 November 2026  \u2022  Summed up for make.fun",
           font=SANS(14), fill=GRAY, anchor="ma")

    img.save(OUT, "PNG")
    print("wrote", OUT, img.size, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
