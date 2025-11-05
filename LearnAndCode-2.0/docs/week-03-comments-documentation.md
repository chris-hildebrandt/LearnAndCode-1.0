# Week 3 · Comments & Documentation (Clean Code Ch. 4)

## 1. Learning Objectives
- Audit existing comments and documentation for clarity and necessity.
- Replace redundant comments with expressive names introduced in Week 2.
- Capture intent through README/journal updates when code alone cannot.

## 2. Reading (35 min)
- **Clean Code – Chapter 4: Comments (pp. 59-76).**
  - Focus on “explain yourself in code,” good vs. bad comments, and warning comments.
- **In Time Tec Quality Manifesto – Documentation sections.**
  - Revisit expectations for professional communication.
- **Optional:** *Clean Code Functions* refresher (10 min) to ensure comment deletions are backed by naming improvements.

## 3. This Week’s Work
- Review `TasksController`, `ITaskService`, and `TaskService` for lingering comments and XML docs.
- Delete comments that repeat what the code now communicates; rewrite ones that capture intent or trade-offs.
- Add/upsert doc comments only where the reader cannot deduce intent (e.g., public API contracts, exceptional behaviour).
- Update `README.md` “What You Will Ship” section with one paragraph summarising the documentation mindset (optional stretch).

## 4. Files to Modify
- `TaskFlowAPI/Controllers/TasksController.cs`
- `TaskFlowAPI/Services/Interfaces/ITaskService.cs`
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `README.md` (if you add the optional summary)

## 5. Step-by-Step Instructions
1. Branch `week-03/<your-name>`.
2. Skim the targeted files and list every comment/XML doc.
3. For each comment decide: delete, reword to communicate intent, or move content into code (rename method, extract variable, etc.).
4. Add “why” comments where side effects, performance workarounds, or partner-facing constraints are not obvious.
5. Run `dotnet build TaskFlowAPI.sln` to ensure no removed XML docs were required for compiler directives.
6. Update README (optional) with a short note on documentation principles adopted this week.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Optional: run `dotnet format --verify-no-changes` to ensure no whitespace regressions after deletions.

## 7. Success Criteria
- Every remaining comment explains intent, warns of side effects, or references an external constraint.
- No TODOs or redundant “what the code does” comments linger in the targeted files.
- Build/tests succeed with no new warnings.

## 8. Submission Process
1. Commit `Week 03 – comments and documentation cleanup`.
2. PR summary lists count of removed vs. rewritten comments and any README additions.
3. Weekly submission issue links to PR and highlights one before/after example.

## 9. Journal and Discussion Prep
Journal:
*Comment Debt:	Which comment deletions felt risky, and how did you mitigate the loss of context?

*Documentation Mindset:	Capture one scenario where written documentation (README, journal, ticket) communicates intent better than inline comments.

Discussion Prep:
- Share an example where you transformed a noisy comment into expressive code.
- When are warning comments acceptable in production code?
- How will you keep documentation updated as the TaskFlow API changes?
- Which areas still need better naming before more comments can be removed?

## 10. Time Estimate
- 35 min – Reading & comment inventory.
- 25 min – Code/document updates.
- 15 min – Testing + PR/issue.
**Total:** ~75 minutes.

## 11. Getting Help
- Ask for feedback on tricky warning comments in team chat.
- Office hours: review README/documentation updates.
- Mentor escalation if removing a comment exposes confusing legacy logic.
