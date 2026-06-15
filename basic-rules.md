# 📖 Basic Rules
### Strike Team Skirmish Game

---

## Overview

Two players each control a **Strike Team** of five operants. Players alternate turns, spending **Command Points** to activate their operants and maneuver for position, gather intelligence, and eliminate the enemy.

The goal is to down all enemy operants, or achieve your mission objective before the enemy achieves theirs.

---

## Turn Structure

Players alternate taking turns. On **your turn**, you receive **3 Command Points (CP)**.

Each CP may be spent on one action. You may spend all 3 CP on different actions, or repeat the same action multiple times (e.g., three Moves in a row). **Any unused CP are lost at the end of your turn.**

| CP Cost | Action  | What it does                                      |
|---------|---------|---------------------------------------------------|
| 1       | **Move**  | Move one operant up to their full MOV distance  |
| 1       | **Scout** | One operant attempts to spot a hidden enemy     |
| 1       | **Shoot / Fight** | One operant attacks a visible enemy   |

> **One operant per action.** Each action must be assigned to an operant. The same operant may receive multiple actions in a single turn — but each action costs 1 CP.

---

## Actions

---

### 🏃 MOVE

Choose one operant. Move them up to their full **MOV** distance (in inches) in any direction.

**Rules:**
- Movement may be split: move 3", perform another action, then use a second Move to continue.
- Operants **may not move through** other operants or impassable terrain.
- Moving within **1" of an enemy** operant ends your movement (you are engaged in melee).
- An operant that ends its Move in **cover** (a wall, crate, barricade, etc.) gains **+2 AC** against ranged attacks until they next move.

---

### 🔍 SCOUT

Choose one operant. They attempt to **detect a hidden enemy** — an enemy that has not yet been spotted and therefore **cannot be targeted** by Shoot actions.

> An enemy operant starts **hidden** if they are behind a structure or in obscuring terrain with no line of sight from any of your operants.

**How to Scout:**

1. Declare which enemy operant your operant is scouting for, and the approximate location.
2. Roll **d20 + your operant's PER modifier**.
3. Compare the result to the **Detection DC**, determined by the distance to the target:

| Distance to Target | Detection DC |
|--------------------|--------------|
| 0" – 8"            | 10           |
| 9" – 16"           | 13           |
| 17" – 24"          | 16           |
| 25" – 32"          | 19           |
| 33"+               | 22           |

**Success:** The hidden enemy is **Spotted**. Place a Spotted token on them. They can now be targeted by Shoot and Fight actions for the rest of the game (or until they move behind full cover again and are declared hidden by their controller).

**Failure:** The Scout action is wasted. You may try again next turn with a CP.

> **Line of Sight required:** Your scouting operant must have a clear line to at least part of the structure the target is hiding behind. You cannot scout through solid walls.

---

### 🔫 SHOOT / ⚔️ FIGHT

Choose one operant. They attack a **visible (Spotted) enemy** with one of their weapons.

> An enemy is visible if they are **not hidden**, or have already been **Spotted**.

---

#### Ranged Attack (SHOOT)

1. Choose a ranged weapon and a target within that weapon's **Range**.
2. Roll **d20 + the weapon's Attack Bonus**.
3. If the result equals or exceeds the target's **AC**, the attack **hits**.
4. Roll the weapon's **Damage Dice** and subtract the result from the target's HP.
5. Apply any weapon **Special** effects on a hit.

> **Cover modifier:** If the target is in cover, their AC increases by +2 against this attack.

> **Out of Range:** You may not declare a Shoot action against a target beyond your weapon's listed range.

---

#### Melee Attack (FIGHT)

1. Your operant must be **within 1"** of the target (engaged in melee).
2. Choose your melee weapon.
3. Roll **d20 + the weapon's Attack Bonus**.
4. If the result equals or exceeds the target's **AC**, the attack **hits**.
5. Roll the weapon's **Damage Dice** and subtract the result from the target's HP.
6. Apply any weapon **Special** effects on a hit.

> **Cover does not apply** to melee attacks — it only protects against ranged fire.

---

## Damage & Downed Operants

- When an operant's **HP reaches 0**, they are **Downed** — remove them from the battlefield.
- Downed operants may not take actions, be activated, or block movement.
- There is **no recovery** from being Downed unless a Special Ability explicitly allows it.

---

## Conditions Reference

Conditions are applied by weapons or Special Abilities. They last until the stated duration.

| Condition     | Effect                                                              | Ends When                        |
|---------------|---------------------------------------------------------------------|----------------------------------|
| **Spotted**   | Enemy can be targeted by Shoot and Fight actions                    | Target moves into full cover     |
| **Staggered** | –2 AC                                                               | End of target's next activation  |
| **Pinned**    | –2 to hit on all attacks                                            | End of target's next activation  |
| **Stunned**   | Skip next activation entirely                                       | Start of target's turn after next |
| **Disrupted** | –2 to next attack roll                                              | After next attack roll           |
| **Burning**   | Take 1d4 fire damage at start of next activation                   | After taking the damage          |
| **Poisoned**  | Take 1d4 damage at start of next activation                        | After taking the damage          |
| **Marked**    | Attacker who applied the mark gains +2 to hit and may trigger bonus effects | Until target is Downed  |

---

## Quick Reference

```
YOUR TURN
─────────────────────────────────────────
  Receive 3 Command Points (CP)
  Spend each CP on one action:

  MOVE (1 CP)
  └─ Move one operant up to their MOV

  SCOUT (1 CP)
  └─ Roll d20 + PER vs Detection DC
     (DC set by distance to hidden target)
     Success → target is Spotted

  SHOOT / FIGHT (1 CP)
  └─ Target must be Spotted or visible
     Roll d20 + ATK bonus vs target AC
     Hit → roll damage dice
     Miss → no effect

  Unused CP are lost. Turn passes to opponent.
─────────────────────────────────────────
```

---

## Example Turn

> **Ironclad** (Crimson Talons) takes her turn with 3 CP.

1. **(1 CP — Move):** Ironclad moves 5" forward and ducks behind a crate. She is now in cover (+2 AC vs ranged).

2. **(1 CP — Scout):** Ironclad suspects Vault (Ashborn Syndicate) is lurking behind a building 14" away. She rolls **d20 + 4 PER = 17**. The Detection DC for 14" is **13**. She beats it — Vault is **Spotted**.

3. **(1 CP — Shoot):** Ironclad targets Vault with her Combat Rifle (Range 24", +5 ATK, 1d8+2 damage). She rolls **d20 + 5 = 19**. Vault's AC is **18**. A hit! She rolls **1d8 + 2 = 7 damage**. Vault drops from 24 HP to **17 HP**.

> Turn passes to the Ashborn Syndicate player.
