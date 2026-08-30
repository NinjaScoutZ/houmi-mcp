---
name: verify
description: Run stack griller, build diagnostics, and close LEDGER card with disk evidence.
---

# /verify — Proof & Close

Verify work is complete with machine-checkable evidence.

1. Run stack grill: `houmi_stack_grill(target_path="frontend_rework/src")`.
2. Run build: execute `cd frontend_rework && npm run build` and check exit code.
3. Close card with evidence: `houmi_ledger(action="close_card", args={"card_id": "...", "evidence": "build clean, grill 0 issues"})`.
4. If issues found → do NOT close. Fix first or add new LEDGER card.
