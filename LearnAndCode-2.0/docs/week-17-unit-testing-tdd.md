# Week 17 · Unit Testing & TDD (Clean Code Ch. 9)

## 1. Learning Objectives
- Write focused unit tests using Arrange-Act-Assert pattern.
- Practice TDD for a new feature (`CompleteTaskAsync`).
- Achieve ≥80% coverage on `TaskService` business logic.

## 2. Reading (50 min)
- **Clean Code Chapter 9: Unit Tests (pp. 167-192).**
- **The Art of Writing Beautiful Unit Tests** – Patterns for expressive tests.
- **F.I.R.S.T. Acronym for Better Unit Tests** – Quick checklist.
- **What is Test Driven Development (Guru99)** – Intro to the workflow we’ll use.
- **YouTube: TDD Crash Course** (optional, 15 min) – Visual walkthrough.

## 3. This Week’s Work
- Add `CompleteTaskAsync` method to `TaskService` (TDD it).
- Write tests in `TaskFlowAPI.Tests/Unit` covering:
  - `GetAllTasksAsync` mapping.
  - `CreateTaskAsync` happy path + validation failure.
  - New `CompleteTaskAsync` (success + already completed scenarios).
- Use Moq + fake clock to control time.

## 4. Files to Modify
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/Services/Tasks/Rules/TaskBusinessRules.cs` (support completion logic)
- `TaskFlowAPI.Tests/Unit/*.cs` (create or expand test classes)
- Optional: `TaskFlowAPI.Tests/Examples` remove skip if you convert example.

## 5. Step-by-Step Instructions
1. Branch `week-17/<your-name>`.
2. Start with a failing test for `CompleteTaskAsync` (TDD). Define behaviour: mark complete, set timestamp, return DTO.
3. Implement minimal production code to pass the test using injected `ISystemClock`.
4. Add tests for existing methods, mocking repository interactions and validators.
5. Use `FluentAssertions` for assertions and `Moq` for verifying repository/validator calls.
6. Run `dotnet test` and inspect coverage report (`dotnet test /p:CollectCoverage=true` optional with coverlet).
7. Update placeholder tests (remove skip) once real tests exist.

## 6. How to Test
```bash
dotnet test TaskFlowAPI.sln --filter TaskService
# Optional coverage
dotnet test TaskFlowAPI.sln /p:CollectCoverage=true /p:CoverletOutputFormat=lcov
```

## 7. Success Criteria
- All placeholder `[Fact(Skip…)]` replaced with real tests.
- `CompleteTaskAsync` implemented and covered by tests.
- Coverage for `TaskService` ≥80% (include screenshot or coverage report).
- Tests pass consistently.

## 8. Submission Process
- Commit `Week 17 – task service tests`.
- PR summary includes coverage percentage and new tests list.
- Weekly issue attaches coverage screenshot or lcov snippet.

## 9. Journal and Discussion Prep
Journal:
*Red-Green-Refactor:* Capture one notable iteration (test, implementation, refactor) and what you learned.

*Coverage Review:* Where did coverage fall short of 80%, and what follow-up action will you take?

Discussion Prep:
- How did TDD influence your implementation of `CompleteTaskAsync`?
- What mocks/fakes did you choose and why?
- What gaps remain in test coverage?
- How will you keep tests maintainable as services evolve?

## 10. Time Estimate
- 15 min – Reading + test plan.
- 45 min – Tests + implementation.
- 15 min – Coverage run + PR/issue.
**Total:** ~75 minutes.

## 11. Getting Help
- Share failing test output in chat for debugging tips.
- Office hours: walk through Moq setup or coverage tooling.
- Mentor escalation if tests are flaky or coverage tool misbehaves.
