# Week 8 · Error Handling & Validation (Clean Code Ch. 7)

## 1. Learning Objectives
- Implement FluentValidation rules for create/update requests.
- Introduce domain-specific exceptions and map them to HTTP responses.
- Configure global exception handling middleware.

## 2. Clean Code Reading (15 min)
- **Chapter 7: Error Handling (pp. 111-134)** – prefer exceptions to error codes, keep error-handling code separate from happy-path logic.
- Summary: Throw exceptions with context, keep the happy path clean, and centralise error mapping.

## 3. This Week’s Work
- Implement `CreateTaskValidator` and `UpdateTaskValidator` with actionable rules.
- Throw `DomainValidationException` or `TaskNotFoundException` from service methods as appropriate.
- Replace placeholder exception middleware with polished `ProblemDetails` outputs.

## 4. Files to Modify
- `TaskFlowAPI/Validators/CreateTaskValidator.cs`
- `TaskFlowAPI/Validators/UpdateTaskValidator.cs`
- `TaskFlowAPI/Services/Tasks/TaskService.cs` (add exception usage + guard logic)
- `TaskFlowAPI/Extensions/ExceptionMiddlewareExtensions.cs`
- `TaskFlowAPI/Program.cs` (ensure middleware order correct)

## 5. Step-by-Step Instructions
1. Branch `week-08/<your-name>`.
2. Implement validation rules:
   - Title: required, 3-100 chars.
   - Priority: between 0-5.
   - DueDate: must be future or today.
   - Update request: require at least one field set.
3. Inject validators into `TaskService` (constructor) and use them in `Add`/`Update`.
4. Throw `DomainValidationException` when validation fails and include aggregated messages.
5. Throw `TaskNotFoundException` in Delete/Update when repository returns null.
6. Update `UseTaskFlowExceptionHandler` to map custom exceptions to 400/404 with structured `ProblemDetails`.
7. Log errors with context inside middleware or service (use `_logger.LogError`).
8. Run build/tests and hit endpoints with invalid payloads to confirm 400 responses with messages.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Manual tests via Swagger/Postman:
  - POST with missing title → 400 + validation message.
  - PUT with nonexistent id → 404 + “Task not found.”

## 7. Success Criteria
- Validators enforce rules and produce clear messages.
- Services catch validator results and throw domain exceptions.
- Exception middleware returns consistent JSON (`application/problem+json`).
- Logs contain warning/error messages for invalid requests.

## 8. Submission Process
- Commit `Week 08 – validation and error handling`.
- PR summary includes sample error response JSON.
- Weekly issue attaches screenshot of Swagger error response.

## 9. Discussion Prep
- How did centralized error handling simplify controllers?
- What validation rules still feel brittle or missing?
- How will these exceptions influence future unit tests?

## 10. Time Estimate
- 15 min – Reading + rule design.
- 45 min – Implement validators, exceptions, middleware.
- 15 min – Manual testing + PR/issue.
**Total:** ~75 minutes.

## 11. Getting Help
- Share validator rules in chat for quick sanity checks.
- Office hours: walkthrough of middleware debugging.
- Mentor escalation if FluentValidation integration or DI wiring is unclear.
