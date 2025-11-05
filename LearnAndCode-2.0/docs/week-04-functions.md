# Week 4 · Functions (Clean Code Ch. 3)

## 1. Learning Objectives
- Design small, intention-revealing controller actions.
- Extend TaskFlow endpoints (update/delete) while keeping flows cohesive.
- Apply Stepdown Rule so readers encounter high-level intent before details.

## 2. Reading (60 min)
- **Clean Code – Chapter 3: Functions (pp. 35-58).**
  - Focus on small functions, descriptive names, and minimizing arguments.
- **Clean Code Functions** (blog) – Applied examples of Chapter 3 refactors.
- **Google Java Style Guide: Method Names** – Reinforces naming standards across languages.
- **PEP 8 Function Naming** – Cross-language perspective for Python clients.
- **C# Coding Conventions: Method Names** – Align controller/service method naming with .NET guidance.
- **The Art of Writing Small and Plain Functions** – Practical heuristics for shrinking complex methods.
- **YouTube: The Ultimate Guide to Writing Functions** (optional, 10 min) – Quick visual refresher.
- **Microsoft REST API Guidelines – PATCH vs. PUT** (optional, 15 min) – confirm HTTP semantics for update/delete choices.

## 3. This Week’s Work
- Refactor `TasksController` methods into smaller helpers where logic exceeds 15–20 lines.
- Extend `ITaskService` with `UpdateTaskAsync` and `DeleteTaskAsync` signatures using expressive parameter names.
- Implement controller actions:
  - `PUT /api/tasks/{taskId}` consumes `UpdateTaskRequest`, returns `204 No Content`.
  - `DELETE /api/tasks/{taskId}` returns `204 No Content` (idempotent).
- Leave service/repository TODOs in place (students will implement later weeks) but ensure controller flow reads cleanly.

## 4. Files to Modify
- `TaskFlowAPI/Controllers/TasksController.cs`
- `TaskFlowAPI/Services/Interfaces/ITaskService.cs`
- `TaskFlowAPI/DTOs/Requests/UpdateTaskRequest.cs` (create or update as needed)

## 5. Step-by-Step Instructions
1. Branch `week-04/<your-name>`.
2. Identify any controller method longer than 20 lines; plan extractions into private helpers.
3. Add `UpdateTaskAsync`/`DeleteTaskAsync` to the service interface and adjust constructor DI parameters after Week 2 renames.
4. Implement `PUT` and `DELETE` endpoints following HTTP semantics and returning appropriate status codes.
5. Ensure helper names articulate intent (e.g., `CreateNotFoundResponse` vs. `Handle404`).
6. Run build/tests.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
  - Manual: Use `TaskFlowAPI.http` or Swagger to hit the new endpoints; expect `NotImplementedException` from service until Week 9—log behaviour for later follow-up.

## 7. Success Criteria
- Controller methods ≤ 20 lines, with meaningful helper names.
- `ITaskService` exposes asynchronous update/delete signatures with descriptive arguments.
- DTOs updated to support update workflow without duplication.
- Build/tests succeed and API still starts.

## 8. Submission Process
1. Commit `Week 04 – functions and endpoints`.
2. PR summary highlights extracted helpers and HTTP verb implementations.
3. Weekly submission issue includes before/after snippets and endpoint screenshots/logs.

## 9. Journal and Discussion Prep
Journal:
*Function Size:	Describe one spot where splitting a function improved clarity. What naming strategy helped?

*HTTP Semantics:	Why did you choose PUT over PATCH for this week? Capture pros/cons.

Discussion Prep:
- Share the largest helper extraction you made and the reasoning.
- How did you decide which parameters belong on service methods vs. DTOs?
- What will you validate first when `TaskService` implementations arrive in Week 9?
- Where might further refactors be necessary once business logic lands?

## 10. Time Estimate
- 45 min – Reading + planning refactors.
- 35 min – Implement endpoints + helpers.
- 20 min – Testing + PR/issue.
**Total:** ~100 minutes.

## 11. Getting Help
- Ask for code review on helper naming in team chat.
- Office hours: pair on HTTP semantics or DTO design.
- Mentor escalation if controller changes introduce routing or model-binding issues.

