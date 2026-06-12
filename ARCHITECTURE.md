# Architecture

## High-Level Flow

```text
GitLab MR / selected MR
        ↓
Orbit Adapter
        ↓
LynkMesh Adapter
        ↓
Guardrail Engine
        ↓
Briefing Renderer
        ↓
GitLab MR Adapter / local markdown output
```

## Components

### Orbit Adapter

Provides GitLab Orbit-style project context: changed files, known entities, symbols, and known layers.

The current implementation uses JSON fixtures. Later, this adapter should be replaced by GitLab Orbit API, CLI, or skill interface integration.

### LynkMesh Adapter

Provides graph-backed context: changed nodes, new dependency edges, expected edges, and blast radius.

The current implementation uses JSON fixtures that mimic a LynkMesh context pack. Later, this can call LynkMesh CLI/MCP/API or consume generated context pack artifacts.

### Guardrail Engine

Evaluates deterministic architecture rules.

MVP rule:

```text
layering.controller_to_model_bypass
```

Expected:

```text
Controller → Service → Model
```

Violation:

```text
Controller → Model
```

### Briefing Renderer

Turns guardrail results into a reviewer-ready Merge Request comment.

### Evidence Log

Each run emits a JSON log with run ID, mode, context IDs, evaluated rules, violations, blast radius count, and output path.
