"""
Socialeap GmbH — Instagram Carousel
Post: "5 SEO-Fehler die deine Website unsichtbar machen"
Format: 1080x1350 px | 7 Slides
Datum: 14.04.2026 | Säule: Expertise
"""

from PIL import Image, ImageDraw, ImageFont
import os, textwrap

# ── Paths ──────────────────────────────────────────────────────────────────────
FONT_DIR = "/root/fonts"
OUT_DIR  = os.path.dirname(os.path.abspath(__file__))

# ── Canvas ─────────────────────────────────────────────────────────────────────
W, H = 1080, 1350

# ── Brand Colors ───────────────────────────────────────────────────────────────
BG          = (10,  10,  14)      # Midnight Black #0A0A0E
WHITE       = (245, 245, 247)     # Off-White      #F5F5F7
BLUE        = (82,  200, 245)     # Sky Blue       #52C8F5
ORANGE      = (245, 160, 40)      # Amber          #F5A028
MAGENTA     = (230, 50,  100)     # Magenta        #E63264
DARK_CARD   = (18,  18,  24)      # slightly lighter BG for cards
LINE_GRAY   = (45,  45,  55)      # subtle separator

# ── Fonts ──────────────────────────────────────────────────────────────────────
def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}.ttf", size)

SORA_XB  = lambda s: font("Sora-ExtraBold",         s)
SORA_B   = lambda s: font("Sora-Bold",               s)
SORA_R   = lambda s: font("Sora-Regular",            s)
JAK_M    = lambda s: font("PlusJakartaSans-Medium",  s)
JAK_B    = lambda s: font("PlusJakartaSans-Bold",    s)
JAK_R    = lambda s: font("PlusJakartaSans-Regular", s)

# ── Helpers ────────────────────────────────────────────────────────────────────
def new_canvas():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)

def draw_text_centered(draw, text, font, y, color=WHITE, max_width=W-120):
    """Draw centered text, auto-wrapping at max_width."""
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        bb = draw.textbbox((0, 0), test, font=font)
        if bb[2] - bb[0] > max_width and line:
            lines.append(" ".join(line))
            line = [w]
        else:
            line.append(w)
    if line:
        lines.append(" ".join(line))
    for ln in lines:
        bb = draw.textbbox((0, 0), ln, font=font)
        x = (W - (bb[2] - bb[0])) // 2
        draw.text((x, y), ln, font=font, fill=color)
        y += (bb[3] - bb[1]) + 12
    return y

def draw_text_left(draw, text, font, x, y, color=WHITE, max_width=W-120):
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        bb = draw.textbbox((0, 0), test, font=font)
        if bb[2] - bb[0] > max_width and line:
            lines.append(" ".join(line))
            line = [w]
        else:
            line.append(w)
    if line:
        lines.append(" ".join(line))
    for ln in lines:
        bb = draw.textbbox((0, 0), ln, font=font)
        draw.text((x, y), ln, font=font, fill=color)
        y += (bb[3] - bb[1]) + 10
    return y

def draw_logo(draw, img):
    """Socialeap wordmark bottom-right, small."""
    lbl = "socialeap."
    fnt = SORA_B(28)
    bb  = draw.textbbox((0,0), lbl, font=fnt)
    tw  = bb[2] - bb[0]
    x   = W - tw - 48
    y   = H - 64
    # Draw "socialeap" in white, "." in orange
    draw.text((x, y), "socialeap", font=fnt, fill=WHITE)
    bb2 = draw.textbbox((0,0), "socialeap", font=fnt)
    draw.text((x + bb2[2]-bb2[0], y), ".", font=fnt, fill=ORANGE)

def draw_slide_number(draw, current, total):
    """Small slide counter top-right."""
    txt = f"{current}/{total}"
    fnt = JAK_M(26)
    bb  = draw.textbbox((0,0), txt, font=fnt)
    x   = W - (bb[2]-bb[0]) - 48
    draw.text((x, 48), txt, font=fnt, fill=(80, 80, 90))

def draw_accent_line(draw, y, color=BLUE, width=60, x=60):
    draw.rectangle([x, y, x+width, y+4], fill=color)

def draw_top_bar(draw):
    """Thin top accent line full width."""
    draw.rectangle([0, 0, W, 5], fill=BLUE)

# ── SLIDE 1 — Cover ────────────────────────────────────────────────────────────
def slide_01():
    img, draw = new_canvas()
    draw_top_bar(draw)

    # Subtle background grid pattern (decorative dots)
    for gx in range(60, W, 80):
        for gy in range(60, H, 80):
            draw.ellipse([gx-1, gy-1, gx+1, gy+1], fill=(30, 30, 40))

    # Number badge
    badge_y = 180
    draw.ellipse([W//2-55, badge_y-55, W//2+55, badge_y+55], fill=BLUE)
    num_fnt = SORA_XB(48)
    nb = draw.textbbox((0,0), "5", font=num_fnt)
    draw.text((W//2 - (nb[2]-nb[0])//2, badge_y - (nb[3]-nb[1])//2), "5", font=num_fnt, fill=BG)

    # Main headline
    y = badge_y + 95
    draw_accent_line(draw, y, BLUE, 50, W//2-25)
    y += 24

    line1_fnt = SORA_XB(94)
    line2_fnt = SORA_XB(94)
    line3_fnt = SORA_B(52)

    y = draw_text_centered(draw, "SEO-FEHLER",   line1_fnt, y+10,  WHITE)
    y = draw_text_centered(draw, "die deine",    line3_fnt, y+8,   (160, 160, 175))
    y = draw_text_centered(draw, "Website",      line1_fnt, y+8,   BLUE)
    y = draw_text_centered(draw, "unsichtbar",   line2_fnt, y+8,   WHITE)
    y = draw_text_centered(draw, "machen.",      line2_fnt, y+4,   ORANGE)

    # Subtext
    y += 40
    sub_fnt = JAK_M(32)
    draw_text_centered(draw, "Und wie du sie behebst.", sub_fnt, y, (140, 140, 160))

    # Swipe hint
    sw_fnt = JAK_R(26)
    sw_txt = "→ Swipe für alle 5 Fehler"
    bb = draw.textbbox((0,0), sw_txt, font=sw_fnt)
    draw.text(((W-(bb[2]-bb[0]))//2, H-160), sw_txt, font=sw_fnt, fill=(80, 80, 95))

    draw_logo(draw, img)
    return img

# ── SLIDE 2–6 — Content Slides ─────────────────────────────────────────────────
FEHLER = [
    {
        "num": "01",
        "title": "Fehlende oder falsche\nMeta-Titles",
        "body": (
            "Der Title-Tag ist das Erste, was Google und Nutzer sehen. "
            "Zu lang, zu kurz oder fehlend — und deine Seite verliert sofort Ranking-Potenzial."
        ),
        "fix": "Jede Seite braucht einen einzigartigen Title-Tag mit Haupt-Keyword (50–60 Zeichen).",
        "color": BLUE,
    },
    {
        "num": "02",
        "title": "Zu langsame\nLadezeit",
        "body": (
            "Google misst Core Web Vitals. Lädt deine Website länger als 3 Sekunden, "
            "verlierst du bis zu 53 % deiner Besucher — bevor die Seite überhaupt erscheint."
        ),
        "fix": "Bilder komprimieren, unnötige Plugins entfernen, Server-Caching aktivieren.",
        "color": ORANGE,
    },
    {
        "num": "03",
        "title": "Keine oder schwache\ninterne Verlinkung",
        "body": (
            "Interne Links verteilen \"Link Juice\" und helfen Google, deine wichtigsten Seiten zu finden. "
            "Ohne sie stehen viele deiner Seiten im Dunkeln."
        ),
        "fix": "Verlinke relevante Unterseiten konsequent — besonders aus Blog-Artikeln.",
        "color": MAGENTA,
    },
    {
        "num": "04",
        "title": "Fehlende\nMobil-Optimierung",
        "body": (
            "Über 60 % der Google-Suchen kommen vom Smartphone. "
            "Google indexiert deine Website primär nach der mobilen Version — nicht der Desktop-Version."
        ),
        "fix": "Responsive Design ist Pflicht. Teste mit Google's Mobile-Friendly Test.",
        "color": BLUE,
    },
    {
        "num": "05",
        "title": "Kein konkretes\nKeyword-Targeting",
        "body": (
            "\"Webdesign Agentur\" zu targeten reicht nicht. "
            "Du brauchst spezifische Long-Tail-Keywords die deine Zielgruppe tatsächlich sucht."
        ),
        "fix": "Keyword-Recherche mit konkreten Suchvolumen — dann Seiten gezielt optimieren.",
        "color": ORANGE,
    },
]

def slide_content(data, slide_num, total=7):
    img, draw = new_canvas()
    draw_top_bar(draw)
    draw_slide_number(draw, slide_num, total)

    accent = data["color"]
    num    = data["num"]
    title  = data["title"]
    body   = data["body"]
    fix    = data["fix"]

    # Large number
    num_fnt = SORA_XB(160)
    nb = draw.textbbox((0,0), num, font=num_fnt)
    draw.text((54, 60), num, font=num_fnt, fill=accent)

    # Title
    title_fnt = SORA_XB(64)
    title_y   = 60 + (nb[3]-nb[1]) + 20
    for line in title.split("\n"):
        bb = draw.textbbox((0,0), line, font=title_fnt)
        draw.text((54, title_y), line, font=title_fnt, fill=WHITE)
        title_y += (bb[3]-bb[1]) + 8

    # Separator
    title_y += 20
    draw.rectangle([54, title_y, 54+440, title_y+3], fill=accent)
    title_y += 28

    # Body text
    body_fnt = JAK_M(34)
    body_y   = draw_text_left(draw, body, body_fnt, 54, title_y, (200, 200, 215), W-108)
    body_y  += 48

    # Fix card
    card_pad = 40
    card_h   = 180
    draw.rounded_rectangle(
        [54, body_y, W-54, body_y+card_h],
        radius=18,
        fill=DARK_CARD,
        outline=accent,
        width=2
    )
    # "Fix:" label
    fix_label_fnt = JAK_B(28)
    draw.text((54+card_pad, body_y+28), "✓  Fix:", font=fix_label_fnt, fill=accent)
    fix_fnt = JAK_M(28)
    draw_text_left(draw, fix, fix_fnt, 54+card_pad, body_y+28+42, WHITE, W-108-card_pad*2-8)

    draw_logo(draw, img)
    return img

# ── SLIDE 7 — CTA ──────────────────────────────────────────────────────────────
def slide_cta():
    img, draw = new_canvas()
    draw_top_bar(draw)

    # Background accent
    draw.ellipse([-200, -200, 600, 600], fill=(15, 35, 50))

    y = 180
    # Icon area
    draw.ellipse([W//2-60, y-60, W//2+60, y+60], fill=BLUE)
    chk_fnt = SORA_XB(52)
    cb = draw.textbbox((0,0), "✓", font=chk_fnt)
    draw.text((W//2-(cb[2]-cb[0])//2, y-(cb[3]-cb[1])//2), "✓", font=chk_fnt, fill=BG)

    y += 100
    draw_text_centered(draw, "Deine Website", SORA_XB(72),  y,    WHITE)
    y += 90
    draw_text_centered(draw, "checken?",      SORA_XB(72),  y,    BLUE)
    y += 90

    draw.rectangle([W//2-30, y, W//2+30, y+4], fill=LINE_GRAY)
    y += 36

    body_lines = [
        "Wir schauen kostenlos,",
        "welche dieser Fehler bei dir vorliegen.",
    ]
    for ln in body_lines:
        draw_text_centered(draw, ln, JAK_M(36), y, (180, 180, 200))
        y += 52

    y += 30

    # CTA Button
    btn_w, btn_h = 620, 90
    btn_x = (W - btn_w) // 2
    draw.rounded_rectangle(
        [btn_x, y, btn_x+btn_w, y+btn_h],
        radius=45,
        fill=BLUE
    )
    btn_fnt = JAK_B(34)
    btn_txt = "Kostenloses Erstgespräch →"
    bb = draw.textbbox((0,0), btn_txt, font=btn_fnt)
    draw.text(
        (btn_x + (btn_w-(bb[2]-bb[0]))//2, y + (btn_h-(bb[3]-bb[1]))//2),
        btn_txt, font=btn_fnt, fill=BG
    )
    y += btn_h + 28

    draw_text_centered(draw, "Link in Bio", JAK_R(30), y, (120, 120, 135))
    y += 52

    # Save hint
    save_fnt = JAK_R(27)
    draw_text_centered(draw, "💾  Speicher diesen Post für später.", save_fnt, y, (100, 100, 115))

    draw_logo(draw, img)
    return img

# ── Generate all slides ─────────────────────────────────────────────────────────
def main():
    slides = [
        ("Slide_01_Cover.png",  slide_01()),
    ]
    for i, data in enumerate(FEHLER, start=2):
        slides.append((f"Slide_0{i}_Fehler{data['num']}.png", slide_content(data, i)))
    slides.append(("Slide_07_CTA.png", slide_cta()))

    for filename, img in slides:
        path = os.path.join(OUT_DIR, filename)
        img.save(path, "PNG", dpi=(300, 300))
        print(f"  ✓  Gespeichert: {filename}  ({img.size[0]}×{img.size[1]}px)")

    print(f"\nAlle {len(slides)} Slides in:\n  {OUT_DIR}")

if __name__ == "__main__":
    main()
