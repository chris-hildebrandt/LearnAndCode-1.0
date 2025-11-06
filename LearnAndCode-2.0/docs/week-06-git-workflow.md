# Week 6 · Git Workflow & Collaboration

## 1. Learning Objectives
- Execute feature branch workflow (branch → commit → PR → review).
- Write meaningful commit messages tied to small scopes.
- Practice review feedback loop by responding to comments.

## 2. Reading & Resources (45 min)
- **Clean Code Chapters 2-4 (recap)** – Revisit naming and function guidance to keep commits focused.
- **Git Documentation** – Skim basics or commands you rarely use.
- **Atlassian Git Tutorials** – Review branching/merging best practices.
- **Learn Git Branching** (interactive) – Complete the basic track to reinforce branching mental models.
- **YouTube: Tools & Concepts for Mastering Version Control with Git** (optional, 15 min) – Quick video primer.
- Optional deep dive: **Pro Git** (selected chapters) & **Git for Professionals** article once basics are solid.

## 3. This Week’s Work
- Simulate a mini feature: add “priority filtering” placeholder to TaskFlow API.
- Create at least two commits: implementation + documentation update.
- Open a PR against your fork and request mentor review.

## 4. Files to Modify
- `TaskFlowAPI/Controllers/TasksController.cs` (add TODO comment stub for upcoming filter work).
- `docs/week-06-git-workflow.md` (fill in Review Notes section).
- Optional: update `TaskFlowAPI.http` with a sample query parameter.

## 5. Step-by-Step Instructions
1. Branch `week-06/<your-name>`.
2. Add a comment in `TasksController` describing future priority filter (`// TODO Week 12: support ?priority=`) and ensure naming matches new conventions.
3. Update `TaskFlowAPI.http` with a GET example using `?priority=High`.
4. Commit #1 `chore: document upcoming priority filter`.
5. Create a markdown note in this file under “Review Notes” about what kind of feedback you expect.
6. Commit #2 `docs: capture Git workflow notes`.
7. Push branch, open PR, and add your mentor as reviewer.
8. Share PR link in chat; ask for at least one comment.
9. Respond to review comment (or add a self-review comment if no feedback within 24h). No merge yet.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```

## 7. Success Criteria
- Two commits with meaningful messages.
- PR open with reviewer assigned and comment addressed.
- Review Notes section completed.
- Build/tests green.

## 8. Submission Process
- Link the open PR (even if not merged) in your weekly issue.
- Include screenshot of review comment + response.

## 9. Journal and Discussion Prep
Journal:
*Commit Hygiene:* What criteria did you use to decide a commit was “complete”? Capture one example.

*Review Expectations:* What type of feedback are you hoping to receive on this PR, and why?

Discussion Prep:
- What made your commits small and reviewable?
- How did you handle feedback or lack thereof?
- What automation could enforce this workflow?
- Where would advanced Git features (rebase, cherry-pick) help future branches?

## 10. Time Estimate
- 10 min – Plan Git workflow.
- 25 min – Implement placeholder + commits.
- 15 min – PR + review response.
**Total:** ~50 minutes.

## 11. Getting Help
- Ask mentor for reviewer pairing if unsure who to request.
- Attend office hours with your PR link for live review practice.
- Use team chat for Git troubleshooting.

---

### Review Notes (fill in before submitting)
- **Reviewer requested:** `________________`
- **Feedback received?** `Yes / No`
- **How you responded:** `________________`
