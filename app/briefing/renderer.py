from __future__ import annotations

from typing import Any

from app.guardrails.engine import Violation


def render_mr_briefing(
    orbit_context: dict[str, Any],
    lynkmesh_context: dict[str, Any],
    violations: list[Violation],
) -> str:
    changed_files = orbit_context.get("changed_files", [])
    blast_radius = lynkmesh_context.get("blast_radius", [])
    context_pack_id = lynkmesh_context.get("context_pack_id", "unknown")

    lines: list[str] = []
    lines.append("## 🛡️ Orbit Guardrail Briefing (powered by LynkMesh)")
    lines.append("")
    lines.append(f"This MR changes {len(changed_files)} architecture-sensitive file(s):")
    lines.append("")
    for changed in changed_files:
        lines.append(f"- `{changed.get('path', 'unknown')}`")
    lines.append("")

    if violations:
        lines.append("### ⚠️ Architecture Guardrail Violation")
        lines.append("")
        for violation in violations:
            lines.append(f"**Rule:** `{violation.rule_id}`")
            lines.append(f"**Violation:** Direct Model access detected from `{violation.source}` to `{violation.target}`.")
            lines.append("")
            lines.append(f"**Expected flow:** {violation.expected_flow}")
            lines.append(f"**Detected flow:** {violation.detected_flow}")
            lines.append("")
            lines.append(f"{violation.reason}")
            lines.append("")
    else:
        lines.append("### ✅ No MVP Guardrail Violation Detected")
        lines.append("")
        lines.append("No controller-to-model bypass was detected by the current MVP rule.")
        lines.append("")

    lines.append("### 📊 Repo-Wide Blast Radius")
    lines.append("")
    if blast_radius:
        lines.append("LynkMesh context indicates this change may affect:")
        lines.append("")
        for item in blast_radius:
            lines.append(f"- `{item.get('symbol', 'unknown')}` — {item.get('reason', 'No reason provided')}")
    else:
        lines.append("No blast-radius entries were provided by the context pack.")
    lines.append("")

    lines.append("### 🧪 Suggested Test Coverage")
    lines.append("")
    lines.append("- [ ] Invoice creation integration test")
    lines.append("- [ ] Billing regression test")
    lines.append("- [ ] Monthly invoice report export test")
    lines.append("")

    lines.append("### ✅ Reviewer Checklist")
    lines.append("")
    lines.append("- [ ] Confirm whether controller should delegate to `InvoiceService`")
    lines.append("- [ ] Check that invoice creation still triggers billing sync")
    lines.append("- [ ] Verify monthly report output after the change")
    lines.append("")

    lines.append("**Context evidence:**")
    lines.append("")
    lines.append("- Orbit source: MR changed files + code context")
    lines.append(f"- LynkMesh context pack: `{context_pack_id}`")
    lines.append("")
    return "\n".join(lines)
