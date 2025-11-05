# Week 23 · Final Polish & Presentation

## 1. Learning Objectives
- Deliver production-ready artifacts (code, docs, tests, demo).
- Produce clear written and video documentation for stakeholders.
- Reflect on end-to-end learning and identify next steps.

## 2. Preparation & Reading (45 min)
- Review README, weekly docs, and ensure terminology is consistent (23-week references, TaskFlow naming).
- **Technical Documentation Best Practices** – Write the Docs guide.
- **The Art of Writing Good Documentation** – Practical tips for clarity.
- **Markdown Cheat Sheet** – Quick formatting reference.
- Optional videos: Beth Aitman’s talks on effective documentation.
- Skim final checklist below before starting.

## 3. This Week’s Work
- Polish codebase: remove unused TODOs, ensure comments explain “why,” not “what.”
- Finalise documentation: update README quick start, architecture overview, diagrams if needed.
- Ensure tests cover final features and run green.
- Record 5-minute demo video: overview, key features, design decisions, next steps.
- Prepare final retro notes.

## 4. Files to Modify
- `README.md`
- `docs/` (update any stale information, add appendix if necessary)
- `WEEKLY_PROGRESS.md` (ensure all boxes checked)
- Additional docs: `docs/final-retro.md` (create)

## 5. Step-by-Step Instructions
1. Branch `week-23/<your-name>`.
2. Run `dotnet build` and `dotnet test`—fix any lingering warnings.
3. Review code for lingering smells or TODOs and clean up.
4. Update README with:
   - Architecture diagram or bullet list
   - Setup verification steps (validated)
   - API endpoint summary (link to Swagger)
5. Create `docs/final-retro.md` capturing:
   - Biggest growth areas
   - Remaining technical debt
   - Next steps plan (learning goals)
6. Record demo video (Loom/Teams) walking through API in <5 min. Include link in README + final retro.
7. Ensure `WEEKLY_PROGRESS.md` all checked; include total time spent.
8. Submit final PR and final weekly issue.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Optional: run integration smoke tests via Swagger or Postman collection.

## 7. Success Criteria
- README is production-ready and up to date.
- All docs reference 23-week program accurately.
- Demo video link accessible and under 5 minutes.
- Tests pass; no warnings/errors on build.
- Final retro completed.

## 8. Submission Process
- Commit `Week 23 – final polish`.
- PR summary includes demo video link and highlights final changes.
- Weekly issue attaches final retro and test/build output.
- Notify mentor in chat that final PR is ready for graduation review.

## 9. Journal and Discussion Prep
Journal:
*Polish Checklist:* Record outstanding TODOs you cleared and why they mattered most.

*Demo Narrative:* Outline the story arc for your 5-minute demo (problem, solution, impact).

Discussion Prep:
- What part of TaskFlow API are you most proud of and why?
- Where would you invest next if given two more weeks?
- How did Clean Code principles change your default coding habits?
- What risks remain for production readiness and how will you communicate them?

## 10. Time Estimate
- 20 min – Build/test cleanup.
- 30 min – Documentation + retro.
- 30 min – Record/demo + upload.
**Total:** ~80 minutes.

## 11. Getting Help
- Ask in chat for README review or demo feedback.
- Office hours: reserve slot for practice presentation.
- Mentor escalation for final review scheduling or sign-off questions.
