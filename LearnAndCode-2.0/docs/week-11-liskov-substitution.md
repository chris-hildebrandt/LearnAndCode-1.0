# Week 11 · Liskov Substitution Principle (LSP)

## 1. Learning Objectives
- Ensure repository/service interfaces can be substituted without breaking consumers.
- Validate assumptions via contract-style unit tests using fakes.
- Tighten exception behaviour so all implementations honour the same rules.

## 2. Reading (10 min)
- Review LSP definition (Barbara Liskov, 1987) and practical examples from SOLID guide.
- Summary: Any class implementing an interface must be usable in place of any other implementation without altering desirable properties (correctness, task completion).

## 3. This Week’s Work
- Create in-memory `FakeTaskRepository` for tests to exercise `ITaskService` contract.
- Adjust `TaskRepository` and `TaskService` to ensure behaviour matches fake (e.g., null vs. exception cases).
- Add contract tests verifying both real and fake repositories honour expectations.

## 4. Files to Modify
- `TaskFlowAPI/Repositories/Interfaces/ITaskRepository.cs` (update XML summary clarifying contract)
- `TaskFlowAPI/Repositories/TaskRepository.cs` (ensure behaviour matches contract)
- `TaskFlowAPI.Tests/Unit/TaskRepositoryContractTests.cs` (new)
- Optional: `TaskFlowAPI/Services/Tasks/TaskService.cs` for behaviour tweaks

## 5. Step-by-Step Instructions
1. Branch `week-11/<your-name>`.
2. Define contract in interface comments (e.g., `GetByIdAsync` returns null when missing, never throws).
3. Implement `FakeTaskRepository` inside test project (in-memory list support) adhering to contract.
4. Write `[Theory]` tests using abstract helper verifying behaviours like:
   - `CreateAsync` returns entity with generated Id.
   - `DeleteAsync` silently succeeds when missing.
   - `GetAllAsync` ordering matches specification.
5. Run tests against both fake and real repository (use xUnit `[ClassData]` or manual loops with shared test method).
6. Adjust production repository/service to satisfy failing contract tests.

## 6. How to Test
```bash
dotnet test TaskFlowAPI.sln --filter TaskRepositoryContractTests
```
- Ensure both implementations pass without conditional expectations.

## 7. Success Criteria
- Interface documentation clearly states behavioural contract.
- Fake repository mirrors real repository behaviour (no diverging edge cases).
- Contract tests pass for both implementations.
- Build/tests succeed.

## 8. Submission Process
- Commit `Week 11 – LSP contract tests`.
- PR summary includes snippet of contract test and link to passing run.
- Weekly issue documents at least one behaviour clarified by the contract.

## 9. Discussion Prep
- What assumptions did the real repository make that weren’t explicit?
- How will fakes/stubs help future testing weeks?
- Where else might LSP be at risk in this codebase?

## 10. Time Estimate
- 10 min – Review contracts + plan tests.
- 35 min – Implement fake + contract tests.
- 15 min – Fix discrepancies + PR/issue.
**Total:** ~60 minutes.

## 11. Getting Help
- Share test scaffolding in chat for feedback.
- Office hours: pair on writing shared contract tests.
- Mentor escalation if EF Core behaviours diverge from fake and you need guidance.
