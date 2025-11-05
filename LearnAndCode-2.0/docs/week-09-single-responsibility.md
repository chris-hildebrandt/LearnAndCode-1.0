# Week 9 · Single Responsibility Principle (SRP)

## 1. Learning Objectives
- Identify and eliminate SRP violations within `TaskService`.
- Extract mapping, validation, and business-rule logic into focused classes.
- Update dependency injection to wire new components.

## 2. Clean Code Reading (15 min)
- Re-read **Clean Code Ch. 3 (Functions)** focusing on “do one thing” mantra.
- Review SRP sections from SOLID cheat sheet (provided in cohort wiki).
- Summary: Each class should have one reason to change. Split responsibilities across mapper, validator, and business rules.

## 3. This Week’s Work
- Extract `TaskMapper`, `TaskValidator` (domain-specific), and `TaskBusinessRules` from `TaskService`.
- Register new services in DI and adjust `TaskService` constructor.
- Ensure unit tests (examples) reflect new structure.

## 4. Files to Modify
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/Services/Tasks/TaskMapper.cs` (create)
- `TaskFlowAPI/Services/Tasks/Validation/TaskValidator.cs` (create)
- `TaskFlowAPI/Services/Tasks/Rules/TaskBusinessRules.cs` (create)
- `TaskFlowAPI/Program.cs` (add registrations)
- `TaskFlowAPI.Tests` examples if needed for namespace updates

## 5. Step-by-Step Instructions
1. Branch `week-09/<your-name>`.
2. Create folders `Services/Tasks/Validation` and `Services/Tasks/Rules` if they don’t exist.
3. Move mapping logic into `TaskMapper` with methods like `ToDto`, `ToEntity`.
4. Move domain validation (non-FluentValidation) into `TaskBusinessRules` (e.g., checking completion status transitions).
5. Inject new dependencies into `TaskService` via constructor. Remove internal helper methods replaced by new classes.
6. Update DI in `Program.cs` to register mapper, business rules, and FluentValidation validators.
7. Ensure service uses new collaborators; logging remains inside service.
8. Build/tests.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Manual GET/POST to verify behavior unchanged.

## 7. Success Criteria
- `TaskService` focused on orchestration only (≤150 lines ideally).
- Mapper/business rules classes contain clear, single responsibilities.
- Dependency injection updated without circular references.
- Build/tests succeed.

## 8. Submission Process
- Commit `Week 09 – SRP refactor`.
- PR summary outlines classes extracted and reasons.
- Weekly issue includes diagram or bullet list of new responsibilities.

## 9. Discussion Prep
- What metric indicated `TaskService` was doing too much?
- How did extraction change your approach to future unit tests?
- Were there responsibilities you intentionally kept inside the service? Why?

## 10. Time Estimate
- 10 min – Identify responsibilities + plan.
- 45 min – Extract classes + DI updates.
- 15 min – Test + PR/issue.
**Total:** ~70 minutes.

## 11. Getting Help
- Ask in chat for feedback on class names/responsibilities.
- Office hours: review DI configuration and refactoring strategy.
- Mentor escalation if you hit circular dependency or namespace headaches.
