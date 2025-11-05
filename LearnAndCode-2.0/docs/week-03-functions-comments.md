# Week 3 · Functions & Comments (Clean Code Ch. 3-4)

## 1. Learning Objectives
- Design small, single-purpose controller actions.
- Add update/delete endpoints that follow HTTP semantics.
- Document “why” with comments only when the code cannot express intent.

## 2. Clean Code Reading (20 min)
- **Chapter 3: Functions (pp. 35-58)** – Functions should be small, do one thing, and have descriptive names.
- **Chapter 4: Comments (pp. 59-76)** – Prefer self-explanatory code; comment only to explain intent or warn of consequences.
- Summary: Extract long methods into smaller ones, keep argument lists short, and write comments that explain “why,” not “what.”

## 3. This Week’s Work
- Refactor `TasksController` methods into smaller private helpers where needed.
- Extend `ITaskService` with update/delete signatures using clean names.
- Implement `PUT /api/tasks/{id}` and `DELETE /api/tasks/{id}` endpoints with proper status codes.
- Add comments sparingly to justify non-obvious decisions (e.g., why a validation check exists).

## 4. Files to Modify
- `TaskFlowAPI/Controllers/TasksController.cs`
- `TaskFlowAPI/Services/Interfaces/ITaskService.cs`
- Any new DTOs required for update operations (e.g., `UpdateTaskRequest`).

## 5. Step-by-Step Instructions
1. Branch `week-03/<your-name>`.
2. Read the existing controller and identify any method >20 lines—plan extractions.
3. Add new method signatures to `ITaskService` (`UpdateTaskAsync`, `DeleteTaskAsync`). Keep naming consistent and asynchronous.
4. Implement controller actions:
   - `PUT /api/tasks/{taskId}` accepts `UpdateTaskRequest`, returns `204 No Content`.
   - `DELETE /api/tasks/{taskId}` returns `204 No Content` (even if already missing).
5. Use private helpers for response creation if logic repeats.
6. Add comments only where the goal or side effect would be unclear without one.
7. Build and test.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Optional: Use `TaskFlowAPI.http` or Postman to send PUT/DELETE requests and observe 204 responses (will throw NotImplemented until Week 7/8—focus on wiring for now).

## 7. Success Criteria
- Controller actions <= 20 lines each, with clear helper method names.
- `ITaskService` exposes asynchronous update/delete methods with expressive parameter names.
- Comments exist only where necessary and explain intent.
- Build + tests succeed.

## 8. Submission Process
1. Commit message `Week 03 – functions and comments`.
2. PR with summary of helper extractions and new endpoints.
3. Weekly submission issue with screenshots of request/response (even if 500 due to TODOs, note expectation).

## 9. Journal and Discussion Prep
Journal:
*Technical Documentation:	Bob Martin says comments shouldn't be needed if names are good. What specific comments did you delete or find redundant after renaming, and why?

Discussion Prep:
- Share before/after of a refactored method—how did it improve readability?
- Where did you choose to keep or delete comments?
- What trade-offs did you make when designing update/delete workflows?

## 10. Time Estimate
- 10 min – Reading & planning extractions.
- 35 min – Refactor + add endpoints.
- 15 min – Testing + PR/issue.
**Total:** ~60 minutes.

## 11. Getting Help
- Ask for review of helper names in chat if unsure.
- Office hours: walk through HTTP semantics vs. business rules.
- Mentor escalation for idempotency or comment-usage questions.
