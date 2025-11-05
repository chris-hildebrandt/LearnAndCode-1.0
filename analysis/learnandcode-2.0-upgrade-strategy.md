## LearnAndCode 2.0 Upgrade Strategy

### Objectives
- Reintroduce AI prompt-engineering content (from 1.0 Week 3) into the 2.0 curriculum.
- Split current Week 3 (Functions & Comments) into two focused weeks (Comments then Functions) to align scope with realistic reading times.
- Expand the program from 21 to 23 weeks and update every cross-reference (docs, README, progress trackers, TaskFlowAPI TODO comments, tests, indexes).
- Restore supplemental reading lists from 1.0 in the 2.0 format.
- Extend enhanced journal/discussion prompts (Weeks 1–3 complete) across the remaining weeks.

### High-Level Timeline Adjustments
| New Week # | Source Content | Notes |
| --- | --- | --- |
| Week 1 | 2.0 Week 1 | No change. |
| Week 2 | 2.0 Week 2 | No change. |
| Week 3 | **Comments & Documentation** (split from old Week 3) | Focus on comment hygiene; adjust readings/time estimates. |
| Week 4 | **Functions** (remaining portion of old Week 3) | Re-evaluate readings (Clean Code Ch. 3) and assignments. |
| Week 5 | **AI Tools & Prompt Engineering** (from 1.0 Week 3) | Migrate readings/tasks; align with TaskFlow usage guidelines. |
| Weeks 6–23 | Old Weeks 4–21 shifted +2 | Update numerals and names accordingly. |

### Phase 0 · Preparation
1. Create working branch.
2. Snapshot current indexes (`learnandcode-2.0-index.md`, etc.) for diff comparison after updates.
3. Export mapping of all `Week` references using ripgrep (`rg "Week [0-9]+" -g"*"`).

### Phase 1 · Curriculum Restructure
1. **Docs Folder Reshuffle**
   - Rename `docs/week-03-functions-comments.md` → `docs/week-03-comments-documentation.md` (comments section only).
   - Create new `docs/week-04-functions.md` (port remaining functions content + adjust readings/time).
   - Create `docs/week-05-ai-tools.md` based on 1.0 Week 3 (adapt structure to 2.0 template: objectives, reading, work, testing, submission, journal/discussion).
   - Shift existing files (`week-04-git-workflow.md` → `week-06-git-workflow.md`, etc.) or duplicate and adjust numbering. Decide between renaming vs adding new copies:
     - Preferred approach: rename files to preserve history using `git mv docs/week-0X-*.md docs/week-0Y-*.md` following new indices.
     - Update front-matter titles (`# Week NN · ...`).
2. **Update References**
   - `README.md` course structure list → reflect 23 weeks.
   - `WEEKLY_PROGRESS.md` → extend to 23 checkboxes.
   - `SETUP.md` or other docs referencing week counts.
   - `.github` templates if referencing week numbers (search `rg "Week [0-9]+" .github`).
3. **TaskFlowAPI TODO Comments**
   - Map old → new week numbers (shift +2 for weeks ≥4).
   - Use regex replacement (e.g., `Week 7` → `Week 9`) across `.cs` files.
   - Verify for both comments and XML docs.
4. **Indexes & Analysis**
   - Update `analysis/indexes/learnandcode-2.0-index.md` and `taskflow-api-index.md` to new chunk IDs (e.g., `L2-DOC-W05` now AI module).
   - Re-run duplicate check afterwards.
5. **WEEKLY_PROGRESS**
   - Align row labels with new week names.
6. **Solution / Tests**
   - Adjust any test placeholder comments referencing weeks (e.g., `TaskServiceTests.Example.cs`).

### Phase 2 · Supplemental Reading Migration
1. Use `analysis/indexes/learnandcode-1.0-index.md` to extract reading lists per week.
2. For each new 2.0 week, ensure `## 2. Reading` mirrors 1.0 references while retaining 2.0 additions.
3. For condensed weeks, distribute readings logically (e.g., Clean Code Ch.6 references appear in Week 7/8).
4. Update time estimates to reflect realistic reading durations (e.g., 45–60 min per Clean Code chapter) and adjust total time.
5. Maintain consistent formatting (bullet list with bolded titles + links).

### Phase 3 · Discussion & Journal Enhancements
1. Review 1.0 `overview-wkX.md` discussion topics for Weeks 4–27.
2. Adapt relevant prompts into 2.0 `Journal and Discussion Prep` sections, matching style used in Weeks 1–3.
3. Ensure each week has 3–5 journal questions and 4–6 discussion prompts tied to TaskFlow work.
4. Update `docs/final-retro-template.md` if referencing specific week counts.

### Validation Plan
- **Automated Searches:**
  - `rg "Week 2[1-9]" LearnAndCode-2.0/docs` to confirm renumbering beyond Week 20.
  - `rg "Week 2" LearnAndCode-2.0/TaskFlowAPI` to ensure TODO comments updated.
  - `rg "21-week" -g"*"` to replace with `23-week` references.
- **Manual Checks:**
  - Confirm `TaskFlowAPI/http` examples align with updated week instructions.
  - Open Swagger instructions in new week docs to verify step alignment.
  - Spot-check `WEEKLY_PROGRESS.md` and README for off-by-one errors.
- **Regression Diffs:**
  - Use `git status` to verify all intended files touched.
  - Re-run `dotnet build` / `dotnet test` to ensure comments or instructions didn’t introduce code issues (should be no code change aside from comments).

### Risk Mitigation
- Perform renaming in stages to avoid broken links: rename files first, then update references.
- Maintain a mapping table (CSV or markdown) to cross-check old vs new week numbers during edits.
- Commit history with logical chunks (Phase 1 restructure, Phase 2 supplements, etc.) for easier review.
- After renumbering, regenerate indexes (`analysis/indexes/...`) to keep them authoritative.

