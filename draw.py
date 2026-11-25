#!/usr/bin/env python3
"""Render the front page of THE TUESDAY GLOBE for Tuesday 24 November 2026.

Draws a 1024x1024 newspaper front page with Pillow: masthead, one lead
story, a grid of short stories and a footer ticker. The render is fully
deterministic: no randomness, no timestamps, no network.
"""

import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 28
PAPER = (247, 243, 232)
INK = (17, 17, 17)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
GREY = (90, 86, 76)
RULE = (120, 114, 100)
LIGHT = (232, 226, 210)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_BOLD = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Wrap text to the given pixel width, returning a list of lines."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, lines, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def fit_lines(draw, text, fnt, max_w, max_lines):
    """Wrap text and clip to max_lines, adding an ellipsis if clipped."""
    lines = wrap(draw, text, fnt, max_w)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and draw.textlength(lines[-1] + " ...", font=fnt) > max_w:
            lines[-1] = lines[-1].rsplit(" ", 1)[0]
        lines[-1] = lines[-1] + " ..."
    return lines


LEAD = {
    "kicker": "TECHNOLOGY  ·  MARKETS",
    "headline": "HUANG BACK AT NVIDIA AFTER TRUMP STEPS IN",
    "summary": (
        "Nvidia reinstates Jensen Huang as chief executive and chair less "
        "than two weeks after he resigned, reportedly after pressure from "
        "Donald Trump. Shares surge 31.5%, adding a record $952bn of market "
        "value in a single day and lifting Wall Street to its best day in "
        "over a year."
    ),
    "stats": "NVDA +31.5%   ·   +$952bn — BIGGEST ONE-DAY GAIN EVER   ·   "
             "NASDAQ +6.5%   ·   S&P 500 +4.7%",
}

# (kicker, headline, summary) — 18 stories, 3 columns x 6 rows.
STORIES = [
    ("MIDDLE EAST",
     "Netanyahu urges Trump to hit Iran again",
     "Israel's PM presses Washington to resume strikes; advisers are split on bombing versus blockade."),
    ("SPACE",
     "Russia may put a nuclear weapon in orbit",
     "Western intelligence warns of a satellite launch as early as December; NATO vows to defend space."),
    ("EUROPE",
     "Moscow: Estonia is near 'open war'",
     "Russia warns Tallinn after it moves to shut its land border from 1 December."),
    ("CONFLICT",
     "Kyiv: we sank a Russian warship off Libya",
     "Ukraine says naval drones hit two Russian vessels near Benghazi; the UN seeks a probe."),
    ("CONFLICT",
     "700,000 Russian soldiers dead, data shows",
     "Leaked statistics point to a toll far above official figures; Medvedev warns of a 'preventive' strike."),
    ("ASIA",
     "Solomon Islands drops China security pact",
     "Honiara will let the 2022 deal lapse and sign a new security treaty with Australia instead."),
    ("ASIA",
     "UK sanctions Myanmar generals",
     "Britain acts after the world court ruled Myanmar committed genocide against the Rohingya."),
    ("WORLD",
     "Wars put food aid for 7.3m at risk",
     "The World Food Programme warns fighting is choking the routes that carry relief."),
    ("CLIMATE",
     "COP31 ends with no deal",
     "The UN climate summit fails amid a split over fossil fuels and finance for poorer nations."),
    ("HEALTH",
     "US loses measles-free status",
     "After 25 years, elimination is gone; Pennsylvania records a ninth death in the outbreak."),
    ("BUSINESS",
     "Sanofi to buy Insmed for $41bn",
     "The French drugmaker agrees the biggest biotech deal in nearly three years."),
    ("BUSINESS",
     "CrowdStrike to buy Zscaler for $43.9bn",
     "The all-stock deal is the latest mega-merger in cybersecurity."),
    ("TECH",
     "States sue Musk firms over Grok images",
     "Oregon and Virginia lead a suit over sexualised AI images of children from the chatbot."),
    ("TECH",
     "UN chief: agree AI safety rules in a year",
     "Guterres calls for a multilateral framework as AI shifts power, he warns."),
    ("SCIENCE",
     "Most distant black hole yet found",
     "Astronomers spot a quasar glowing within 630 million years of the Big Bang."),
    ("MIDDLE EAST",
     "Gaza strikes kill three, UN warns",
     "Israeli strikes kill an UNRWA worker; the UN says the war undid 77 years of development."),
    ("SPORT",
     "Guirassy double powers Dortmund 4-0",
     "Borussia Dortmund rout 10-man Villarreal in the Champions League."),
    ("SPACE",
     "Pakistani astronaut to fly to Tiangong",
     "Zeeshan Ali will be the first foreign astronaut aboard China's space station."),
]

TICKER = (
    "TO WATCH  —  US Thanksgiving travel braces for record king tides  ·  "
    "EU unveils a 22nd Russia sanctions package  ·  Second US carrier heads "
    "for the Gulf  ·  Champions League continues Wednesday"
)


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.line([(MARGIN, 18), (W - MARGIN, 18)], fill=RULE, width=2)
    title = "THE TUESDAY GLOBE"
    tf = SERIF_BOLD(64)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 26), title, font=tf, fill=INK)

    # Dateline row: edition info left, date centre, tagline right.
    df = SANS_BOLD(15)
    date = "TUESDAY 24 NOVEMBER 2026"
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 104), date, font=df, fill=RED)
    small = SANS(12)
    d.text((MARGIN, 106), "No. 329", font=small, fill=GREY)
    tag = "ONE IMAGE · THE WHOLE DAY"
    d.text((W - MARGIN - d.textlength(tag, font=small), 106), tag,
           font=small, fill=GREY)

    d.line([(MARGIN, 128), (W - MARGIN, 128)], fill=INK, width=3)
    d.line([(MARGIN, 133), (W - MARGIN, 133)], fill=INK, width=1)

    # ---- Lead story -----------------------------------------------------
    y = 148
    kf = SANS_BOLD(15)
    d.text((MARGIN, y), LEAD["kicker"], font=kf, fill=RED)
    y += 24
    hf = SANS_BOLD(40)
    head_lines = fit_lines(d, LEAD["headline"], hf, W - 2 * MARGIN, 2)
    y = draw_wrapped(d, MARGIN, y, head_lines, hf, INK, 46)
    y += 6
    sf = SERIF(17)
    sum_lines = fit_lines(d, LEAD["summary"], sf, W - 2 * MARGIN, 4)
    y = draw_wrapped(d, MARGIN, y, sum_lines, sf, INK, 23)
    y += 10
    # Stat strip.
    stf = SANS_BOLD(14)
    sw = d.textlength(LEAD["stats"], font=stf)
    d.rectangle([MARGIN, y, MARGIN + sw + 20, y + 30], fill=NAVY)
    d.text((MARGIN + 10, y + 7), LEAD["stats"], font=stf, fill=(255, 255, 255))
    y += 30

    # Rule above the grid.
    gy = y + 16
    d.line([(MARGIN, gy), (W - MARGIN, gy)], fill=INK, width=2)

    # ---- Story grid: 3 columns x 6 rows --------------------------------
    cols, rows = 3, 6
    gx0, gx1 = MARGIN, W - MARGIN
    col_gap = 18
    col_w = (gx1 - gx0 - (cols - 1) * col_gap) // cols
    grid_top = gy + 12
    grid_bottom = 958
    row_h = (grid_bottom - grid_top) // rows
    for i, (kicker, headline, summary) in enumerate(STORIES):
        r, c = divmod(i, cols)
        x = gx0 + c * (col_w + col_gap)
        top = grid_top + r * row_h
        # Column separators.
        if c:
            d.line([(x - col_gap // 2, top + 4),
                    (x - col_gap // 2, top + row_h - 10)],
                   fill=LIGHT, width=1)
        cy = top
        d.text((x, cy), kicker, font=SANS_BOLD(11), fill=RED)
        cy += 16
        hl = fit_lines(d, headline, SANS_BOLD(15), col_w, 2)
        cy = draw_wrapped(d, x, cy, hl, SANS_BOLD(15), INK, 18)
        cy += 2
        sl = fit_lines(d, summary, SANS(12), col_w, 2)
        draw_wrapped(d, x, cy, sl, SANS(12), (60, 58, 50), 15)

    # ---- Footer ticker --------------------------------------------------
    d.rectangle([0, 966, W, H], fill=NAVY)
    tf2 = SANS_BOLD(13)
    ticker_lines = wrap(d, TICKER, tf2, W - 2 * MARGIN)
    ty = 966 + (H - 966 - len(ticker_lines) * 17) // 2
    draw_wrapped(d, MARGIN, ty, ticker_lines, tf2, (255, 255, 255), 17)
    return img


def main():
    img = render()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, format="PNG")
    data = open(out, "rb").read()
    print(f"wrote {out}: {len(data)} bytes, "
          f"sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
