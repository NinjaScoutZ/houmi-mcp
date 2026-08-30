"""Houmi MCP Core — Auto-Detect Intelligence Kernel.
Unifies:
- Godkiller Hard Proof & Disk Gates
- Fable5 Work Discipline & LEDGER Machine
- Graft Code Graph & Blast Radius
- Cathryn Lavery Editorial Diagram Design
- Houmi Stack Intelligence (React 19, Fabric.js Canvas, Tailwind v4, Tauri v2)
"""

import os
import re
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("houmi-core")

def _get_workspace_root() -> Path:
    env_ws = os.environ.get("HOUMI_WORKSPACE") or os.environ.get("GODKILLER_WORKSPACE")
    if env_ws:
        return Path(env_ws).resolve()
    return Path.cwd().resolve()

def _get_ledger_path() -> Path:
    return _get_workspace_root() / ".agents" / "LEDGER.md"

def _get_backend_spec_path() -> Path:
    return _get_workspace_root() / ".agents" / "backend_requirements.md"

# ==============================================================================
# 1. AUTO-DETECT ROUTER (Intelligent Switchboard)
# ==============================================================================

@mcp.tool()
def houmi_route(intent: str, file_target: Optional[str] = None) -> Dict[str, Any]:
    """Auto-detect intent and recommend the optimal toolchain and mode automatically.
    
    Determines if the task requires:
    - Canvas / Fabric.js handling
    - Backend Tauri IPC synchronization
    - Editorial Diagram generation
    - Stack grilling (Types, Leaks, Tailwind)
    - Graft symbol blast radius analysis
    """
    intent_lower = intent.lower()
    file_lower = (file_target or "").lower()
    
    triggers = []
    mode = "ultradeep"
    
    # 1. Mode Detection
    if any(w in intent_lower for w in ["plan", "spec", "architect", "วางแผน"]):
        mode = "plan"
    elif any(w in intent_lower for w in ["ask", "what", "where", "how", "ค้นหา", "ถาม"]):
        mode = "ask"
    elif any(w in intent_lower for w in ["debug", "bug", "fix", "error", "แก้", "พัง"]):
        mode = "debug"
    elif any(w in intent_lower for w in ["verify", "test", "check", "audit", "ตรวจ", "ย่าง"]):
        mode = "verify"
    elif any(w in intent_lower for w in ["loop", "marathon", "ยาว", "ออโต้"]):
        mode = "loop"

    # 2. Sub-system Auto-Detection
    if "canvas" in intent_lower or "balloon" in intent_lower or "fabric" in intent_lower or "canvas" in file_lower:
        triggers.append({"subsystem": "canvas", "action": "Auto-inspect Fabric.js event cleanup & selection box"})

    if any(w in intent_lower for w in ["backend", "tauri", "ipc", "rust", "api", "endpoint"]):
        triggers.append({"subsystem": "backend_sync", "action": "Auto-record API contract in .agents/backend_requirements.md"})

    if any(w in intent_lower for w in ["diagram", "chart", "flow", "architecture", "ไดอะแกรม"]):
        triggers.append({"subsystem": "diagram", "action": "Generate Editorial SVG/HTML diagram (Cathryn Lavery standard)"})

    if any(w in intent_lower for w in ["refactor", "rename", "delete", "restructure"]):
        triggers.append({"subsystem": "graft_blast_radius", "action": "Auto-check impacted call sites before editing"})

    triggers.append({"subsystem": "stack_grill", "action": "Auto-audit React 19, TypeScript any, and Tailwind design tokens on finish"})

    return {
        "ok": True,
        "recommended_mode": f"/{mode}",
        "detected_triggers": triggers,
        "execution_pipeline": [
            f"1. Activate mode {mode}",
            "2. Read/pop LEDGER card from disk",
            "3. Auto-run required subsystem checks",
            "4. Execute changes in frontend_rework/",
            "5. Auto-grill and close card with verified evidence"
        ]
    }

# ==============================================================================
# 2. EDITORIAL DIAGRAM ENGINE (Cathryn Lavery Design Standard)
# ==============================================================================

@mcp.tool()
def houmi_diagram(title: str, diagram_type: str, components: List[Dict[str, str]], style: str = "dark_obsidian") -> Dict[str, Any]:
    """Generate standalone, editorial-quality SVG/HTML architecture diagrams.
    Avoids ugly Mermaid boxes in favor of clean typography, semantic colors, and spatial layout.
    
    Types: 'architecture', 'flowchart', 'sequence', 'pipeline'
    Styles: 'dark_obsidian' (Amber Gold + Charcoal), 'minimal_light', 'editorial_navy'
    """
    ws = _get_workspace_root()
    diagrams_dir = ws / ".agents" / "diagrams"
    diagrams_dir.mkdir(parents=True, exist_ok=True)
    
    bg_color = "#0B0F17" if "dark" in style else "#F8FAFC"
    card_bg = "#131B2E" if "dark" in style else "#FFFFFF"
    text_color = "#F1F5F9" if "dark" in style else "#0F172A"
    accent_color = "#F59E0B" if "dark" in style else "#2563EB"
    border_color = "#1E293B" if "dark" in style else "#E2E8F0"

    svg_cards = ""
    for idx, comp in enumerate(components):
        x = 50 + (idx % 3) * 260
        y = 90 + (idx // 3) * 160
        c_name = comp.get("name", f"Component {idx+1}")
        c_role = comp.get("role", "")
        c_tech = comp.get("tech", "")
        
        svg_cards += f"""
        <g transform="translate({x}, {y})">
            <rect width="230" height="130" rx="10" fill="{card_bg}" stroke="{border_color}" stroke-width="1.5"/>
            <rect x="0" y="0" width="230" height="6" rx="3" fill="{accent_color}"/>
            <text x="16" y="34" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="15" font-weight="700" fill="{text_color}">{c_name}</text>
            <text x="16" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" fill="#94A3B8">{c_role}</text>
            <rect x="16" y="85" width="198" height="26" rx="4" fill="{bg_color}" stroke="{border_color}" stroke-width="1"/>
            <text x="24" y="102" font-family="monospace" font-size="11" fill="{accent_color}">{c_tech}</text>
        </g>
        """

    svg_content = f"""<svg width="860" height="460" viewBox="0 0 860 460" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    <text x="50" y="50" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="800" fill="{text_color}" letter-spacing="-0.5px">{title}</text>
    <text x="50" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" fill="#64748B">Editorial Architecture Diagram • {diagram_type.upper()}</text>
    {svg_cards}
</svg>"""

    slug = re.sub(r'[^a-zA-Z0-9_-]', '_', title.lower())
    out_file = diagrams_dir / f"{slug}.svg"
    out_file.write_text(svg_content.strip(), encoding="utf-8")
    
    return {
        "ok": True,
        "title": title,
        "path": str(out_file),
        "diagram_type": diagram_type,
        "style": style,
        "svg_snippet": svg_content[:300] + "..."
    }

# ==============================================================================
# 3. LEDGER & PLAN GATE (Fable5 Machine)
# ==============================================================================

@mcp.tool()
def houmi_ledger(action: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Task Ledger State Machine with machine-checkable acceptance tests and evidence-on-close."""
    args = args or {}
    ws = _get_workspace_root()
    (ws / ".agents").mkdir(parents=True, exist_ok=True)
    ledger_file = _get_ledger_path()

    if action == "init":
        if not ledger_file.exists():
            ledger_file.write_text("# HOUMI TASK LEDGER\n\n## Active Round\n- [ ] CARD-01: Core Architecture\n  -- accept: npm run build\n  -- scope: frontend_rework/\n", encoding="utf-8")
        return {"ok": True, "path": str(ledger_file)}

    if action == "pop_card":
        if not ledger_file.exists():
            return {"ok": False, "error": "Ledger missing."}
        content = ledger_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if re.match(r"^-\s*\[\s*\]\s*", line):
                details = [lines[j].strip() for j in range(i+1, min(i+5, len(lines))) if lines[j].startswith("  --")]
                return {"ok": True, "card": line.strip(), "details": details}
        return {"ok": True, "card": None, "message": "All cards complete"}

    if action == "close_card":
        card_id = args.get("card_id", "")
        evidence = args.get("evidence", "").strip()
        if not evidence:
            return {"ok": False, "error": "EVIDENCE_REQUIRED: Must provide concrete test evidence to close a card."}
        content = ledger_file.read_text(encoding="utf-8")
        pattern = re.compile(rf"(-\s*\[\s*\]\s*{re.escape(card_id)}[^\n]*)", re.IGNORECASE)
        match = pattern.search(content)
        if not match:
            return {"ok": False, "error": f"Open card {card_id} not found."}
        updated = content[:match.start()] + match.group(1).replace("[ ]", "[x]") + f"\n  -- evidence: {evidence}" + content[match.end():]
        ledger_file.write_text(updated, encoding="utf-8")
        return {"ok": True, "closed_card": card_id}

    if action == "add_card":
        card_text = args.get("card_text", "").strip()
        accept_cmd = args.get("accept_cmd", "npm run build").strip()
        entry = f"\n- [ ] {card_text}\n  -- accept: {accept_cmd}\n  -- scope: frontend_rework/\n"
        with open(ledger_file, "a", encoding="utf-8") as f:
            f.write(entry)
        return {"ok": True, "added": card_text}

    return {"ok": False, "error": f"Unknown action: {action}"}

# ==============================================================================
# 4. BACKEND & TAURI IPC SYNC
# ==============================================================================

@mcp.tool()
def houmi_backend_sync(action: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Sync backend API / Tauri IPC specifications needed by Frontend."""
    args = args or {}
    spec_file = _get_backend_spec_path()

    if action == "record_api":
        name = args.get("command_name")
        purpose = args.get("purpose", "")
        payload = args.get("payload_schema", {})
        response = args.get("response_schema", {})
        is_tauri = args.get("is_tauri_ipc", True)
        if not name:
            return {"ok": False, "error": "command_name is required."}
        entry = f"\n### `{name}` {'(Tauri IPC)' if is_tauri else '(REST/WS)'}\n**Purpose:** {purpose}\n**Payload:** `{json.dumps(payload)}`\n**Response:** `{json.dumps(response)}`\n---\n"
        with open(spec_file, "a", encoding="utf-8") as f:
            f.write(entry)
        return {"ok": True, "command": name, "recorded_to": str(spec_file)}

    if action == "list_apis":
        if not spec_file.exists():
            return {"ok": True, "commands": []}
        return {"ok": True, "commands": re.findall(r"###\s*`([^`]+)`", spec_file.read_text(encoding="utf-8"))}

    return {"ok": False, "error": f"Unknown action: {action}"}

# ==============================================================================
# 5. STACK GRILLER & AST INSPECTOR
# ==============================================================================

@mcp.tool()
def houmi_stack_grill(target_path: str = "frontend_rework/src") -> Dict[str, Any]:
    """Auto-grill source code for React 19, Type any, Canvas leaks, and Tailwind bypass."""
    ws = _get_workspace_root()
    p = (ws / target_path).resolve()
    if not p.exists():
        return {"ok": False, "error": f"Path not found: {p}"}

    issues = []
    for ext in (".ts", ".tsx", ".js", ".jsx"):
        for f in (p.rglob(f"*{ext}") if p.is_dir() else [p]):
            if "node_modules" in f.parts or "dist" in f.parts:
                continue
            content = f.read_text(encoding="utf-8", errors="ignore")
            lines = content.splitlines()
            rel = str(f.relative_to(ws))
            for idx, line in enumerate(lines, 1):
                if re.search(r":\s*any\b|\bas\s+any\b", line):
                    issues.append({"file": rel, "line": idx, "type": "TYPE_SAFETY", "msg": "Explicit `any` type."})
                if "canvas.on(" in line and not any("dispose" in l or "canvas.off" in l for l in lines):
                    issues.append({"file": rel, "line": idx, "type": "CANVAS_LEAK", "msg": "Fabric.js event listener without off/dispose."})
                    break
                if re.search(r"#[0-9a-fA-F]{3,8}\b", line) and "tailwind.config" not in rel:
                    issues.append({"file": rel, "line": idx, "type": "DESIGN_TOKEN", "msg": "Hardcoded hex color bypassing tokens."})
                if re.search(r"TODO:|mockData|fakeData", line):
                    issues.append({"file": rel, "line": idx, "type": "HOLLOW_CODE", "msg": "Hollow code or mock placeholder."})

    return {"ok": True, "target": str(target_path), "issues_count": len(issues), "passed": len(issues) == 0, "issues": issues[:25]}

# ==============================================================================
# 6. GRAFT CODE GRAPH & BLAST RADIUS
# ==============================================================================

@mcp.tool()
def houmi_graft_intel(action: str, target: str) -> Dict[str, Any]:
    """Graft symbol callers and file API skeletons."""
    ws = _get_workspace_root()

    if action == "skeleton":
        p = (ws / target).resolve()
        if not p.is_file():
            return {"ok": False, "error": f"File not found: {target}"}
        sigs = [l.strip()[:100] for l in p.read_text(encoding="utf-8", errors="ignore").splitlines() if re.match(r"^\s*(export\s+)?(async\s+)?(function|const|class|interface|type)\s+([A-Za-z0-9_]+)", l)]
        return {"ok": True, "file": target, "skeleton": sigs}

    if action == "callers":
        found = []
        for f in (ws / "frontend_rework" / "src").rglob("*.ts*"):
            content = f.read_text(encoding="utf-8", errors="ignore")
            if target in content:
                found.append(str(f.relative_to(ws)))
        return {"ok": True, "symbol": target, "impacted_files": list(set(found))}

    return {"ok": False, "error": f"Unknown action: {action}"}

# ==============================================================================
# 7. WRITE GUARD
# ==============================================================================

_GUARD_PATHS = set()

@mcp.tool()
def houmi_guard(action: str, paths: Optional[List[str]] = None) -> Dict[str, Any]:
    """Write Guard allowlisting."""
    global _GUARD_PATHS
    if action == "set_paths":
        _GUARD_PATHS = set(paths or [])
        return {"ok": True, "allowlisted": list(_GUARD_PATHS)}
    if action == "end_turn":
        _GUARD_PATHS.clear()
        return {"ok": True, "cleared": True}
    return {"ok": True, "active": list(_GUARD_PATHS)}

if __name__ == "__main__":
    mcp.run()
