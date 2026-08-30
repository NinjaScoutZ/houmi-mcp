# ⚡ Houmi MCP & Skills Suite

> **Autonomous Software Engineering Kernel & High-Craft Design System for Antigravity & Claude Code.**

Houmi MCP synthesizes four frontier AI-agent engineering disciplines into a unified, zero-bloat MCP server and slash-command suite:

1. **👑 Fable5 Work Discipline (`fable5-mode`):** Plan-gate (`SPEC.md` + `LEDGER.md`), small-card execution, machine-checkable acceptance criteria, and mandatory evidence-on-close.
2. **🛡️ Godkiller Hard Proof (`godkiller`):** Gates on disk beat chat, zero tolerance for hollow code (stubs/TODOs/mocks), and phase write-guard allowlists.
3. **🌱 Graft Code Graph Intelligence (`Graft`):** Fast symbol callers, impact radius analysis, and file API skeletons in < 200 tokens.
4. **🎨 Editorial Diagram Design (`diagram-design`):** Generates publication-ready standalone SVG architecture diagrams (Dark Obsidian theme) instead of generic Mermaid boxes.

---

## 🎛️ Architecture & Core MCP Tools

The `houmi-core` MCP server exposes 7 focused tools:

```text
┌──────────────────────────────────────────────────────────────────────────┐
│                          houmi-core MCP (7 tools)                        │
├──────────────────────────────────────────────────────────────────────────┤
│  🧭 houmi_route          Auto-detect intent → mode + subsystem triggers  │
│  📋 houmi_ledger         Fable5 task cards on disk (.agents/LEDGER.md)   │
│  🔗 houmi_backend_sync   Backend API / Tauri IPC contract manager        │
│  🔥 houmi_stack_grill    React 19 / Fabric.js / TypeScript / Token audit │
│  🌳 houmi_graft_intel    Symbol callers (blast radius) | file skeleton   │
│  🎨 houmi_diagram        Editorial SVG diagrams (Dark Obsidian style)    │
│  🛡️ houmi_guard          Write-guard path allowlisting per phase         │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Slash Commands

| Command | Mode | Purpose |
|---|---|---|
| **`/houmi`** | 🧠 Master Auto-Detect | Single entry point: auto-routes Canvas, Backend sync, Diagrams, and Grilling |
| **`/loop`** | 🔄 Marathon Loop | Continuous 6–8 hour autonomous cycle with self-grilling and auto-wake |
| **`/plan`** | 📐 Plan & Spec | Phased plan, Editorial SVG diagram, Fable5 LEDGER cards |
| **`/ask`** | 🔍 Read-Only Explore | Graft symbol search and API skeleton (< 200 tokens) |
| **`/debug`** | 🐛 Diagnosis | Hypothesis → blast radius → minimal fix → stack verify |
| **`/ultradeep`** | ⚡ 1-Phase Execution | Single card execution with write-guard |
| **`/view`** | 👁️ Deep Architecture | Architecture study and editorial system diagrams |
| **`/verify`** | ✅ Evidence Gate | Machine-checkable build test and LEDGER close |
| **`/jury`** | 🏛️ Final Audit | Pre-release compliance check |

---

## 📦 Quickstart & Installation

### Option 1 — One-Line PowerShell (Windows)
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

### Option 2 — One-Line Bash (Linux / macOS)
```bash
bash ./scripts/install.sh
```

### Option 3 — Manual Setup
```bash
# 1. Install package in editable mode
pip install -e .

# 2. Add to your mcp_config.json (e.g. ~/.gemini/antigravity/mcp_config.json):
{
  "mcpServers": {
    "houmi-core": {
      "command": "houmi-mcp"
    }
  }
}

# 3. Copy skills to your global or project skills directory:
cp -r skills/* ~/.agents/skills/
```

---

## 📄 License
MIT © [NinjaScoutZ](https://github.com/NinjaScoutZ)
