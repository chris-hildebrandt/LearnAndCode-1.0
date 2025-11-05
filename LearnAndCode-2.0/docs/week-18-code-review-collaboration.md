# Week 18 · Code Review & Collaboration

## 1. Learning Objectives
- Perform professional peer reviews using provided checklist.
- Provide actionable, respectful feedback with suggested fixes.
- Respond to review comments on your own PR quickly and thoroughly.

## 2. Preparation (10 min)
- Review Google Engineering Practices “How to do a Code Review”.
- Skim team’s review rubric (linked in cohort wiki).
- Summary: Reviews focus on correctness, readability, tests, and maintainability.

## 3. This Week’s Work
- Review **two** classmates’ Week 17 PRs (or designated practice PRs).
- Leave at least three high-quality comments per PR (nit/praise/question/breakage).
- Respond to all comments on your own Week 17 PR and make necessary updates.

## 4. Files to Modify
- `docs/week-18-code-review-collaboration.md` (fill in Review Log section)
- Code changes only if review feedback uncovers issues in your Week 17 branch.

## 5. Step-by-Step Instructions
1. Branch `week-18/<your-name>` (only for documentation changes).
2. Use `.github/pull_request_template.md` checklist while reviewing peer PRs.
3. Focus comments on behaviour (“This breaks filtering when priority is empty because…”).
4. Provide at least one suggestion comment (`suggestion` block or code snippet).
5. On your PR, respond to every comment within 24 hours—commit fixes as needed.
6. Capture review activity in the Review Log below.
7. If no classmates available, review the provided sample PR in repo (`samples/review-week-18.md`).

## 6. How to Test
- Run tests (`dotnet test TaskFlowAPI.sln`) if you make code changes from review feedback.

## 7. Success Criteria
- Two peer reviews completed with actionable comments.
- All comments on your PR resolved (either code change or explanation).
- Review Log completed with links to PRs.

## 8. Submission Process
- Commit documentation update `Week 18 – review log`.
- PR summary includes links to reviews you performed and confirmation your PR comments resolved.
- Weekly issue attaches screenshot of one review comment thread.

## 9. Discussion Prep
- What makes a comment “high leverage” vs. noise?
- How did you handle disagreement during review?
- What review checklist item caught the most issues?

## 10. Time Estimate
- 10 min – Prep + checklist review.
- 30 min – Review PR #1.
- 30 min – Review PR #2.
- 10 min – Respond to comments on your PR + documentation.
**Total:** ~80 minutes (spread through the week).

## 11. Getting Help
- Ask in chat if you need a review pairing partner.
- Office hours: dry run review session with mentor.
- Escalate to mentor if a review discussion stalls >24 hours.

---

### Review Log (fill before submitting)
- **PRs reviewed (links):**
  1. `________________`
  2. `________________`
- **Top issue caught:** `________________`
- **Feedback requested on my PR:** `________________`
- **Response completed?** `Yes / No`
