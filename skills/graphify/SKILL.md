---
name: graphify
description: Map a source tree, or query an existing graphify-out/graph.json, only when the operator asks for a code graph. A single code lookup stays a search.
---

# Graphify

Use this only when the operator asks to map a codebase or to query a graph that already exists. One symbol, call site, or file stays a search of the source.

## Extract

Code only. The local AST pass needs no API key:

```bash
graphify extract <path> --code-only --out /tmp/graphify-<name>
```

That writes `/tmp/graphify-<name>/graphify-out/`. Leave the output untracked and do not commit it. To rebuild code that is already graphed, run `graphify update <path>`.

Keep the extract path narrow. Leave out `.env`, credentials, `data/`, paper books, cloud bot transcripts, and `prompts/`.

## Query

```bash
graphify query "<question>" --graph <path>/graphify-out/graph.json
graphify explain "<symbol>" --graph <path>/graphify-out/graph.json
graphify path "<A>" "<B>" --graph <path>/graphify-out/graph.json
```

Treat an edge marked INFERRED as unverified until the source file confirms it.

## Leave alone

Do not run `graphify install`, `graphify hook install`, `graphify claude install`, `graphify codex install`, `--watch`, `graphify-mcp`, cloud sync, `--global`, a database push, or URL ingest unless the operator asks. Do not edit AGENTS.md or CLAUDE.md. Do not send docs, PDFs, images, or video through the semantic model pass.
