# Week 12 · Interface Segregation Principle (ISP)

## 1. Learning Objectives
- Split “fat” interfaces into focused contracts.
- Update implementations and consumers to depend only on what they use.
- Ensure DI configuration honours the new abstractions.

## 2. Reading (10 min)
- Review ISP section from SOLID guide (clients should not be forced to depend on methods they do not use).
- Summary: Break `ITaskRepository` into read/write interfaces so services/controllers depend on minimal contracts.

## 3. This Week’s Work
- Create `ITaskReader` and `ITaskWriter` interfaces.
- Update repository implementation to implement both.
- Update services/controllers to depend on the appropriate interface(s).

## 4. Files to Modify
- `TaskFlowAPI/Repositories/Interfaces/ITaskRepository.cs` (split or replace)
- New files: `ITaskReader.cs`, `ITaskWriter.cs`
- `TaskFlowAPI/Repositories/TaskRepository.cs`
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/Program.cs`

## 5. Step-by-Step Instructions
1. Branch `week-12/<your-name>`.
2. Create new interfaces:
   - `ITaskReader`: `GetAllAsync`, `GetByIdAsync`.
   - `ITaskWriter`: `CreateAsync`, `UpdateAsync`, `DeleteAsync`.
3. Update `TaskRepository` to implement both interfaces. Remove obsolete combined interface.
4. Update DI registrations: register concrete type for both reader and writer (scoped).
5. Update `TaskService` constructor to depend on required interfaces (likely both).
6. Update controller or other consumers to request only the reader interface when appropriate.
7. Adjust tests/fakes to mirror new interfaces.
8. Build/tests.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```

## 7. Success Criteria
- No files depend on unused repository methods.
- DI container resolves service with split interfaces.
- Tests compile and pass with new abstractions.

## 8. Submission Process
- Commit `Week 12 – interface segregation`.
- PR summary explains who consumes reader vs. writer.
- Weekly issue includes diagram or table of dependencies after refactor.

## 9. Discussion Prep
- What benefits did you notice after splitting interfaces?
- Could any service depend on only `ITaskReader` now?
- Where else could ISP apply in this codebase?

## 10. Time Estimate
- 10 min – Plan new interfaces.
- 35 min – Implement + update consumers.
- 15 min – Test + PR/issue.
**Total:** ~60 minutes.

## 11. Getting Help
- Post interface proposals in chat for naming review.
- Office hours: walkthrough DI adjustments.
- Mentor escalation if circular dependencies appear after refactor.
