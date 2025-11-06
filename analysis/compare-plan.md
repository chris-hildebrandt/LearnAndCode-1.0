## Curriculum Comparison Plan

### Purpose
- Establish a repeatable framework to compare `LearnAndCode-1.0` (legacy) and `LearnAndCode-2.0` (TaskFlow API) curricula.
- Optimize memory and context management by chunking materials into consistently scoped units with stable identifiers.
- Produce reference indexes that enable detail-oriented, file-level and concept-level crosswalks without re-reading entire repositories.

### Scope & Guardrails
- Treat everything under `/workspace` except `LearnAndCode-2.0/` as the **1.0 curriculum**. Explicitly exclude the nested `LearnAndCode-2.0/` directory when cataloging 1.0 to avoid duplication.
- Treat the entire `LearnAndCode-2.0/` tree (docs + TaskFlow API solution + supplemental PDFs) as the **2.0 curriculum**.
- Capture supplemental artefacts (PDFs, project files, scripts) because they influence learning outcomes.

### Chunking Strategy

**Shared Rules**
- Chunks map to the smallest unit that must be referenced during comparison (generally a file or cohesive section inside very large files).
- Use stable chunk identifiers combining curriculum version, thematic area, and sequence. Format: `L{version}-{area}-{sequence}`.
- Record metadata: path, chunk title, type (overview, exercise, code, policy, etc.), short summary, keywords.

**1.0 Curriculum (`L1-*`)**
- Area Codes:
  - `WK` – Weekly materials (Weeks 01–27).
  - `GEN` – Root-level guides (e.g., `README.md`).
- Weekly Chunk Template (per week):
  - `L1-WK{##}-OV` – `overview` markdown.
  - `L1-WK{##}-EX` – example/readme/code artefacts.
  - `L1-WK{##}-AS` – assignments or activity subfolders (use sequence suffix `-a`, `-b` if multiple).
- Handle large example files (e.g., `Week 08 Composition`, `.cs.txt` submissions) by splitting into logical subsections if >400 lines or multiple concepts, appending `/p1`, `/p2` as needed.

**2.0 Curriculum (`L2-*`)**
- Area Codes:
  - `DOC` – Weekly curriculum docs inside `docs/`.
  - `API` – TaskFlow API application source.
  - `SUP` – Supplemental resources (PDFs, `SETUP.md`, `WEEKLY_PROGRESS.md`, etc.).
- Weekly docs: `L2-DOC-W{##}` numbering follows file prefix (01–21). Subsections within long docs use anchors `-sec1`, `-sec2` when sections differ materially (e.g., instructions vs. journal prompts).
- TaskFlow API code:
  - Level 1 chunk per bounded context folder (e.g., `L2-API-CTRL`, `L2-API-SVC`).
  - Level 2 chunk per file for focused comparisons (e.g., `L2-API-CTRL-TasksController`).
  - Capture intentional smells/TODOs in the summary metadata for future analysis.

### Index Artefacts to Produce
- `analysis/indexes/learnandcode-1.0-index.md`
  - Table listing all `L1-*` chunks, sorted by week then resource type.
  - Columns: `Chunk ID`, `Path`, `Type`, `Focus`, `Key Links/Dependencies`.
- `analysis/indexes/learnandcode-2.0-index.md`
  - Table covering `docs/` weeks, supplemental files, and TaskFlow API project-level chunks.
- `analysis/indexes/taskflow-api-index.md`
  - Nested list or table drilling into `L2-API-*` chunks with notes on design patterns, validations, tests.
- For any chunk that requires sub-chunking, add anchor references (e.g., `L2-DOC-W05-sec3`) directly within the index file to maintain a single source of truth.

### Workflow for Building References
1. Generate raw inventory (done) for 1.0 excluding `LearnAndCode-2.0` and for 2.0.
2. Populate the index markdown files using the chunk templates above, cross-checking titles and key objectives inside each file.
3. Highlight missing or non-standard assets (e.g., plain-text submissions) in a "Notes" column for potential normalization.
4. After indexes are complete, cross-link equivalent topics between versions (e.g., `L1-WK02-OV` ↔︎ `L2-DOC-W02`) in a separate comparison matrix (to be built in the next phase).

### Quality Controls
- Validate that every 1.0 week (01–27) has at least one chunk entry. If a week lacks supplemental materials in 2.0, record an explicit `GAP` note.
- Confirm that chunk IDs remain unique; run `rg 'L[12]-' analysis/indexes` later to verify duplicates.
- Store future comparison notes in `analysis/comparison-notes.md` (TBD) to keep the plan immutable once executed.

### Next Steps After Index Creation
- Build a topic alignment matrix comparing 1.0 vs 2.0 chunk IDs.
- Identify content gaps (removed, new, or significantly altered topics).
- Verify supplemental readings restored in 2.0 by matching `SUP` chunks against 1.0 references.

