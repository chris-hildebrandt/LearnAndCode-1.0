# Week 21 · API Design & Documentation

## 1. Learning Objectives
- Polish RESTful design (status codes, resource names, pagination).
- Document API using Swagger annotations and XML comments.
- Introduce API versioning and response shaping.

## 2. Reading (50 min)
- **Microsoft REST API Guidelines** – Resource naming, versioning, pagination.
- **REST API Tutorial (restfulapi.net)** – Core concepts and terminology.
- **Stack Overflow Blog: Best Practices for REST API Design** – Common pitfalls.
- **Swagger/OpenAPI Best Practices** (cohort wiki) – Documentation focus.
- Optional: Review public API docs (GitHub, Stripe, Twitter) for inspiration.
- Optional videos: REST API Concepts & Examples, REST API Design Best Practices.

## 3. This Week’s Work
- Add pagination support (`page`, `pageSize`) to task listing.
- Configure `Swashbuckle` for XML comments + operation summaries.
- Add API versioning (v1 default) using `Microsoft.AspNetCore.Mvc.Versioning` package.
- Update README with API endpoint overview.

## 4. Files to Modify
- `TaskFlowAPI/Controllers/TasksController.cs`
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/DTOs/Responses/PagedResponse.cs`
- `TaskFlowAPI/Program.cs` (Swagger + versioning)
- `TaskFlowAPI/TaskFlowAPI.csproj` (add XML documentation output)
- `README.md` (API section)

## 5. Step-by-Step Instructions
1. Branch `week-21/<your-name>`.
2. Enable XML comments in csproj `<GenerateDocumentationFile>true</GenerateDocumentationFile>`.
3. Install `Microsoft.AspNetCore.Mvc.Versioning` and configure `options.AssumeDefaultVersionWhenUnspecified = true`.
4. Update controller route to include version (e.g., `[Route("api/v{version:apiVersion}/tasks")]`).
5. Modify `GetTasks` action to accept `page`/`pageSize` query parameters and return `PagedResponse<TaskDto>`.
6. Update service to apply pagination after filters.
7. Add Swagger configuration to include XML comments and tags.
8. Update README “What You Will Build” with API endpoints overview.
9. Build/tests and hit Swagger to confirm docs show summaries + version.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Manual: `GET /api/v1/tasks?page=1&pageSize=10` expecting paged metadata.

## 7. Success Criteria
- API responds with paged payload containing metadata (page, pageSize, totalCount, totalPages).
- Swagger UI displays operation summaries and parameter descriptions.
- Versioned route works; old route removed or redirected.
- README documents major endpoints and query params.

## 8. Submission Process
- Commit `Week 21 – API design polish`.
- PR summary includes screenshot of updated Swagger UI.
- Weekly issue documents pagination decisions (default size, max size).

## 9. Journal and Discussion Prep
Journal:
*Documentation Update:* Record the most significant addition you made to README or swagger descriptions.

*Versioning Choice:* Note why you selected your versioning strategy and any migrations required later.

Discussion Prep:
- How did you choose default page size and limits?
- What versioning strategy did you implement and why?
- How can clients discover available filters/pagination from docs?
- Which external API docs inspired your approach?

## 10. Time Estimate
- 15 min – Reading + plan.
- 45 min – Pagination + versioning + docs updates.
- 15 min – Swagger verification + PR/issue.
**Total:** ~75 minutes.

## 11. Getting Help
- Share Swagger screenshot in chat if unsure about doc wording.
- Office hours: review pagination logic and off-by-one pitfalls.
- Mentor escalation if versioning conflicts with existing routes.
