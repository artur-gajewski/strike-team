#!/usr/bin/env python3
"""Generate Kill Team-style character card PDF for Strike Team game."""

from weasyprint import HTML, CSS

# ── DATA ─────────────────────────────────────────────────────────────────────

TEAMS = [
    {
        "name": "CRIMSON TALONS VANGUARD",
        "faction_color": "#C0392B",
        "faction_accent": "#E74C3C",
        "faction_light": "#FFFFFF",
        "header_text": "#FFFFFF",
        "operants": [
            {
                "name": "Mara Voss", "number": 1,
                "callsign": "IRONCLAD",
                "role": "Sergeant · Squad Leader",
                "mov": '6"', "hp": 20, "ac": 16, "per": "+4",
                "ranged": [
                    {"name": "Combat Rifle",  "range": '24"', "atk": "+5", "dmg": "1d8+2",  "special": "—"},
                    {"name": "Heavy Sidearm", "range": '12"', "atk": "+5", "dmg": "1d6+2",  "special": "Bonus action after moving"},
                ],
                "melee": {"name": "Tactical Blade", "atk": "+6", "dmg": "1d6+3", "special": "18–20: target Staggered (–2 AC)"},
                "ability_name": "Rally the Line",
                "ability": "Once per game: all friendlies within 8\" remove 1 condition (Staggered, Pinned, or Shaken).",
            },
            {
                "name": "Dayo Fen", "number": 2,
                "callsign": "PHANTOM",
                "role": "Scout · Sniper",
                "mov": '8"', "hp": 12, "ac": 13, "per": "+8",
                "ranged": [
                    {"name": "Marksman Rifle", "range": '36"', "atk": "+7", "dmg": "1d10+3", "special": "Ignore cover AC beyond 12\""},
                    {"name": "Compact Pistol", "range": '10"', "atk": "+5", "dmg": "1d6+1",  "special": "—"},
                ],
                "melee": {"name": "Serrated Blade", "atk": "+5", "dmg": "1d4+3", "special": "Unaware target: +1d6 damage"},
                "ability_name": "Overwatch Eye",
                "ability": "If Phantom doesn't move, place 1 Overwatch token. Next enemy within 24\" LoS triggers a free Marksman Rifle attack.",
            },
            {
                "name": "Bram Holst", "number": 3,
                "callsign": "IRONKEG",
                "role": "Specialist · Demolitions",
                "mov": '5"', "hp": 22, "ac": 17, "per": "+2",
                "ranged": [
                    {"name": "Grenade Launcher", "range": '20"', "atk": "+4", "dmg": "2d6",   "special": "Blast 3\" — AC 14 save or hit"},
                    {"name": "Heavy Pistol",     "range": '12"', "atk": "+4", "dmg": "1d8+1", "special": "—"},
                ],
                "melee": {"name": "Breaching Axe", "atk": "+5", "dmg": "1d8+2", "special": "Ignores cover AC bonus"},
                "ability_name": "Frag Pack",
                "ability": "Once per game: plant a charge on terrain. Triggers on entry within 2\" (3d6, Blast 4\") or detonate on Ironkeg's activation.",
            },
            {
                "name": "Sera Okafor", "number": 4,
                "callsign": "STITCH",
                "role": "Specialist · Combat Medic",
                "mov": '6"', "hp": 14, "ac": 14, "per": "+3",
                "ranged": [
                    {"name": "Assault Carbine",   "range": '22"', "atk": "+4", "dmg": "1d8+1", "special": "—"},
                    {"name": "Medshot Injector",  "range": '8"',  "atk": "+4", "dmg": "1d6+2", "special": "Heals friendly target instead of damage"},
                ],
                "melee": {"name": "Shock Baton", "atk": "+4", "dmg": "1d6+1", "special": "DC 13 CON save or Stunned"},
                "ability_name": "Trauma Response",
                "ability": "Once per game: when a friendly within 6\" is downed, Stitch moves up to 4\" and restores them to 4 HP.",
            },
            {
                "name": "Tanek Rall", "number": 5,
                "callsign": "HURRICANE",
                "role": "Specialist · Close Assault",
                "mov": '6"', "hp": 16, "ac": 15, "per": "+2",
                "ranged": [
                    {"name": "Combat Shotgun",  "range": '12"', "atk": "+6", "dmg": "2d6",   "special": "≤6\": +1d4 dmg. >12\": –2 to hit"},
                    {"name": "Submachine Gun",  "range": '18"', "atk": "+5", "dmg": "1d6+2", "special": "Burst: –2 to hit, roll dmg twice (take higher)"},
                ],
                "melee": {"name": "Chainblade", "atk": "+6", "dmg": "1d8+3", "special": "Rend: –1 AC on target (max –3, permanent)"},
                "ability_name": "Charge!",
                "ability": "Move ≥4\" straight toward target before melee: +1d6 damage and push target back 2\".",
            },
        ],
    },
    {
        "name": "ASHBORN SYNDICATE STRIKE CELL",
        "faction_color": "#1A4A8A",
        "faction_accent": "#2563b0",
        "faction_light": "#FFFFFF",
        "header_text": "#FFFFFF",
        "operants": [
            {
                "name": "Rho Draven", "number": 1,
                "callsign": "SABLE",
                "role": "Sergeant · Mercenary Commander",
                "mov": '6"', "hp": 20, "ac": 15, "per": "+3",
                "ranged": [
                    {"name": "Mag-Rail Carbine", "range": '26"', "atk": "+5", "dmg": "1d8+2", "special": "Ignores 1 pt heavy armour AC bonus"},
                    {"name": "Scatter Pistol",   "range": '10"', "atk": "+5", "dmg": "1d6+2", "special": "Hits all in 2\" cone from target"},
                ],
                "melee": {"name": "Vibro-Blade", "atk": "+6", "dmg": "1d6+3", "special": "Reroll one damage die per attack (take higher)"},
                "ability_name": "Calculated Strike",
                "ability": "Once per game: designate a Priority Target. All friendlies gain +2 to attack that target until it is downed.",
            },
            {
                "name": "Lyss Null", "number": 2,
                "callsign": "WHISPER",
                "role": "Scout · Infiltrator",
                "mov": '8"', "hp": 11, "ac": 12, "per": "+7",
                "ranged": [
                    {"name": "Silenced Long Rifle", "range": '32"', "atk": "+6", "dmg": "1d10+2", "special": "Firing does not reveal Whisper's position"},
                    {"name": "Dart Pistol",         "range": '12"', "atk": "+5", "dmg": "1d4+2",  "special": "Poison: 1d4 damage at start of target's next turn"},
                ],
                "melee": {"name": "Monofilament Wire", "atk": "+5", "dmg": "1d4+3", "special": "Unaware target: +1d6 damage"},
                "ability_name": "Ghost Protocol",
                "ability": "Once per round: spend full activation to become Concealed — enemies cannot voluntarily target Whisper until they move or attack.",
            },
            {
                "name": "Grast Molen", "number": 3,
                "callsign": "VAULT",
                "role": "Specialist · Heavy Support",
                "mov": '4"', "hp": 24, "ac": 18, "per": "+1",
                "ranged": [
                    {"name": "Rotary Cannon", "range": '20"', "atk": "+4", "dmg": "1d10+1", "special": "Stationary: +1 to hit, DC 13 save or target Pinned"},
                    {"name": "Flamer",        "range": '8"',  "atk": "+4", "dmg": "2d4",    "special": "Burning: 1d4 fire dmg at start of target's next turn"},
                ],
                "melee": {"name": "Reinforced Fist", "atk": "+5", "dmg": "1d8+2", "special": "Knockback: push target 2\" on hit"},
                "ability_name": "Iron Bastion",
                "ability": "While stationary: friendlies within 3\" may use Vault's AC against ranged attacks — Vault absorbs the hit.",
            },
            {
                "name": "Sixx Prenn", "number": 4,
                "callsign": "ARC",
                "role": "Specialist · Tech Operative",
                "mov": '6"', "hp": 13, "ac": 14, "per": "+4",
                "ranged": [
                    {"name": "Shock Rifle",  "range": '22"', "atk": "+4", "dmg": "1d8",   "special": "EMP Burst: target Disrupted (–2 to next attack)"},
                    {"name": "Sentry Drone", "range": '24"', "atk": "+5", "dmg": "1d6+1", "special": "Deploy free; attacks each round (HP 4, AC 11)"},
                ],
                "melee": {"name": "Shock Baton", "atk": "+4", "dmg": "1d6+1", "special": "DC 13 CON save or Stunned"},
                "ability_name": "System Override",
                "ability": "Once per game: skip movement this activation — one enemy within 18\" LoS loses their Special Ability for the rest of the game.",
            },
            {
                "name": "Vael Hurst", "number": 5,
                "callsign": "JACKAL",
                "role": "Specialist · Tracker",
                "mov": '7"', "hp": 16, "ac": 14, "per": "+5",
                "ranged": [
                    {"name": "Hunting Rifle", "range": '30"', "atk": "+6", "dmg": "1d10+1", "special": "Marked: +2 to hit that target for rest of game"},
                    {"name": "Revolver",      "range": '14"', "atk": "+5", "dmg": "1d8+1",  "special": "Fan the Hammer: fire twice at –2 to hit each"},
                ],
                "melee": {"name": "Hunting Blade", "atk": "+6", "dmg": "1d8+2", "special": "vs Marked target: +1d6 damage"},
                "ability_name": "Never Lose the Trail",
                "ability": "Moving toward a Marked target ignores Overwatch. If Marked target disengages, Jackal makes a free melee reaction attack.",
            },
        ],
    },
]

# ── HTML TEMPLATE ─────────────────────────────────────────────────────────────

def weapon_rows(weapons):
    rows = ""
    for i, w in enumerate(weapons):
        row_class = "row-alt" if i % 2 == 1 else ""
        rows += f"""
        <tr class="{row_class}">
            <td class="w-name">{w['name']}</td>
            <td class="w-center">{w.get('range', '—')}</td>
            <td class="w-center">{w['atk']}</td>
            <td class="w-center">{w['dmg']}</td>
            <td class="w-special">{w['special']}</td>
        </tr>"""
    return rows

def make_card(op, team):
    fc = team["faction_color"]
    fa = team["faction_accent"]
    fl = team["faction_light"]
    ht = team["header_text"]

    ranged_rows = weapon_rows(op["ranged"])
    melee = op["melee"]

    return f"""
<div class="card">
    <!-- HEADER -->
    <div class="card-header" style="background: linear-gradient(135deg, {fc} 0%, {fa} 100%);">
        <div class="header-number">#{op['number']}</div>
        <div class="header-left">
            <div class="callsign" style="color:{fl};">{op['callsign']}</div>
            <div class="op-name" style="color:{ht};">{op['name']}</div>
            <div class="role" style="color:{fl};">{op['role']}</div>
        </div>
        <div class="faction-tag" style="background:#ffffff; color:{fc}; border: 2px solid {fc};">
            {team['name'].split()[0]}<br>{team['name'].split()[1] if len(team['name'].split())>1 else ''}
        </div>
    </div>

    <!-- STAT BLOCK -->
    <div class="stats-bar">
        <div class="stat-box" style="border-bottom: 3px solid {fc};">
            <div class="stat-label">MOV</div>
            <div class="stat-value">{op['mov']}</div>
        </div>
        <div class="stat-sep"></div>
        <div class="stat-box" style="border-bottom: 3px solid {fc};">
            <div class="stat-label">HP</div>
            <div class="stat-value">{op['hp']}</div>
        </div>
        <div class="stat-sep"></div>
        <div class="stat-box" style="border-bottom: 3px solid {fc};">
            <div class="stat-label">AC</div>
            <div class="stat-value">{op['ac']}</div>
        </div>
        <div class="stat-sep"></div>
        <div class="stat-box" style="border-bottom: 3px solid {fc};">
            <div class="stat-label">PER</div>
            <div class="stat-value">{op['per']}</div>
        </div>
    </div>

    <!-- WEAPONS -->
    <div class="section-label" style="background:{fc}; color:#ffffff;">⬤ RANGED WEAPONS</div>
    <table class="weapon-table">
        <thead>
            <tr>
                <th class="w-name">WEAPON</th>
                <th class="w-center">RNG</th>
                <th class="w-center">ATK</th>
                <th class="w-center">DMG</th>
                <th class="w-special">SPECIAL</th>
            </tr>
        </thead>
        <tbody>
            {ranged_rows}
        </tbody>
    </table>

    <div class="section-label" style="background:{fc}; color:#ffffff;">⬤ MELEE WEAPON</div>
    <table class="weapon-table">
        <thead>
            <tr>
                <th class="w-name">WEAPON</th>
                <th class="w-center">ATK</th>
                <th class="w-center">DMG</th>
                <th class="w-special" colspan="2">SPECIAL</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="w-name">{melee['name']}</td>
                <td class="w-center">{melee['atk']}</td>
                <td class="w-center">{melee['dmg']}</td>
                <td class="w-special" colspan="2">{melee['special']}</td>
            </tr>
        </tbody>
    </table>

    <!-- ABILITY -->
    <div class="section-label" style="background:{fc}; color:#ffffff;">⬤ SPECIAL ABILITY</div>
    <div class="ability-box" style="border-left: 4px solid {fc};">
        <span class="ability-name" style="color:{fc};">{op['ability_name']}.</span>
        <span class="ability-text"> {op['ability']}</span>
    </div>
</div>
"""

def make_page(cards_html, page_class=""):
    return f'<div class="page {page_class}">{cards_html}</div>'

def build_html():
    cards = []
    for team in TEAMS:
        for op in team["operants"]:
            cards.append(make_card(op, team))

    # 2 cards per page
    pages = []
    for i in range(0, len(cards), 2):
        pair = cards[i]
        if i + 1 < len(cards):
            pair += cards[i + 1]
        pages.append(make_page(pair))

    pages_html = "\n".join(pages)

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;900&family=Barlow:wght@400;500;600&display=swap');

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
      font-family: 'Barlow', 'Arial Narrow', Arial, sans-serif;
      background: #ffffff;
      color: #111;
  }}

  .page {{
      width: 210mm;
      min-height: 297mm;
      padding: 10mm;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      gap: 8mm;
      page-break-after: always;
  }}

  /* ── CARD ── */
  .card {{
      background: #ffffff;
      border: 1.5px solid #ccc;
      border-radius: 6px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      flex: 1;
  }}

  /* ── HEADER ── */
  .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 12px;
      min-height: 64px;
      gap: 12px;
  }}
  .header-number {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-weight: 300;
      font-size: 52px;
      line-height: 1;
      letter-spacing: -2px;
      min-width: 42px;
      text-align: center;
      color: #ffffff;
  }}
  .callsign {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-weight: 900;
      font-size: 22px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #ffffff;
  }}
  .op-name {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-weight: 600;
      font-size: 13px;
      letter-spacing: 1px;
      margin-top: 1px;
      color: rgba(255,255,255,0.9);
  }}
  .header-left {{ flex: 1; }}
  .role {{
      font-size: 10px;
      font-weight: 500;
      letter-spacing: 1px;
      margin-top: 2px;
      text-transform: uppercase;
      color: rgba(255,255,255,0.75);
  }}
  .faction-tag {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-weight: 900;
      font-size: 8px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      text-align: center;
      padding: 5px 7px;
      border-radius: 4px;
      line-height: 1.3;
  }}

  /* ── STATS ── */
  .stats-bar {{
      display: flex;
      align-items: stretch;
      height: 48px;
      border-bottom: 1.5px solid #e0e0e0;
  }}
  .stat-box {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 4px 0;
      background: #ffffff;
  }}
  .stat-sep {{
      width: 1px;
      background: #e0e0e0;
      margin: 6px 0;
  }}
  .stat-label {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-size: 8px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #888;
  }}
  .stat-value {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-size: 22px;
      font-weight: 600;
      color: #111;
      line-height: 1;
  }}

  /* ── SECTION LABEL ── */
  .section-label {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 2px;
      padding: 3px 10px;
      text-transform: uppercase;
  }}

  /* ── WEAPON TABLE ── */
  .weapon-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
  }}
  .weapon-table thead tr {{
      background: #f5f5f5;
  }}
  .weapon-table th {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #555;
      padding: 4px 8px;
      text-align: left;
      border-bottom: 1px solid #ddd;
      text-transform: uppercase;
  }}
  .weapon-table td {{
      padding: 5px 8px;
      color: #222;
      vertical-align: middle;
      border-bottom: 1px solid #eee;
      text-align: left;
  }}
  .weapon-table tbody tr:last-child td {{ border-bottom: none; }}
  .weapon-table tbody tr.row-alt {{ background: #fafafa; }}
  .w-name   {{ width: 28%; font-weight: 600; color: #111; }}
  .w-center {{ width: 9%; text-align: left; font-family: 'Barlow Condensed', monospace; font-weight: 700; color: #111; }}
  .w-special {{ color: #444; font-size: 12px; }}

  /* ── ABILITY ── */
  .ability-box {{
      margin: 6px 10px 8px;
      padding: 6px 10px;
      background: #f9f9f9;
      border-radius: 3px;
      font-size: 13px;
      line-height: 1.5;
  }}
  .ability-name {{
      font-family: 'Barlow Condensed', 'Arial Narrow', Arial, sans-serif;
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 0.5px;
  }}
  .ability-text {{
      color: #333;
  }}
</style>
</head>
<body>
{pages_html}
</body>
</html>
"""

if __name__ == "__main__":
    html = build_html()

    out_html = "/Users/aga/code/omat/strike-team/character_cards.html"
    out_pdf  = "/Users/aga/code/omat/strike-team/character_cards.pdf"

    with open(out_html, "w") as f:
        f.write(html)

    print("Converting to PDF...")
    HTML(filename=out_html).write_pdf(
        out_pdf,
        stylesheets=[CSS(string="@page { size: A4; margin: 0; }")]
    )
    print(f"Done! → {out_pdf}")
