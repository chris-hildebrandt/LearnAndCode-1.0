# Week 18 · Code Smells & Refactoring

## 1. Learning Objectives
- Identify common smells (long method, duplicate code, shotgun surgery, etc.).
- Apply targeted refactorings without changing behaviour.
- Document before/after impact for peer review.

## 2. Reading (45 min)
- **Clean Code Chapter 17: Smells and Heuristics.**
- **Refactoring Guru: Code Smells** – Catalogue of common smells and refactors.
- **Clean Code Smells and Heuristics** – Quick reference checklist.
- **YouTube: Why Code with Code Smells is Harder to Understand** (optional, 10 min).
- **YouTube: Code Refactoring – Learn Code Smells** (optional, 15 min).

## 3. This Week’s Work
- Find at least **three** distinct smells in TaskFlow API (code or tests).
- Refactor each smell using appropriate technique (extract method/class, replace conditional, parameter object, etc.).
- Document each change in PR description with “smell → refactor → result”.

## 4. Files to Modify
- Any production or test file containing the smell.
- Update documentation or TODO comments if necessary.

## 5. Step-by-Step Instructions
1. Branch `week-18/<your-name>`.
2. Scan recent code (controllers, services, filters, validators, tests) for smells.
3. For each smell:
   - Capture snippet before change (paste into PR description later).
   - Refactor carefully, running tests after each change.
   - Ensure naming/structure aligns with earlier clean-code practices.
4. Optional: add regression tests if refactor needed better coverage.
5. Run full build/tests at the end.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```

## 7. Success Criteria
- At least three smells removed; each clearly described in PR.
- Behaviour unchanged (tests pass).
- No new smells introduced (e.g., giant helpers).

## 8. Submission Process
- Commit `Week 18 – smell cleanup` (use multiple commits if helpful, e.g., one per smell).
- PR summary includes table:
  | Smell | Location | Refactoring | Outcome |
- Weekly issue references same table + lessons learned.

## 9. Journal and Discussion Prep
Journal:
*Smell Catalog:* Log the three smells you targeted and the refactor applied.

*Regression Safeguards:* Note which tests or checks gave you confidence behaviour stayed the same.

Discussion Prep:
- Which smell surprised you most?
- How did you ensure behaviour stayed the same?
- What tooling helped you locate smells?
- Where do you still see opportunities for future refactors?

## 10. Time Estimate
- 10 min – Identify smells.
- 40 min – Refactor (approx. 3x ~13 min each).
- 10 min – Tests + documentation.
**Total:** ~60 minutes.

## 11. Getting Help
- Share suspected smell snippets in chat for feedback.
- Office hours: pair refactor review session.
- Mentor escalation if tests fail post-refactor and you need debugging support.
