"""Builds the profile's SVGs (header, project cards, toolbox).
Calm palette, serif headings, no glow. They render inside <img>, so no external
fonts or scripts. Run: python3 assets/generate.py"""
from html import escape
import os

OUT = os.path.dirname(os.path.abspath(__file__))

CREAM, CREAM_EDGE = "#f6f1e7", "#e6dccb"
INK, SOFT, FAINT = "#2d3a34", "#5d6862", "#8b918a"
SAGE, CLAY, DUSK, OCHRE = "#8fa98b", "#d08c6b", "#7f97b2", "#c9a45c"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"


def save(name, svg):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)


def header():
    W, H = 1000, 280
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="20"/></clipPath></defs>
<style>
  .n {{ font: 400 54px {SERIF}; fill: {INK}; }}
  .s {{ font: 400 19px {SANS}; fill: {SOFT}; }}
  .k {{ font: 600 12px {SANS}; fill: {FAINT}; letter-spacing: 2.4px; }}
  .drift {{ animation: drift 70s linear infinite; }}
  .drift2 {{ animation: drift 95s linear infinite; animation-delay: -40s; }}
  @keyframes drift {{ from {{ transform: translateX(-260px); }} to {{ transform: translateX({W + 60}px); }} }}
</style>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="{CREAM}"/>
  <circle cx="790" cy="118" r="54" fill="{CLAY}" opacity=".55"/>
  <g class="drift" fill="#ffffff" opacity=".85">
    <ellipse cx="60" cy="70" rx="58" ry="14"/><ellipse cx="95" cy="60" rx="34" ry="14"/>
  </g>
  <g class="drift2" fill="#ffffff" opacity=".7">
    <ellipse cx="60" cy="126" rx="44" ry="11"/><ellipse cx="84" cy="118" rx="24" ry="10"/>
  </g>
  <path d="M520 280 C600 170 700 150 790 190 C860 220 930 160 1000 150 L1000 280Z" fill="#d9e0cf"/>
  <path d="M430 280 C560 200 640 230 740 215 C830 202 900 240 1000 205 L1000 280Z" fill="#bccaae"/>
  <path d="M600 280 C700 245 780 262 860 250 C920 242 960 255 1000 250 L1000 280Z" fill="{SAGE}"/>
  <text x="64" y="92" class="k">FULL-STACK ENGINEER · MUMBAI</text>
  <text x="62" y="158" class="n">Nikhil Patil</text>
  <rect x="64" y="182" width="48" height="3" rx="1.5" fill="{SAGE}"/>
  <text x="64" y="224" class="s">I build AI products that hold up after the demo.</text>
</g>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="{CREAM_EDGE}"/>
</svg>'''


def card(key, initial, accent, title, desc, tags):
    W, H = 490, 196
    lines = "".join(f'<text x="28" y="{112 + i * 22}" class="d">{escape(l)}</text>' for i, l in enumerate(desc))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .t {{ font: 400 24px {SERIF}; fill: {INK}; }}
  .i {{ font: 400 22px {SERIF}; fill: #ffffff; }}
  .d {{ font: 400 15px {SANS}; fill: {SOFT}; }}
  .g {{ font: 600 11px {SANS}; fill: {FAINT}; letter-spacing: 1.6px; }}
  .a {{ font: 400 20px {SANS}; fill: {FAINT}; }}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="18" fill="{CREAM}" stroke="{CREAM_EDGE}"/>
<rect x="28" y="28" width="42" height="42" rx="12" fill="{accent}"/>
<text x="49" y="57" text-anchor="middle" class="i">{escape(initial)}</text>
<text x="86" y="58" class="t">{escape(title)}</text>
{lines}
<text x="28" y="172" class="g">{escape("  ·  ".join(t.upper() for t in tags))}</text>
<text x="{W - 32}" y="58" text-anchor="end" class="a">→</text>
</svg>'''


def toolbox():
    W = 1000
    rows = [
        ("BUILD", ["TypeScript", "Next.js", "React", "Node", "Python"], SAGE),
        ("DATA", ["Postgres", "Supabase", "MongoDB", "Redis", "pgvector"], DUSK),
        ("AI", ["Claude", "GPT", "Gemini", "Firecrawl", "Agents"], CLAY),
    ]
    out, y = [], 58
    for label, items, color in rows:
        out.append(f'<circle cx="40" cy="{y - 5}" r="5" fill="{color}"/><text x="56" y="{y}" class="k">{label}</text>')
        x = 150
        for it in items:
            w = len(it) * 8.2 + 30
            out.append(
                f'<rect x="{x:.0f}" y="{y - 21}" width="{w:.0f}" height="32" rx="16" fill="#ffffff" stroke="{CREAM_EDGE}"/>'
                f'<text x="{x + w / 2:.0f}" y="{y}" text-anchor="middle" class="c">{escape(it)}</text>'
            )
            x += w + 10
        y += 50
    H = y - 14
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .k {{ font: 600 12px {SANS}; fill: {FAINT}; letter-spacing: 2px; }}
  .c {{ font: 500 14px {SANS}; fill: {INK}; }}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{CREAM}" stroke="{CREAM_EDGE}"/>
{"".join(out)}
</svg>'''


save("header.svg", header())
save("toolbox.svg", toolbox())
CARDS = [
    ("support", "S", SAGE, "Support Agent", ["A shopping and support assistant for one brand.", "Finds products, checks orders, lives in a chat bubble."], ["TypeScript", "LLMs", "Shopify"]),
    ("firecrawl", "F", CLAY, "Firecrawl Agent", ["Visits a store it has never seen, works out", "how it works and places the order."], ["Next.js", "Firecrawl", "Agents"]),
    ("meetai", "M", DUSK, "MeetAI", ["Video meetings with live transcripts", "and a summary waiting when you hang up."], ["Next.js", "TypeScript", "AI"]),
    ("eduquest", "E", OCHRE, "EduQuest", ["Learning, turned into a Pokémon-style game", "so practice feels like playing."], ["React", "JavaScript"]),
]
for key, *rest in CARDS:
    save(f"card-{key}.svg", card(key, *rest))
print("ok")
