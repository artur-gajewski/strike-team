#!/usr/bin/env python3
"""Generate Kill Team-style rules booklet PDF for Strike Team game."""

from weasyprint import HTML, CSS

ACCENT = "#C0392B"   # matches Crimson Talons red as the "game" colour

HTML_CONTENT = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@300;400;600;700;900&family=Barlow:wght@400;500;600&display=swap');

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
      font-family: 'Barlow', 'Arial Narrow', Arial, sans-serif;
      background: #ffffff;
      color: #111;
      font-size: 13px;
      line-height: 1.6;
  }}

  /* ── PAGE ── */
  .page {{
      width: 210mm;
      min-height: 297mm;
      padding: 0;
      background: #ffffff;
      page-break-after: always;
      display: flex;
      flex-direction: column;
  }}

  /* ── COVER PAGE ── */
  .cover {{
      background: #ffffff;
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20mm;
      gap: 6mm;
  }}
  .cover-eyebrow {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 300;
      font-size: 13px;
      letter-spacing: 5px;
      text-transform: uppercase;
      color: rgba(192,57,43,0.6);
  }}
  .cover-title {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 900;
      font-size: 64px;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: {ACCENT};
      text-align: center;
      line-height: 1;
  }}
  .cover-subtitle {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 300;
      font-size: 20px;
      letter-spacing: 6px;
      text-transform: uppercase;
      color: rgba(123,16,16,0.75);
      text-align: center;
  }}
  .cover-rule {{
      width: 60mm;
      height: 2px;
      background: rgba(192,57,43,0.3);
      margin: 4mm 0;
  }}
  .cover-tagline {{
      font-size: 12px;
      color: rgba(192,57,43,0.5);
      letter-spacing: 2px;
      text-transform: uppercase;
      text-align: center;
  }}

  /* ── CONTENT PAGES ── */
  .content-page {{
      flex: 1;
      display: flex;
      flex-direction: column;
  }}
  .page-header {{
      background: linear-gradient(135deg, {ACCENT} 0%, #A93226 100%);
      padding: 6px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
  }}
  .page-header-title {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 700;
      font-size: 11px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: rgba(255,255,255,0.8);
  }}
  .page-header-game {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 300;
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: rgba(255,255,255,0.5);
  }}

  .page-body {{
      flex: 1;
      padding: 10mm 14mm;
      display: flex;
      flex-direction: column;
      gap: 7mm;
  }}

  .page-footer {{
      border-top: 1px solid #e0e0e0;
      padding: 4px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
  }}
  .page-footer-text {{
      font-size: 9px;
      color: #aaa;
      letter-spacing: 1px;
      text-transform: uppercase;
  }}

  /* ── SECTION HEADING ── */
  .section-heading {{
      border-left: 5px solid {ACCENT};
      padding-left: 10px;
      margin-bottom: 2mm;
  }}
  .section-heading h2 {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 900;
      font-size: 22px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #111;
      line-height: 1;
  }}
  .section-heading .sub {{
      font-size: 11px;
      color: #888;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-top: 1px;
  }}

  /* ── SUBSECTION HEADING ── */
  .sub-heading {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: {ACCENT};
      margin-bottom: 2px;
      margin-top: 4px;
  }}

  /* ── BODY TEXT ── */
  p {{ margin-bottom: 3mm; color: #222; }}
  strong {{ color: #111; font-weight: 600; }}

  /* ── RULE BLOCK (highlighted callout) ── */
  .rule-block {{
      background: #f8f8f8;
      border-left: 4px solid {ACCENT};
      padding: 8px 12px;
      border-radius: 0 4px 4px 0;
      font-size: 12px;
      color: #333;
  }}
  .rule-block strong {{ color: {ACCENT}; }}

  /* ── NUMBERED LIST ── */
  ol.steps {{
      padding-left: 20px;
      margin: 0;
  }}
  ol.steps li {{
      margin-bottom: 4px;
      color: #222;
  }}

  /* ── BULLET LIST ── */
  ul.rules-list {{
      padding-left: 20px;
      margin: 0;
  }}
  ul.rules-list li {{
      margin-bottom: 4px;
      color: #222;
  }}

  /* ── CP ACTION CARDS ── */
  .action-cards {{
      display: flex;
      gap: 5mm;
  }}
  .action-card {{
      flex: 1;
      border: 1.5px solid #ddd;
      border-radius: 6px;
      overflow: hidden;
  }}
  .action-card-header {{
      background: linear-gradient(135deg, {ACCENT} 0%, #A93226 100%);
      padding: 6px 10px;
      display: flex;
      align-items: center;
      gap: 8px;
  }}
  .action-card-icon {{
      font-size: 18px;
      line-height: 1;
  }}
  .action-card-title {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #ffffff;
  }}
  .action-card-cp {{
      margin-left: auto;
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-size: 11px;
      font-weight: 600;
      color: rgba(255,255,255,0.7);
      letter-spacing: 1px;
  }}
  .action-card-body {{
      padding: 8px 10px;
      font-size: 11px;
      color: #333;
      line-height: 1.5;
      background: #fff;
  }}

  /* ── DATA TABLE ── */
  .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
  }}
  .data-table thead tr {{
      background: {ACCENT};
  }}
  .data-table th {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 2px;
      color: #ffffff;
      padding: 5px 10px;
      text-align: left;
      text-transform: uppercase;
  }}
  .data-table td {{
      padding: 6px 10px;
      color: #222;
      border-bottom: 1px solid #eee;
      vertical-align: middle;
  }}
  .data-table tbody tr:nth-child(even) {{ background: #f9f9f9; }}
  .data-table tbody tr:last-child td {{ border-bottom: none; }}
  .data-table td strong {{ color: {ACCENT}; }}

  /* ── QUICK REFERENCE BOX ── */
  .quick-ref {{
      border: 1.5px solid {ACCENT};
      border-radius: 6px;
      overflow: hidden;
  }}
  .quick-ref-header {{
      background: {ACCENT};
      padding: 5px 12px;
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 700;
      font-size: 11px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #ffffff;
  }}
  .quick-ref-body {{
      padding: 8px 12px;
      display: flex;
      gap: 6mm;
  }}
  .quick-ref-col {{
      flex: 1;
  }}
  .qr-label {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 700;
      font-size: 10px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: {ACCENT};
      margin-bottom: 3px;
      border-bottom: 1px solid #eee;
      padding-bottom: 2px;
  }}
  .qr-item {{
      font-size: 11px;
      color: #333;
      margin-bottom: 2px;
      padding-left: 8px;
      position: relative;
  }}
  .qr-item::before {{
      content: '›';
      position: absolute;
      left: 0;
      color: {ACCENT};
      font-weight: 700;
  }}

  /* ── EXAMPLE BOX ── */
  .example-box {{
      background: #f5f5f5;
      border: 1px solid #ddd;
      border-radius: 6px;
      padding: 8px 12px;
      font-size: 11px;
      color: #333;
      line-height: 1.6;
  }}
  .example-box .ex-label {{
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 700;
      font-size: 10px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: {ACCENT};
      margin-bottom: 5px;
  }}
  .example-box .ex-step {{
      margin-bottom: 5px;
      padding-left: 10px;
      border-left: 2px solid #ddd;
  }}
  .example-box .ex-step strong {{ color: #111; }}

  /* ── WHAT YOU NEED — DICE GRID ── */
  .need-grid {{
      display: flex;
      gap: 3mm;
      flex-wrap: wrap;
      margin-top: 3mm;
  }}
  .need-chip {{
      flex: 1;
      min-width: 28mm;
      border: 1.5px solid #ddd;
      border-radius: 6px;
      overflow: hidden;
      text-align: center;
  }}
  .need-chip-die {{
      background: {ACCENT};
      color: #ffffff;
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 900;
      font-size: 20px;
      letter-spacing: 1px;
      padding: 6px 0;
  }}
  .need-chip-desc {{
      padding: 5px 6px;
      font-size: 10px;
      color: #444;
      line-height: 1.4;
      background: #fff;
  }}

  /* ── CONDITIONS TABLE ── */
  .conditions-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 3mm;
  }}
  .condition-chip {{
      border: 1.5px solid #ddd;
      border-radius: 5px;
      overflow: hidden;
      width: calc(50% - 1.5mm);
  }}
  .condition-chip-header {{
      background: #222;
      padding: 3px 8px;
      font-family: 'Barlow Condensed', Arial, sans-serif;
      font-weight: 700;
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #fff;
  }}
  .condition-chip-body {{
      padding: 5px 8px;
      font-size: 11px;
      color: #333;
      line-height: 1.4;
      background: #fff;
  }}
  .condition-chip-body .ends {{
      font-size: 10px;
      color: #999;
      margin-top: 2px;
  }}
</style>
</head>
<body>

<!-- ════════════════════════════════════════════════════
     PAGE 1 — COVER
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="cover">
    <div class="cover-eyebrow">Tabletop Skirmish Game</div>
    <div class="cover-rule"></div>
    <div class="cover-title">Strike<br>Team</div>
    <div class="cover-subtitle">Basic Rules</div>
    <div class="cover-rule"></div>
    <div class="cover-tagline">Two teams. Three command points. One survivor.</div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 2 — INTRODUCTION & LORE
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">Introduction</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body">

      <div>
        <div class="section-heading">
          <h2>What Is Strike Team?</h2>
        </div>
        <p><strong>Strike Team</strong> is a fast-paced tactical skirmish game for two players. Each player commands a squad of five elite operants — soldiers, scouts, specialists — in a close-quarters battle fought across ruined urban terrain, industrial complexes, and hostile wilderness. Games last 30–60 minutes and require no board: only a play surface, terrain, miniatures, and dice.</p>
        <p>Unlike large-scale wargames, Strike Team focuses on the individual. Every operant has a name, a role, and a unique special ability. Every decision matters. Losing a single operative can swing the battle. There are no respawns, no reinforcements, and no extraction plan — only the mission.</p>
        <p>The game blends the tactical depth of a miniatures wargame with the character-driven mechanics of a d20 styled tabletop roleplaying game. Operant stats are presented as character sheets: Movement, Hit Points, Armor Class, Perception. Combat is resolved with a d20 roll, keeping the system intuitive for players from both hobby traditions.</p>
      </div>

      <div>
        <div class="section-heading">
          <h2>The World</h2>
          <div class="sub">Near-future. No law. Only contract.</div>
        </div>
        <p>It is the mid-22nd century. Nation-states have fractured. The gap between the last war and the next one is measured in weeks, not years. Private military corporations now fill the void left by collapsed governments — enforcing contracts, seizing resources, and eliminating threats with surgical precision.</p>
        <p>Most conflicts never make the news. They are settled quietly, in the dark, by small teams of expendable professionals. These operants are the instrument of choice: five soldiers, deployed behind enemy lines with no support, no witnesses, and a clear objective.</p>
      </div>

      <div>
        <div class="section-heading">
          <h2>The Factions</h2>
        </div>

        <div class="sub-heading" style="color: #C0392B;">⬤ Crimson Talons Vanguard</div>
        <p>A veteran rapid-response unit built from the ruins of a dissolved special operations programme. The Talons operate under a strict chain of command, led by their battle-hardened Sergeant. They are disciplined, adaptable, and fiercely loyal to one another. Where other units rely on firepower, the Talons rely on coordination — their greatest weapon is the team itself. They fight not for money, but for the belief that someone has to hold the line.</p>

        <div class="sub-heading" style="color: #1A4A8A; margin-top: 5mm;">⬤ Ashborn Syndicate Strike Cell</div>
        <p>The Syndicate is a corporate mercenary outfit operating on the edge of legality — and frequently beyond it. Their operants are augmented with black-market cybernetics: optical implants, combat reflexes, reinforced skeletal frames. They take contracts others refuse and ask no questions about the target. The Syndicate doesn't lose operants — it replaces them. Loyalty is a line item on the budget. What holds this cell together isn't brotherhood. It's the payout.</p>

        <div class="rule-block" style="margin-top: 5mm;">
          <strong>In Strike Team,</strong> these two factions are in direct opposition — but the rules support any narrative you build. Rename the teams, create new operants, and make the world your own.
        </div>
      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">2</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 3 — WHAT DO YOU NEED
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">What Do You Need to Play</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body">

      <div class="section-heading">
        <h2>What Do You Need to Play</h2>
      </div>

      <!-- DICE -->
      <div>
        <div class="sub-heading">🎲 Dice</div>
        <p>You will need a set of polyhedral dice. Both players share or bring their own. The following dice are used in Strike Team:</p>
        <div class="need-grid">
          <div class="need-chip">
            <div class="need-chip-die">d4</div>
            <div class="need-chip-desc">Poison, Burning damage &amp; light weapon damage</div>
          </div>
          <div class="need-chip">
            <div class="need-chip-die">d6</div>
            <div class="need-chip-desc">Sidearms, blades &amp; general weapon damage</div>
          </div>
          <div class="need-chip">
            <div class="need-chip-die">d8</div>
            <div class="need-chip-desc">Rifles, axes &amp; heavy weapon damage</div>
          </div>
          <div class="need-chip">
            <div class="need-chip-die">d10</div>
            <div class="need-chip-desc">Marksman rifles, cannons &amp; sniper weapons</div>
          </div>
          <div class="need-chip">
            <div class="need-chip-die">d20</div>
            <div class="need-chip-desc">All attack rolls and Perception (Scout) checks</div>
          </div>
        </div>
        <div class="rule-block" style="margin-top:4mm;">
          <strong>Tip:</strong> Having 2–3 of each die speeds up play, especially for blast weapons that roll multiple dice at once.
        </div>
      </div>

      <!-- RULER -->
      <div>
        <div class="sub-heading">📏 Ruler or Measuring Tape</div>
        <p>All distances in Strike Team are measured in <strong>inches</strong>. You need a ruler or flexible measuring tape marked in inches to measure movement, weapon ranges, and ability radii.</p>
      </div>

      <!-- MINIATURES -->
      <div>
        <div class="sub-heading">🧍 10 Miniatures (Five Red, Five Blue)</div>
        <p>Each team requires five miniatures on <strong>1-inch round bases</strong>. Use two sets in contrasting team colours:</p>
        <ul class="rules-list">
          <li><strong>5 Red miniatures</strong> — Crimson Talons Vanguard (Operants #1–5)</li>
          <li><strong>5 Blue miniatures</strong> — Ashborn Syndicate Strike Cell (Operants #1–5)</li>
        </ul>
        <p style="margin-top:2mm;">Each miniature must be individually identifiable by its <strong>operant number (#1–#5)</strong>, matching the number printed on that operant's character sheet. Use numbered bases, stickers, paint markings, or small numbered tokens beneath each model.</p>
      </div>

      <!-- TOKENS -->
      <div>
        <div class="sub-heading">🪙 Tokens &amp; Markers</div>
        <p>You will need the following tokens during play. Small coloured coins, poker chips, or printed chits all work well:</p>
        <table class="data-table">
          <thead>
            <tr>
              <th>Token</th>
              <th>Qty</th>
              <th>Purpose</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Spotted</strong></td><td>10</td><td>Placed next to an operant detected by a Scout action — marks them as targetable by Shoot actions. Removed when that operant moves at least 1".</td></tr>
            <tr><td><strong>Overwatch</strong></td><td>2</td><td>Placed when Phantom (Crimson Talons) uses their Overwatch Eye ability — triggers a free attack</td></tr>
            <tr><td><strong>Demolition Charge</strong></td><td>1</td><td>Placed on terrain by Ironkeg — explodes when triggered or detonated remotely</td></tr>
            <tr><td><strong>Sentry Drone</strong></td><td>1</td><td>Placed on the battlefield by Arc (Ashborn Syndicate) — attacks independently each round</td></tr>
          </tbody>
        </table>
      </div>

      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">3</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 3 — SETTING UP THE PLAY AREA
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">Setting Up the Play Area</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body" style="padding-top: 16mm;">

      <!-- PLAY AREA -->
      <div>
        <div class="sub-heading">🗺️ Play Mat or Playing Surface</div>
        <p>Strike Team is played on a flat surface representing the battlefield. The recommended playing area is <strong>30" × 24"</strong> — large enough to give operants room to maneuver while keeping engagements tense. Any of the following work well:</p>
        <ul class="rules-list">
          <li><strong>Neoprene game mat</strong> — printed with urban, industrial, or wilderness textures (ideal)</li>
          <li><strong>Plain green or grey felt</strong> — cheap and easy to cut to size</li>
          <li><strong>Poster board or large cutting mat</strong> — practical for casual play</li>
          <li><strong>Tabletop with marked grid</strong> — use a 1" grid mat for easier distance measuring</li>
        </ul>
      </div>

      <!-- TERRAIN -->
      <div>
        <div class="sub-heading">🧱 Terrain Obstacles</div>
        <p>Terrain pieces create the obstacles, cover, and chokepoints that make the game tactical. You need a mix of <strong>blocking terrain</strong> (fully hides operants) and <strong>cover terrain</strong> (partial protection). Recommended pieces:</p>
        <table class="data-table">
          <thead><tr><th>Terrain Piece</th><th>Type</th><th>Suggested Qty</th></tr></thead>
          <tbody>
            <tr><td><strong>Ruined walls / barricades</strong></td><td>Cover</td><td>6–8</td></tr>
            <tr><td><strong>Shipping containers / crates</strong></td><td>Cover &amp; Blocking</td><td>4–6</td></tr>
            <tr><td><strong>Small buildings / ruins</strong></td><td>Blocking</td><td>2–4</td></tr>
            <tr><td><strong>Rock formations / boulders</strong></td><td>Cover</td><td>4–6</td></tr>
            <tr><td><strong>Trees / dense foliage clusters</strong></td><td>Obscuring</td><td>3–5</td></tr>
            <tr><td><strong>Fuel drums / pillars</strong></td><td>Cover</td><td>4–6</td></tr>
          </tbody>
        </table>
        <div class="rule-block" style="margin-top:3mm;">
          Miniature terrain, 3D-printed scenery, LEGO bricks, or cardboard cut-outs all work. What matters is that both players agree on which pieces <strong>block line of sight</strong> and which only grant <strong>cover (+2 AC)</strong> before the game starts.
        </div>
      </div>

      <div>
        <div class="section-heading">
          <h2>Setting Up the Play Area</h2>
          <div class="sub">Board size · Terrain placement · Deployment zones</div>
        </div>
        <p>A well-constructed play area rewards tactical movement, punishes reckless charges, and ensures neither team has a natural advantage. Follow these steps before the first turn.</p>
      </div>

      <!-- STEP 1 -->
      <div>
        <div class="sub-heading">Step 1 — Lay Out the Board</div>
        <p>Set up your playing surface (<strong>30" × 24"</strong> recommended). Orient it so the long edges face each player. Define the two short edges as <strong>deployment edges</strong> — each player deploys from their own edge.</p>
        <div class="rule-block">
          <strong>Deployment zone:</strong> Each player places all five of their operants within <strong>4" of their deployment edge</strong> before the game begins. Operants start visible — Spotted tokens are not required at deployment.
        </div>
      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">4</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 4 — SETTING UP (CONTINUED)
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">Setting Up the Play Area (continued)</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body">

      <!-- STEP 2 -->
      <div>
        <div class="sub-heading">Step 2 — Place Terrain</div>
        <p>Players alternate placing terrain pieces, one at a time, starting with the player who lost the last dice roll (or a coin flip for the first game). Follow these guidelines for a balanced battlefield:</p>
        <ul class="rules-list">
          <li>Aim for <strong>8–14 terrain pieces</strong> total on a 30"×24" board.</li>
          <li>Place <strong>at least 2 large blocking pieces</strong> (buildings, container stacks) in the central zone to create mid-field cover and break long sightlines.</li>
          <li>Scatter <strong>cover pieces</strong> (crates, barricades, boulders) across the board — roughly one piece every 6–8".</li>
          <li>Place <strong>trees or foliage</strong> in clusters of 2–3 to create obscuring zones where operants can hide.</li>
          <li>No terrain piece may be placed within <strong>3" of a deployment edge</strong>.</li>
          <li>No terrain piece may be placed within <strong>1" of another terrain piece</strong>.</li>
        </ul>
      </div>

      <!-- STEP 3 -->
      <div>
        <div class="sub-heading">Step 3 — Agree on Terrain Rules</div>
        <p>Before the game, both players must agree on the following for each terrain type:</p>
        <table class="data-table">
          <thead><tr><th>Terrain Type</th><th>Blocks Line of Sight?</th><th>Grants Cover (+2 AC)?</th><th>Passable?</th></tr></thead>
          <tbody>
            <tr><td><strong>Solid walls / buildings</strong></td><td>✅ Yes</td><td>✅ Yes (edge)</td><td>❌ No</td></tr>
            <tr><td><strong>Crates / barricades</strong></td><td>✅ Yes (if taller than base)</td><td>✅ Yes</td><td>❌ No</td></tr>
            <tr><td><strong>Boulders / rocks</strong></td><td>✅ Yes</td><td>✅ Yes</td><td>❌ No</td></tr>
            <tr><td><strong>Trees / foliage</strong></td><td>✅ Yes (obscuring)</td><td>✅ Yes</td><td>✅ Yes (costs +1" per 2" moved through)</td></tr>
            <tr><td><strong>Fuel drums / pillars</strong></td><td>❌ No</td><td>✅ Yes</td><td>❌ No</td></tr>
          </tbody>
        </table>
      </div>

      <!-- STEP 4 -->
      <div>
        <div class="sub-heading">Step 4 — Deploy Operants</div>
        <p>Players roll off (d20, highest wins) to decide who deploys first. The <strong>winner deploys last</strong> — a tactical advantage. Players alternate placing one operant at a time within their deployment zone until all ten operants are on the board.</p>
        <div class="rule-block">
          <strong>Tip:</strong> Place scouts (Phantom, Whisper) near flanks for early Overwatch positions. Deploy heavy operants (Ironkeg, Vault) centrally where they can control chokepoints. Keep your medic (Stitch) behind other operants at deployment.
        </div>
      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">5</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 5 — OVERVIEW + TURN STRUCTURE
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">Overview &amp; Turn Structure</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body">

      <div>
        <div class="section-heading">
          <h2>Overview</h2>
        </div>
        <p>Two players each control a <strong>Strike Team</strong> of five operants. Players alternate turns, spending <strong>Command Points</strong> to activate operants — maneuvering for position, gathering intelligence, and eliminating the enemy.</p>
        <p>The goal is to <strong>down all enemy operants</strong>, or achieve your mission objective before the enemy achieves theirs.</p>
      </div>

      <div>
        <div class="section-heading">
          <h2>Turn Structure</h2>
          <div class="sub">3 Command Points per turn</div>
        </div>
        <p>Players alternate taking turns. On <strong>your turn</strong>, you receive <strong>3 Command Points (CP)</strong>. Each CP is spent on one action assigned to one operant.</p>
        <div class="rule-block">
          <strong>Key rule:</strong> An operant may receive up to 3 CP per turn — one Move, one Scout, and one Shoot/Fight — but <strong>the same action type cannot be assigned twice to the same operant</strong>. Unused CP are lost at end of turn.
        </div>
      </div>

      <div>
        <div class="action-cards">
          <div class="action-card">
            <div class="action-card-header">
              <div class="action-card-icon">🏃</div>
              <div class="action-card-title">Move</div>
              <div class="action-card-cp">1 CP</div>
            </div>
            <div class="action-card-body">
              Move one operant up to their full <strong>MOV</strong> distance in any direction. Operants in <strong>cover</strong> at end of move gain <strong>+2 AC</strong> vs ranged until they move again.
            </div>
          </div>
          <div class="action-card">
            <div class="action-card-header">
              <div class="action-card-icon">🔍</div>
              <div class="action-card-title">Scout</div>
              <div class="action-card-cp">1 CP</div>
            </div>
            <div class="action-card-body">
              Attempt to detect a <strong>hidden enemy</strong>. Roll <strong>d20 + PER</strong> vs Detection DC (set by distance). On success, the target is <strong>Spotted</strong> and can be targeted.
            </div>
          </div>
          <div class="action-card">
            <div class="action-card-header">
              <div class="action-card-icon">🔫</div>
              <div class="action-card-title">Shoot / Fight</div>
              <div class="action-card-cp">1 CP</div>
            </div>
            <div class="action-card-body">
              Attack a <strong>visible (Spotted)</strong> enemy. Roll <strong>d20 + ATK bonus</strong> vs target's <strong>AC</strong>. On a hit, roll weapon <strong>Damage Dice</strong> and apply any Special effects.
            </div>
          </div>
        </div>
      </div>

      <div>
        <div class="rule-block">
          <strong>Examples:</strong> Move one operant, Scout with them, then Shoot with them (all 3 CP on one operant). Or Move one operant and Shoot with two others. You <em>cannot</em> Shoot twice with the same operant, but you can Shoot with two different operants.
        </div>
      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">6</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 6 — ACTIONS IN DETAIL
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">Actions in Detail</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body">

      <!-- MOVE -->
      <div>
        <div class="section-heading">
          <h2>🏃 Move</h2>
        </div>
        <p>Choose one operant. Move them up to their full <strong>MOV</strong> distance (in inches) in any direction.</p>
        <ul class="rules-list">
          <li>Operants <strong>may not move through</strong> other operants or impassable terrain.</li>
          <li>Moving within <strong>1" of an enemy</strong> ends your movement — you are now engaged in melee.</li>
          <li>An operant ending their Move in <strong>cover</strong> (wall, crate, barricade) gains <strong>+2 AC</strong> against ranged attacks until they next move.</li>
        </ul>
      </div>

      <!-- SCOUT -->
      <div>
        <div class="section-heading">
          <h2>🔍 Scout</h2>
        </div>
        <p>Choose one operant. They attempt to detect a <strong>hidden enemy</strong>. An enemy starts hidden if they are behind a structure with no line of sight from any of your operants — hidden operants <strong>cannot be targeted</strong> by Shoot or Fight actions.</p>
        <div class="sub-heading">How to Scout</div>
        <ol class="steps">
          <li>Declare which enemy operant you are scouting for and their approximate location.</li>
          <li>Roll <strong>d20 + your operant's PER modifier</strong>.</li>
          <li>Compare the result to the <strong>Detection DC</strong> for that distance.</li>
        </ol>
        <br>
        <table class="data-table">
          <thead>
            <tr>
              <th>Distance to Target</th>
              <th>Detection DC</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>0" – 8"</td><td><strong>10</strong></td></tr>
            <tr><td>9" – 16"</td><td><strong>13</strong></td></tr>
            <tr><td>17" – 24"</td><td><strong>16</strong></td></tr>
            <tr><td>25" – 32"</td><td><strong>19</strong></td></tr>
            <tr><td>33"+</td><td><strong>22</strong></td></tr>
          </tbody>
        </table>
        <br>
        <ul class="rules-list">
          <li><strong>Success:</strong> Place a <strong>Spotted token</strong> next to the target's miniature. That operant can now be targeted by Shoot and Fight actions. The Spotted condition is removed as soon as the target moves at least <strong>1"</strong>.</li>
          <li><strong>Failure:</strong> The CP is wasted. You may try again next turn.</li>
          <li><strong>Line of Sight required:</strong> Your operant must have a clear line to at least part of the structure the target hides behind. You cannot Scout through solid walls.</li>
        </ul>
      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">7</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 7 — SHOOT / FIGHT + DAMAGE
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">Shoot, Fight &amp; Damage</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body">

      <div>
        <div class="section-heading">
          <h2>🔫 Shoot / ⚔️ Fight</h2>
        </div>
        <p>Choose one operant. They attack a <strong>visible (Spotted)</strong> enemy — one that is not hidden, or that has already been Spotted.</p>
      </div>

      <div>
        <div class="sub-heading">Ranged Attack (Shoot)</div>
        <ol class="steps">
          <li>Choose a ranged weapon and a target within that weapon's <strong>Range</strong>.</li>
          <li>Roll <strong>d20 + weapon's Attack Bonus</strong>.</li>
          <li>If the result equals or exceeds the target's <strong>AC</strong>, the attack <strong>hits</strong>.</li>
          <li>Roll the weapon's <strong>Damage Dice</strong> and subtract from the target's HP.</li>
          <li>Apply any weapon <strong>Special</strong> effects on a hit.</li>
        </ol>
        <br>
        <div class="rule-block">
          <strong>Cover:</strong> If the target is in cover, their AC increases by <strong>+2</strong> against this attack.<br>
          <strong>Out of Range:</strong> You may not Shoot against a target beyond your weapon's listed range.
        </div>
      </div>

      <div>
        <div class="sub-heading">Melee Attack (Fight)</div>
        <ol class="steps">
          <li>Your operant must be <strong>within 1"</strong> of the target (engaged in melee).</li>
          <li>Choose your melee weapon.</li>
          <li>Roll <strong>d20 + weapon's Attack Bonus</strong>.</li>
          <li>If the result equals or exceeds the target's <strong>AC</strong>, the attack <strong>hits</strong>.</li>
          <li>Roll the weapon's <strong>Damage Dice</strong> and subtract from the target's HP.</li>
          <li>Apply any weapon <strong>Special</strong> effects on a hit.</li>
        </ol>
        <br>
        <div class="rule-block">
          <strong>Cover does not apply</strong> to melee attacks — it only protects against ranged fire.
        </div>
      </div>

      <div>
        <div class="section-heading">
          <h2>Damage &amp; Downed Operants</h2>
        </div>
        <ul class="rules-list">
          <li>When an operant's <strong>HP reaches 0</strong>, they are <strong>Downed</strong> — remove them from the battlefield immediately.</li>
          <li>Downed operants may not take actions, be activated, or block movement.</li>
          <li>There is <strong>no recovery</strong> from being Downed unless a Special Ability explicitly states otherwise.</li>
        </ul>
      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">8</div>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════
     PAGE 8 — SPOTTED CONDITION + QUICK REFERENCE + EXAMPLE
     ════════════════════════════════════════════════════ -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <div class="page-header-title">Spotted Condition, Reference &amp; Example</div>
      <div class="page-header-game">Strike Team · Basic Rules</div>
    </div>
    <div class="page-body">

      <div>
        <div class="section-heading">
          <h2>The Spotted Condition</h2>
          <div class="sub">The only condition in Strike Team</div>
        </div>
        <p>An enemy operant that is <strong>hiding behind an obstacle</strong> — out of direct line of sight — cannot be targeted by Shoot or Fight actions until they are <strong>Spotted</strong>.</p>
        <p>When a Scout action succeeds, the scouting operant has detected the hidden enemy. Place a <strong>Spotted token</strong> next to that enemy's miniature to identify their condition. That operant can now be targeted for shooting — as long as the attacker has line of sight to any part of the target's position.</p>
        <div class="rule-block">
          <strong>Removing Spotted:</strong> The Spotted condition is removed immediately when the target operant moves at least <strong>1"</strong>. They are once again hidden and cannot be targeted until Spotted again by a new Scout action.
        </div>
        <br>
        <table class="data-table">
          <thead>
            <tr><th>Situation</th><th>Can be targeted?</th></tr>
          </thead>
          <tbody>
            <tr><td>In open — no obstacle between attacker and target</td><td>✅ Yes</td></tr>
            <tr><td>Behind obstacle, no Spotted token</td><td>❌ No — must Scout first</td></tr>
            <tr><td>Behind obstacle, has Spotted token</td><td>✅ Yes — until they move 1"</td></tr>
            <tr><td>Had Spotted token, moved 1" or more</td><td>❌ No — token removed, must Scout again</td></tr>
          </tbody>
        </table>
      </div>

      <div>
        <div class="quick-ref">
          <div class="quick-ref-header">⚡ Quick Reference — Your Turn</div>
          <div class="quick-ref-body">
            <div class="quick-ref-col">
              <div class="qr-label">Turn Setup</div>
              <div class="qr-item">Receive 3 Command Points (CP)</div>
              <div class="qr-item">Each CP = one action on one operant</div>
              <div class="qr-item">Max: 1 Move + 1 Scout + 1 Shoot per operant</div>
              <div class="qr-item">Unused CP are lost</div>
            </div>
            <div class="quick-ref-col">
              <div class="qr-label">Move (1 CP)</div>
              <div class="qr-item">Move up to MOV distance</div>
              <div class="qr-item">Cover → +2 AC vs ranged</div>
              <div class="qr-label" style="margin-top:5px;">Scout (1 CP)</div>
              <div class="qr-item">d20 + PER vs Detection DC</div>
              <div class="qr-item">Success → target Spotted</div>
            </div>
            <div class="quick-ref-col">
              <div class="qr-label">Shoot / Fight (1 CP)</div>
              <div class="qr-item">Target must be Spotted</div>
              <div class="qr-item">d20 + ATK vs target AC</div>
              <div class="qr-item">Hit → roll damage dice</div>
              <div class="qr-item">Miss → no effect</div>
              <div class="qr-item">Cover: +2 AC (ranged only)</div>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div class="section-heading">
          <h2>Example Turn</h2>
          <div class="sub">Ironclad vs Vault · 3 Command Points</div>
        </div>
        <div class="example-box">
          <div class="ex-label">⬤ Ironclad (Crimson Talons) takes her turn</div>
          <div class="ex-step"><strong>CP 1 — Move:</strong> Ironclad moves 5" forward and ducks behind a crate. She is now in cover (+2 AC vs ranged).</div>
          <div class="ex-step"><strong>CP 2 — Scout:</strong> She suspects Vault is lurking 14" away. Rolls d20 + 4 PER = <strong>17</strong> vs DC <strong>13</strong>. Success — Vault is <strong>Spotted</strong>.</div>
          <div class="ex-step"><strong>CP 3 — Shoot:</strong> Ironclad fires her Combat Rifle (+5 ATK, 1d8+2). Rolls d20 + 5 = <strong>19</strong> vs Vault's AC <strong>18</strong>. A hit! Rolls 1d8+2 = <strong>7 damage</strong>. Vault drops from 24 HP to <strong>17 HP</strong>.</div>
          <div class="ex-step" style="border-left-color: #aaa; color: #777;">Turn passes to the Ashborn Syndicate player.</div>
        </div>
      </div>

    </div>
    <div class="page-footer">
      <div class="page-footer-text">Strike Team · Basic Rules</div>
      <div class="page-footer-text">9</div>
    </div>
  </div>
</div>

</body>
</html>
"""

if __name__ == "__main__":
    out_html = "/Users/aga/code/omat/strike-team/rules_booklet.html"
    out_pdf  = "/Users/aga/code/omat/strike-team/rules_booklet.pdf"

    with open(out_html, "w") as f:
        f.write(HTML_CONTENT)

    print("Converting to PDF...")
    HTML(filename=out_html).write_pdf(
        out_pdf,
        stylesheets=[CSS(string="@page { size: A4; margin: 0; }")]
    )
    print(f"Done! → {out_pdf}")
