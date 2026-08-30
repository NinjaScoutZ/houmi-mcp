---
name: plan
description: Spec, Fable5 LEDGER cards, and Editorial SVG architecture diagrams.
---

# /plan — Specification & Architecture

Plan before code. All output goes to `.agents/plans/`.

## Procedure
1. Research the task scope using `houmi_graft_intel(action="skeleton")` and `houmi_route`.
2. Write plan as `### Phase N — Title` in `.agents/plans/*-plan.md`.
3. Generate Editorial SVG diagram: `houmi_diagram(title=..., diagram_type="architecture", components=[...])`.
4. Break plan into LEDGER cards: `houmi_ledger(action="add_card", args={"card_text": "...", "accept_cmd": "npm run build"})`.
5. If backend functions are needed: `houmi_backend_sync(action="record_api", args={"command_name": "...", "purpose": "..."})`.
6. **DO NOT write application source code.** Plan only.
