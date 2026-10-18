"""Generates the animated SVGs for the GitHub profile README (assets/*.svg).
SVGs render inside <img>, so: no external fonts/scripts, CSS + SMIL animation only."""
from html import escape
import os

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
BLUE, PURPLE, PINK, GREEN, AMBER = "#7aa2f7", "#bb9af7", "#f7768e", "#9ece6a", "#e0af68"
BG, PANEL, FG, MUTED = "#0b0f1d", "#111628", "#e6e9f5", "#8b93b8"


def write(name, svg):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)


# ── hero ────────────────────────────────────────────────────────────────
def hero():
    W, H = 1000, 300
    chips = ["AI agents", "LLM pipelines", "AI search", "Next.js", "TypeScript", "Supabase"]
    chip_svg, x = [], 0
    widths = [len(c) * 8.6 + 34 for c in chips]
    total = sum(widths) + 10 * (len(chips) - 1)
    x = (W - total) / 2
    for i, (c, w) in enumerate(zip(chips, widths)):
        chip_svg.append(
            f'<g class="chip" style="animation-delay:{1.1 + i * 0.15:.2f}s">'
            f'<rect x="{x:.1f}" y="222" width="{w:.1f}" height="30" rx="15" fill="#ffffff0d" stroke="#ffffff26"/>'
            f'<text x="{x + w / 2:.1f}" y="242" text-anchor="middle" class="chipt">{escape(c)}</text></g>'
        )
        x += w + 10
    dots = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="1" fill="#ffffff14"/>'
        for cx in range(20, W, 40) for cy in range(20, H, 40)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="name" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0" stop-color="{BLUE}"/><stop offset="0.5" stop-color="{PURPLE}"/><stop offset="1" stop-color="{PINK}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-0.5 0;0.5 0;-0.5 0" dur="8s" repeatCount="indefinite"/>
  </linearGradient>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<style>
  .t1 {{ font: 800 64px {SANS}; letter-spacing: -1px; }}
  .t2 {{ font: 500 20px {SANS}; fill: {MUTED}; }}
  .chipt {{ font: 600 14px {SANS}; fill: {FG}; }}
  .stat {{ font: 600 13px {MONO}; fill: {GREEN}; }}
  .fade {{ opacity: 0; animation: up .9s ease-out forwards; }}
  .chip {{ opacity: 0; animation: up .6s ease-out forwards; }}
  @keyframes up {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
  .pulse {{ animation: pulse 1.6s ease-in-out infinite; transform-origin: 383px 54px; }}
  @keyframes pulse {{ 0%,100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: .35; transform: scale(1.8); }} }}
</style>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  {dots}
  <g filter="url(#blur)" opacity="0.55">
    <circle r="120" fill="{BLUE}"><animateMotion dur="18s" repeatCount="indefinite" path="M180,80 C380,10 300,260 120,220 S-20,120 180,80Z"/></circle>
    <circle r="110" fill="{PURPLE}"><animateMotion dur="22s" repeatCount="indefinite" path="M820,90 C980,180 700,300 620,170 S700,20 820,90Z"/></circle>
    <circle r="90" fill="{PINK}"><animateMotion dur="26s" repeatCount="indefinite" path="M520,250 C620,330 420,330 400,250 S470,180 520,250Z"/></circle>
  </g>
  <g class="fade" style="animation-delay:.1s">
    <rect x="370" y="40" width="260" height="28" rx="14" fill="#9ece6a1a" stroke="#9ece6a55"/>
    <circle cx="383" cy="54" r="4" fill="{GREEN}" class="pulse"/><circle cx="383" cy="54" r="4" fill="{GREEN}"/>
    <text x="395" y="59" class="stat">currently building AI agents</text>
  </g>
  <text x="{W / 2}" y="140" text-anchor="middle" class="t1 fade" fill="url(#name)" style="animation-delay:.35s">Nikhil Patil</text>
  <text x="{W / 2}" y="182" text-anchor="middle" class="t2 fade" style="animation-delay:.7s">Full-stack engineer turning LLMs into products people actually use · Mumbai</text>
  {"".join(chip_svg)}
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#ffffff1f"/>
</svg>'''


# ── terminal ────────────────────────────────────────────────────────────
def terminal():
    W, LH, TOP = 1000, 26, 70
    lines = [
        ("$ ", BLUE, 'agent run "wireless headphones under ₹3,000, delivered this week"', FG),
        ("→ ", PURPLE, "visiting store … reading /llms.txt", MUTED),
        ("✓ ", GREEN, "found storefront API · searching catalog", FG),
        ("→ ", PURPLE, "12 products matched · comparing price, reviews, delivery", MUTED),
        ("✓ ", GREEN, "best match: 4.6★ · ₹2,899 · arrives Thursday", FG),
        ("→ ", PURPLE, "creating order … payment link ready", MUTED),
        ("✓ ", GREEN, "done in 9.4s · 6 tool calls · 0 humans needed", GREEN),
        ("$ ", BLUE, "whoami", FG),
        ("", FG, "nikhil — I build agents like this one, end to end.", AMBER),
    ]
    H = TOP + LH * len(lines) + 30
    CYCLE = 16.0
    css, rows = [], []
    t = 0.6
    for i, (pre, pc, text, tc) in enumerate(lines):
        typing = 0.6 + len(text) * 0.022 if pre == "$ " else 0.35
        a = t / CYCLE * 100
        b = (t + typing) / CYCLE * 100
        css.append(
            f"@keyframes l{i} {{ 0%,{a:.2f}% {{ clip-path: inset(0 100% 0 0); opacity:1 }} "
            f"{b:.2f}%,90% {{ clip-path: inset(0 0 0 0); opacity:1 }} 96%,100% {{ clip-path: inset(0 0 0 0); opacity:0 }} }}"
            f" .l{i} {{ animation: l{i} {CYCLE}s linear infinite; }}"
        )
        y = TOP + i * LH
        rows.append(
            f'<g class="l{i}"><text x="28" y="{y}" class="m"><tspan fill="{pc}">{escape(pre)}</tspan>'
            f'<tspan fill="{tc}">{escape(text)}</tspan></text></g>'
        )
        t += typing + (0.5 if pre == "$ " else 0.45)
    cy = TOP + (len(lines) - 1) * LH
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .m {{ font: 500 15px {MONO}; }}
  .title {{ font: 600 13px {SANS}; fill: {MUTED}; }}
  {" ".join(css)}
  .cur {{ animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
</style>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="{PANEL}" stroke="#ffffff1f"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="38" rx="14" fill="#ffffff08"/>
<circle cx="24" cy="20" r="6" fill="#f7768e"/><circle cx="44" cy="20" r="6" fill="#e0af68"/><circle cx="64" cy="20" r="6" fill="#9ece6a"/>
<text x="{W / 2}" y="25" text-anchor="middle" class="title">shopping-agent — live run</text>
{"".join(rows)}
<rect x="28" y="{cy + 12}" width="9" height="3" fill="{BLUE}" class="cur"/>
</svg>'''


# ── project cards ───────────────────────────────────────────────────────
def card(key, emoji, title, lines, chips, accent, live):
    W, H = 490, 190
    chip_svg, x = [], 24
    for c in chips:
        w = len(c) * 7.4 + 22
        chip_svg.append(
            f'<rect x="{x:.1f}" y="146" width="{w:.1f}" height="24" rx="12" fill="#ffffff0d" stroke="#ffffff22"/>'
            f'<text x="{x + w / 2:.1f}" y="162" text-anchor="middle" class="chip">{escape(c)}</text>'
        )
        x += w + 8
    body = "".join(f'<text x="24" y="{98 + i * 22}" class="d">{escape(l)}</text>' for i, l in enumerate(lines))
    live_svg = (
        f'<rect x="{W - 78}" y="22" width="56" height="24" rx="12" fill="{accent}22" stroke="{accent}77"/>'
        f'<text x="{W - 50}" y="38" text-anchor="middle" class="live" fill="{accent}">live ↗</text>'
        if live else ""
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="b{key}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="{H}">
    <stop offset="0" stop-color="{accent}"/><stop offset="0.5" stop-color="#ffffff10"/><stop offset="1" stop-color="{accent}"/>
    <animateTransform attributeName="gradientTransform" type="rotate" values="0 {W / 2} {H / 2};360 {W / 2} {H / 2}" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <radialGradient id="g{key}" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(40 30) scale(260)">
    <stop offset="0" stop-color="{accent}" stop-opacity=".22"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
</defs>
<style>
  .h {{ font: 700 22px {SANS}; fill: {FG}; }}
  .d {{ font: 400 15px {SANS}; fill: {MUTED}; }}
  .chip {{ font: 600 12px {MONO}; fill: {FG}; }}
  .live {{ font: 700 12px {SANS}; }}
  .e {{ font: 26px {SANS}; }}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{PANEL}"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="url(#g{key})"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="url(#b{key})" stroke-width="2"/>
<text x="24" y="54" class="e">{emoji}</text>
<text x="64" y="52" class="h">{escape(title)}</text>
{live_svg}
{body}
{"".join(chip_svg)}
</svg>'''


write("hero.svg", hero())
write("terminal.svg", terminal())
CARDS = [
    ("support", "🛍️", "Support Agent", ["AI shopping + support assistant for a brand:", "semantic search over Shopify, order tracking."], ["TypeScript", "LLMs", "Shopify"], BLUE, False),
    ("firecrawl", "🕷️", "Firecrawl Agent", ["Visits any online store, works out how it's", "built, finds the product and places the order."], ["Next.js", "Firecrawl", "Agents"], PURPLE, False),
    ("meetai", "🎙️", "MeetAI", ["Online meetings with live transcription", "and automatic AI summaries."], ["Next.js", "TypeScript", "AI"], PINK, True),
    ("eduquest", "🎮", "EduQuest", ["Pokémon-inspired gamified learning that", "makes studying feel like an adventure."], ["React", "JavaScript", "Game"], GREEN, False),
]
for c in CARDS:
    write(f"card-{c[0]}.svg", card(*c))
print("ok", sorted(os.listdir(OUT)))
