# Week 7 · Service Layer & DTOs (Clean Code Ch. 6 & 11)

## 1. Learning Objectives
- Implement business logic in the service layer using repository abstractions.
- Map between entities and DTOs with intentional helpers.
- Handle not-found and validation errors consistently (pre-FluentValidation).

## 2. Clean Code Reading (15 min)
- **Chapter 6: Objects and Data Structures (pp. 89-110)** – balance data exposure with behaviour.
- Revisit **Chapter 11** sections on separating policy from implementation.
- Summary: Services orchestrate work using abstractions, hiding persistence and enforcing rules.

## 3. This Week’s Work
- Implement `TaskService` methods (`GetAll`, `Get`, `Add`) using repository + mapping helpers.
- Add temporary guard clauses for create/update until Week 8 validation lands.
- Return `TaskDto` results to controllers.

## 4. Files to Modify
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/Services/Interfaces/ITaskService.cs` (ensure async naming after Week 2/3 refactor)
- Optional: add/update mapping helpers if you extracted them.

## 5. Step-by-Step Instructions
1. Branch `week-07/<your-name>`.
2. Implement `GetAll`:
   - Call `_taskRepository.GetAllAsync`.
   - Map each entity via `MapToDto` helper.
   - Return read-only list (`AsReadOnly()` or `List<TaskDto>` to be converted later).
3. Implement `Get`:
   - Fetch entity by id via repository.
   - Return null if not found (controller returns 404).
4. Implement `Add`:
   - Guard `request.Title` and `request.ProjectId` (temporary until Week 8).
   - Map request to entity via `MapToEntity` helper.
   - Save via repository and return DTO.
5. Add logging for critical paths using `_logger` (`LogInformation` on create, `LogWarning` on not found).
6. Update helper methods if needed to hydrate `ProjectName` (null-safe).
7. Build/tests.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Optional: run API and test `GET /api/tasks` and `POST /api/tasks` via Swagger (use sample payload). Expect validation to be basic; more in Week 8.

## 7. Success Criteria
- No remaining `NotImplementedException` in `TaskService`.
- Controller endpoints return data instead of throwing.
- Logging statements added for create + not-found scenarios.
- Build/tests succeed; manual GET returns seeded tasks.

## 8. Submission Process
- Commit `Week 07 – task service implementation`.
- PR summary must include sample JSON payload used for manual testing.
- Weekly issue attaches Swagger screenshot showing GET response.

## 9. Discussion Prep
- How does the service shield controllers from repository details?
- What validation gaps remain before Week 8?
- How will you extract mapper/validator in Week 9 without breaking consumers?

## 10. Time Estimate
- 10 min – Reading + code review.
- 35 min – Implement service methods + logging.
- 15 min – Manual testing + PR/issue.
**Total:** ~60 minutes.

## 11. Getting Help
- Share mapping helper logic in chat for feedback.
- Office hours: pair on first successful POST via Swagger.
- Mentor escalation if async flow or logging usage is unclear.
