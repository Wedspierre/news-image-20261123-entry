#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news front page (1024x1024 PNG).

Deterministic: fixed palette, fixed layout, fixed fonts, no timestamps.
Run: python3 draw.py  -> writes entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 243, 234)
INK = (17, 17, 17)
PAPER = (255, 253, 247)
RED = (158, 27, 27)
BLUE = (18, 52, 96)
GOLD = (176, 124, 18)
GREY = (90, 88, 80)
LINE = (200, 192, 172)

FDIR = "/usr/share/fonts/truetype/liberation/"

def font(name, size):
    return ImageFont.truetype(FDIR + name, size)

SERIF_B = lambda s: font("LiberationSerif-Bold.ttf", s)
SERIF = lambda s: font("LiberationSerif-Regular.ttf", s)
SANS_B = lambda s: font("LiberationSans-Bold.ttf", s)
SANS = lambda s: font("LiberationSans-Regular.ttf", s)

def wrap(draw, text, fnt, width):
    out = []
    for para in text.split("\n"):
        out.extend(textwrap.wrap(para, width=width) or [""])
    # re-wrap by pixel width
    lines = []
    for raw in out:
        words = raw.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 92], fill=INK)
d.text((24, 12), "THE WORLD TODAY", font=SERIF_B(44), fill=(255, 253, 247))
d.text((24, 62), "MONDAY 23 NOVEMBER 2026  \u00b7  36 STORIES  \u00b7  7 REGIONS",
       font=SANS_B(15), fill=(232, 200, 120))
d.text((W - 24, 16), "ONE DAY.", font=SERIF_B(30), fill=(255, 253, 247), anchor="ra")
d.text((W - 24, 58), "ONE PAGE.", font=SERIF_B(30), fill=(232, 200, 120), anchor="ra")

# ---------- ticker ----------
d.rectangle([0, 92, W, 118], fill=RED)
tick = ("MARKETS  \u00b7  S&P 500 6,910  \u22123.7% Fri  \u00b7  Nasdaq \u22125.3%  \u00b7  VIX 35.9  \u00b7  "
        "Gold $3,515/oz  \u00b7  Bitcoin $61,034  \u00b7  Brent ~$90/bbl  \u00b7  Kospi \u22122.8% Mon")
d.text((24, 99), tick, font=SANS_B(14), fill=(255, 255, 255))

# ---------- lead panel: COP31 ----------
lx, ly, lw, lh = 24, 130, 976, 158
d.rectangle([lx, ly, lx + lw, ly + lh], fill=PAPER, outline=INK, width=2)
d.rectangle([lx, ly, lx + lw, ly + 30], fill=BLUE)
d.text((lx + 12, ly + 6), "LEAD  \u00b7  CLIMATE  \u00b7  ANTALYA, TURKIYE", font=SANS_B(15), fill=(255, 255, 255))
# globe icon
cx, cy, r = lx + 880, ly + 84, 54
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=4)
d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=BLUE, width=2)
d.line([cx - r, cy, cx + r, cy], fill=BLUE, width=2)
d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360, fill=BLUE, width=2)
d.text((cx, cy + r + 8), "COP31", font=SANS_B(13), fill=BLUE, anchor="ma")
d.text((lx + 12, ly + 38), "COP31 COLLAPSES \u2014 NO DEAL", font=SERIF_B(34), fill=INK)
lead_body = ("Nearly 200 nations leave Antalya with no climate deal after the EU rejects a final "
             "text that never mentions fossil fuels \u2014 the first COP to fail since Copenhagen "
             "in 2009. Talks ran two days over, the longest summit on record; a $120bn adaptation "
             "finance target was dropped. Australia's PM calls it a sign of \u2018difficult "
             "geopolitical times\u2019. (AP / NPR / Reuters, 22\u201323 Nov)")
for i, ln in enumerate(wrap(d, lead_body, SANS(15), 800)):
    d.text((lx + 12, ly + 80 + i * 19), ln, font=SANS(15), fill=INK)

# ---------- six story cards ----------
cards = [
    ("WAR & DIPLOMACY", RED, "US presses for Ukraine deal by January",
     "Washington wants a Kyiv\u2013Moscow peace deal by early January, the FT reports. "
     "Trump says Putin \u2018clearly\u2019 wants talks; Russia then hits Kyiv and Lviv, killing 10.",
     "FT / Reuters"),
    ("MIDDLE EAST", BLUE, "Houthis claim strike on Saudi refinery",
     "Yemen's Houthis say they hit the Rabigh oil refinery on Saudi Arabia's Red Sea coast and a "
     "radar site near Riyadh. Riyadh says it intercepted missiles.",
     "Reuters / ISW"),
    ("TECH & MARKETS", GOLD, "Nvidia faces SEC accounting probe",
     "Nvidia falls 14% on Friday, wiping $491bn in a day, after Reuters reports SEC staff are "
     "examining its accounting. Down 23% in a week, worst since 2008.",
     "Reuters / Motley Fool"),
    ("LATIN AMERICA", RED, "\u2018El Chapo Isidro\u2019 captured in Sinaloa",
     "Mexican special forces seize FBI Top Ten fugitive Fausto Isidro Meza Flores in Guasave; "
     "11 die in the raid as cartel gunmen burn trucks.",
     "AP / Reuters"),
    ("ASIA", BLUE, "Candy factory fire: ~50 missing in Java",
     "Seven body bags recovered after fire rips through a candy factory in Cikande, Banten. "
     "About 50 workers unaccounted for; victims need DNA tests to identify.",
     "Reuters / AP"),
    ("ASIA", GOLD, "Seoul minister quits over AI exam cheating",
     "Education minister Choi Kyo-jin resigns after a top scorer confessed to cheating with a "
     "hidden camera and AI. 111 device cases found in the Suneung exam.",
     "Reuters / Guardian"),
]
cw, chh, gap = 318, 120, 10
cx0, cy0 = 24, 300
for i, (tag, col, head, body, src) in enumerate(cards):
    x = cx0 + (i % 3) * (cw + gap)
    y = cy0 + (i // 3) * (chh + gap)
    d.rectangle([x, y, x + cw, y + chh], fill=PAPER, outline=LINE, width=1)
    d.rectangle([x, y, x + cw, y + 22], fill=col)
    d.text((x + 8, y + 4), tag, font=SANS_B(12), fill=(255, 255, 255))
    hl = wrap(d, head, SANS_B(15), cw - 16)
    for j, ln in enumerate(hl[:2]):
        d.text((x + 8, y + 27 + j * 18), ln, font=SANS_B(15), fill=INK)
    bl = wrap(d, body, SANS(11), cw - 16)
    for j, ln in enumerate(bl[:3]):
        d.text((x + 8, y + 27 + len(hl[:2]) * 18 + j * 14), ln, font=SANS(11), fill=(40, 40, 40))
    d.text((x + 8, y + chh - 15), "Source: " + src, font=SANS(9), fill=GREY)

# ---------- briefs ----------
by = cy0 + 2 * chh + gap + 8
d.text((24, by), "MORE FROM AROUND THE WORLD", font=SANS_B(15), fill=INK)
d.line([24, by + 22, W - 24, by + 22], fill=INK, width=2)

briefs = [
    ("EUROPE", "Russian cargo ship still on fire off Finland after an attack, rescuers report."),
    ("EUROPE", "14 people missing after a Russian drone hits a building in the Kyiv region, Zelenskyy says."),
    ("EUROPE", "Poland says three Russian cruise missiles struck on Friday."),
    ("EUROPE", "Thousands march in Lisbon as the rising cost of living fuels anger."),
    ("MIDDLE EAST", "Netanyahu and Eisenkot end talks with no deal on forming an Israel government."),
    ("MIDDLE EAST", "Settler violence in the West Bank is \u2018an act of Jewish terrorism\u2019, a minister says."),
    ("MIDDLE EAST", "Iran strike wounds two in Bahrain; Saudi Arabia condemns \u2018criminal\u2019 attacks."),
    ("MIDDLE EAST", "Saudi-led coalition says it intercepted a Houthi missile in the west."),
    ("AFRICA", "24 civilians killed in fresh violence in South Sudan, officials say."),
    ("AFRICA", "WHO chief pleads for peace in the Ebola-hit area of DR Congo."),
    ("AFRICA", "Drone strikes hit homes and a UN building in Sudan's capital, Khartoum."),
    ("AFRICA", "35 Fulani killed in revenge attacks in Nigeria."),
    ("SOUTH ASIA", "Nepal PM Balendra Shah holds talks with Modi in Delhi on borders, energy and trade."),
    ("SOUTH ASIA", "Tata Sons gears up for a decision this week: go public or stay private."),
    ("SOUTH ASIA", "Amit Shah launches a \u20b94,000-crore infrastructure push in Arunachal Pradesh."),
    ("SOUTH ASIA", "India declare at a record 720/9 in the Wellington Test; NZ 157-4 at lunch, day five."),
    ("OCEANIA", "Australia's PM says the COP31 failure shows \u2018difficult geopolitical times\u2019."),
    ("OCEANIA", "New Zealand retail sales jump 2.2% in the third quarter, beating forecasts."),
    ("OCEANIA", "Australia's manufacturing PMI slips to 48.7 in November."),
    ("EAST ASIA", "South Korea readies a stock stabilisation fund as the Kospi slides 2.8% on Monday."),
    ("EAST ASIA", "North Korea's Kim says his country seeks security, not supremacy."),
    ("N. AMERICA", "Father and daughter detained by ICE at Seattle airport were heading to a baptism, lawyer says."),
    ("N. AMERICA", "US futures rebound in Asia after Friday's rout; gold steadies near $3,577."),
    ("GLOBAL", "Nations agree to keep negotiating lethal AI weapons at a UN conference."),
    ("TECH", "Tech giants form the AAIF to set standards for 100 billion AI agents."),
    ("SPORT", "Liverpool 4-0 Man Utd: Pochettino's nightmare debut; Yoro sent off in the 8th minute."),
    ("SPORT", "Gukesh v Sindarov: Sindarov gets White in Game 1 of the world chess title match, Geneva."),
    ("SPORT", "Anupama defends her IBSF World Women's Snooker Championship title."),
    ("LATIN AM.", "Brazil ex-leader Bolsonaro is \u2018stable\u2019 in intensive care, doctors say."),
]
y = by + 28
for region, text in briefs:
    d.text((24, y), "\u25aa", font=SANS_B(11), fill=RED)
    d.text((40, y), region, font=SANS_B(11), fill=RED)
    d.text((140, y), text, font=SANS(11), fill=INK)
    y += 14

# ---------- footer ----------
fy = H - 22
d.line([24, fy - 4, W - 24, fy - 4], fill=LINE, width=1)
d.text((24, fy), "Sources: AP, Reuters, AFP, NPR, FT, The Hindu, Indian Express, Chess.com. All events of 23 Nov 2026 (or first reported that day).",
       font=SANS(10), fill=GREY)
d.text((W - 24, fy), "THE WORLD TODAY", font=SANS_B(10), fill=GREY, anchor="ra")

img.save("entry.png", format="PNG", optimize=True)
print("saved entry.png", img.size)
