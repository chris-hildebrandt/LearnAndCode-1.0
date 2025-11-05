# LearnAndCode Reference Pack

## Metadata Schema

All repository artefacts are indexed in `index.json` using the following shape:

```
{
  "id": "<relative path>",
  "week": "<top-level week folder or null>",
  "subcategory": "<immediate child folder or filename>",
  "name": "<base filename>",
  "extension": "<file extension>",
  "content_kind": "text|code|data|unknown",
  "content_subtype": "<language or MIME hint>",
  "size_bytes": <integer>,
  "sha256_16": "<first 16 hex characters of SHA-256 hash>"
}
```

Use the `week` and `subcategory` fields for hierarchical grouping, while `content_kind` and `content_subtype` enable language-aware ingestion.

## Deliverables

- `index.json`: canonical machine-readable inventory with metadata, hashes, and `generated` flags.
- `summaries/file_summaries.json`: file-level abstractions with short/long summaries and basic stats.
- `summaries/week_rollups.json`: tiered aggregation for each curriculum week plus general assets.
- `summaries/chunks.jsonl`: chunked text payloads (≤~2k characters) with metadata for embedding or retrieval pipelines.

## Workflow

1. Index the repository to ensure every asset is catalogued.
2. Generate tiered summaries (file → week → curriculum) with token-aware chunking.
3. Export embedding-ready `.jsonl` slices if vectorisation is required.

Each stage can be re-run independently as new content is added.
