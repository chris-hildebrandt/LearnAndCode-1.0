# Week 12 · Open/Closed Principle (OCP)

## 1. Learning Objectives
- Extend functionality (task filtering) without modifying existing service orchestration.
- Implement strategy pattern for task filters.
- Register strategies in DI and compose them dynamically.

## 2. Reading (45 min)
- **Clean Code Chapter 11 (Systems)** – Focus on keeping policies decoupled from details.
- **Understanding SOLID: Open-Closed Principle (Dev.to)** – Practical examples across languages.
- **Open-Closed Principle – Wikipedia** – Original definition and historical context.
- **Open-Closed Principle in Java (GeeksForGeeks)** – Additional implementation references.
- **Mastering SOLID: OCP (LinkedIn)** – Python-focused interpretation.
- **Open-Closed Principle in Practice (HowToDoInJava)** – Real-world best practices.
- Optional: Review cohort wiki article “Open/Closed Principle with Strategy Pattern” for additional context.

## 3. This Week’s Work
- Implement `StatusTaskFilter`, `PriorityTaskFilter`, `DueDateTaskFilter`, and `CompositeTaskFilter`.
- Add `ITaskFilterFactory` (or similar) to build filters based on query parameters.
- Update `TaskService` (or controller) to use filters when fetching tasks.

## 4. Files to Modify
- `TaskFlowAPI/Services/Tasks/Filters/*.cs`
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/Controllers/TasksController.cs` (wire query parameters)
- `TaskFlowAPI/Program.cs` (register filters/factory)

## 5. Step-by-Step Instructions
1. Branch `week-12/<your-name>`.
2. Implement each concrete filter’s `IsMatch` method.
3. Create `TaskFilterFactory` that accepts query parameters (`status`, `priority`, `dueBefore`, `dueAfter`) and returns a composite filter.
4. Update `TaskService.GetAllTasksAsync` to accept optional filter input (introduce new method or parameter object) and apply `Where(filter.IsMatch)`.
5. Update controller `GET /api/tasks` to accept query params and pass to service.
6. Register filters and factory in DI.
7. Ensure default behavior (no filters) still returns all tasks.
8. Build/tests + manual requests.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Manual: `GET /api/tasks?status=Completed`, `?priority=1,2`, `?dueBefore=2025-01-01`.

## 7. Success Criteria
- No switch statements or if-chains inside service for filtering logic.
- Adding a new filter is additive (new class + DI registration only).
- Query parameters correctly influence results.
- Build/tests succeed; manual requests filter data as expected.

## 8. Submission Process
- Commit `Week 12 – task filter strategies`.
- PR summary includes list of supported query params and example outputs.
- Weekly issue attaches screenshot or curl results showing filter working.

## 9. Journal and Discussion Prep
Journal:
*Filter Composition:* Document the signature you settled on for combining filters and why it remains OCP-friendly.

*Extensibility Audit:* List one prospective filter you might add later and what changes would (or wouldn’t) be required.

Discussion Prep:
- What would it take to add a new filter now?
- How did you decide where the factory lives (controller vs. service)?
- What caching or performance implications come with in-memory filtering?
- Which guardrails prevent this design from devolving into complex chains?

## 10. Time Estimate
- 10 min – Design filters + read docs.
- 45 min – Implement filters, factory, controller updates.
- 15 min – Manual verification + PR/issue.
**Total:** ~70 minutes.

## 11. Getting Help
- Share factory signature in chat for review.
- Office hours: live debug of query parameter binding.
- Mentor escalation if DI scope or filter composition is confusing.
