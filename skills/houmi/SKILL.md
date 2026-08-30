---
name: houmi
description: Master Houmi Auto-Detect Intelligence (Auto-routes Canvas, Backend Sync, Editorial Diagrams, Stack Grilling, and Marathon Loop).
---

# Houmi — Master Auto-Detect (`/houmi`)

Single entry-point. Detects what the task needs and activates the right subsystems automatically.

## Auto-Detect Pipeline
1. Call `houmi_route(intent="<user request>")` to classify mode and subsystems.
2. If Canvas/Fabric.js is involved → auto-inspect event listeners & dispose cleanup.
3. If Backend/Tauri IPC is mentioned → auto-record contract to `.agents/backend_requirements.md`.
4. If architecture diagram is needed → generate Editorial SVG via `houmi_diagram` (not Mermaid).
5. If refactor/rename → auto-check blast radius via `houmi_graft_intel.callers`.
6. Always auto-grill on finish via `houmi_stack_grill`.

## MCP Tool Reference
All tools live on `ServerName="houmi-core"`:

| Tool | Purpose |
|---|---|
| `houmi_route` | Auto-detect intent → recommended mode & subsystem triggers |
| `houmi_ledger` | Fable5 task cards: init, pop_card, add_card, close_card (evidence required) |
| `houmi_backend_sync` | Record/list Tauri IPC & REST API contracts |
| `houmi_stack_grill` | Scan for Type any, Canvas leaks, hardcoded colors, hollow code |
| `houmi_graft_intel` | Symbol callers (blast radius) and file skeleton (API at a glance) |
| `houmi_diagram` | Editorial SVG architecture diagrams (Dark Obsidian / Minimal Light) |
| `houmi_guard` | Write-guard path allowlisting per phase |
