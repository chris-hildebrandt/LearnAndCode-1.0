# Week 6 · Repository Pattern (Clean Code Ch. 11 systems focus)

## 1. Learning Objectives
- Implement repository methods using EF Core best practices.
- Apply async patterns (`await`, `CancellationToken`) consistently.
- Understand how repositories isolate data access from services.

## 2. Clean Code Reading (15 min)
- **Chapter 11: Systems (pp. 155-174)** – focus on separating construction from use and keeping boundaries clean.
- Summary: Organise code so high-level policies aren’t coupled to implementation details (like EF Core).

## 3. This Week’s Work
- Implement all TODOs in `TaskRepository`.
- Use `AsNoTracking` for read operations and include `Project` navigation.
- Ensure create/update/delete paths save changes with cancellation support.

## 4. Files to Modify
- `TaskFlowAPI/Repositories/TaskRepository.cs`
- `TaskFlowAPI/Repositories/Interfaces/ITaskRepository.cs` (doc comments if needed)
- Optional: `TaskFlowDbContext` if you need helper queries (keep minimal).

## 5. Step-by-Step Instructions
1. Branch `week-06/<your-name>`.
2. Implement `GetAllAsync` using ordering by `Priority` then `DueDate` then `CreatedAt`.
3. Implement `GetByIdAsync` including related `Project` via `.Include` and `.AsNoTracking()`.
4. Implement `CreateAsync` using `_dbContext.Tasks.AddAsync` and `SaveChangesAsync`.
5. Implement `UpdateAsync` ensuring entity is tracked (attach if necessary) and call `SaveChangesAsync`.
6. Implement `DeleteAsync` with null check—no exception if entity missing.
7. Add guard clauses for `cancellationToken.ThrowIfCancellationRequested()` when appropriate.
8. Run build/tests.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- (Optional) `dotnet ef database update` followed by manual GET via Swagger to ensure repository works (will still hit NotImplemented in service until Week 7, that’s expected).

## 7. Success Criteria
- No remaining `NotImplementedException` in `TaskRepository`.
- All methods use async/await and respect `CancellationToken`.
- Query methods include `AsNoTracking` and navigation properties as needed.
- Build/tests succeed.

## 8. Submission Process
- Commit `Week 06 – repository implementation`.
- PR summary must list each method and how you tested it.
- Weekly submission issue includes code snippet of your favourite query.

## 9. Discussion Prep
- What trade-offs did you consider regarding eager vs. lazy loading?
- How does cancelling a request propagate through repository methods?
- Which helper methods or extension methods might simplify repository code later?

## 10. Time Estimate
- 10 min – Reading + plan queries.
- 35 min – Implement methods + guard clauses.
- 10 min – Build/test + PR/issue.
**Total:** ~55 minutes.

## 11. Getting Help
- Share LINQ query ideas in chat for review.
- Office hours demo: hooking repository into Program.cs (already registered).
- Mentor escalation if SaveChanges behaviour or tracking confuses you.
