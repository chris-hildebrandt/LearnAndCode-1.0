## TaskFlow API Deep-Dive Index

| Chunk ID | Component | Responsibilities & Key Behavior | Known Smells / TODOs | Linked Weeks |
| --- | --- | --- | --- | --- |
| L2-API-PROGRAM | `TaskFlowAPI/Program.cs` | Configures DI container, logging, middleware pipeline, EF Core context | TODOs for missing service registrations, middleware gaps | Week 6 setup, Week 10 error handling, Week 21 API design |
| L2-API-CTRL-TasksController | `TaskFlowAPI/Controllers/TasksController.cs` | Handles task CRUD endpoints, orchestrates service layer | Intentional poor naming (Week 2 refactor), missing PUT/DELETE (Week 4 assignment) | Weeks 2–4 |
| L2-API-SVC-ITaskService | `TaskFlowAPI/Services/Interfaces/ITaskService.cs` | Defines task service contract (GetAll, Get, Add, Update, Delete) | Missing method docs, inconsistent naming | Weeks 2–4, 9 |
| L2-API-SVC-TaskService | `TaskFlowAPI/Services/Tasks/TaskService.cs` | Business logic placeholder, mapping helpers, orchestrates repository calls | Methods throw `NotImplementedException`, inline validation TODO, mapper extraction planned | Weeks 9–11 |
| L2-API-REPO-ITaskRepository | `TaskFlowAPI/Repositories/Interfaces/ITaskRepository.cs` | Repository abstraction for task persistence | Missing async cancellation tokens | Weeks 8–9 |
| L2-API-REPO-TaskRepository | `TaskFlowAPI/Repositories/TaskRepository.cs` | EF Core implementation of task repository | Contains synchronous patterns, TODOs for filtering/pagination | Weeks 8–9, 11 |
| L2-API-DATA-DbContext | `TaskFlowAPI/Data/TaskFlowDbContext.cs` | EF Core context, DbSets for `TaskEntity`/`ProjectEntity` | Missing configuration for relationships, TODO for seeding | Weeks 7–8 |
| L2-API-ENT-TaskEntity | `TaskFlowAPI/Entities/TaskEntity.cs` | Domain model for tasks (fields: Title, Description, Priority, etc.) | Nullable handling, default values to review | Weeks 7–8 |
| L2-API-ENT-ProjectEntity | `TaskFlowAPI/Entities/ProjectEntity.cs` | Domain model for projects with task collection | Needs navigation property configuration | Weeks 7–8 |
| L2-API-DTO-CreateTaskRequest | `TaskFlowAPI/DTOs/Requests/CreateTaskRequest.cs` | Incoming payload definition for POST | Missing validation attributes, optional fields ambiguous | Weeks 2, 9–10 |
| L2-API-DTO-UpdateTaskRequest | `TaskFlowAPI/DTOs/Requests/UpdateTaskRequest.cs` | Payload definition for updates | TODO comment on partial updates vs patch | Week 4 extension, Week 10 validation |
| L2-API-DTO-TaskDto | `TaskFlowAPI/DTOs/Responses/TaskDto.cs` | Outgoing task representation for clients | Additional fields (ProjectName) derived; mapping handled in service | Weeks 2, 9 |
| L2-API-DTO-ProjectSummaryDto | `TaskFlowAPI/DTOs/Responses/ProjectSummaryDto.cs` | Lightweight project summary for list screens | TODO for tasks count calculation | Week 12+ |
| L2-API-DTO-PagedResponse | `TaskFlowAPI/DTOs/Responses/PagedResponse.cs` | Generic pagination envelope | TODO to enforce page metadata consistency | Week 12 filtering |
| L2-API-FLTR-Interfaces | `TaskFlowAPI/Services/Tasks/Filters/ITaskFilter.cs` | Filter chaining contract for task queries | Need docs on combination order | Week 12 advanced |
| L2-API-FLTR-Composite | `TaskFlowAPI/Services/Tasks/Filters/CompositeTaskFilter.cs` | Aggregates multiple filters | TODO to guard against empty sequences | Week 12 |
| L2-API-FLTR-DueDate | `TaskFlowAPI/Services/Tasks/Filters/DueDateTaskFilter.cs` | Filters tasks by due date range | TODO to validate range inputs | Week 12 |
| L2-API-FLTR-Priority | `TaskFlowAPI/Services/Tasks/Filters/PriorityTaskFilter.cs` | Filters tasks by priority levels | Needs constants/enums alignment | Week 12 |
| L2-API-FLTR-Status | `TaskFlowAPI/Services/Tasks/Filters/StatusTaskFilter.cs` | Filters tasks by completion state | TODO to align with domain statuses | Week 12 |
| L2-API-VAL-Create | `TaskFlowAPI/Validators/CreateTaskValidator.cs` | FluentValidation rules for creation | TODO to enforce project existence, due date >= today | Week 10 |
| L2-API-VAL-Update | `TaskFlowAPI/Validators/UpdateTaskValidator.cs` | FluentValidation rules for updates | TODO for partial updates, status transitions | Week 10 |
| L2-API-EXC-DomainValidation | `TaskFlowAPI/Exceptions/DomainValidationException.cs` | Custom exception for validation failures | TODO to include validation error payloads | Week 10 |
| L2-API-EXC-TaskNotFound | `TaskFlowAPI/Exceptions/TaskNotFoundException.cs` | Exception for missing tasks | TODO to include identifier context | Week 10 |
| L2-API-EXT-ExceptionMiddleware | `TaskFlowAPI/Extensions/ExceptionMiddlewareExtensions.cs` | Configures global exception handler | TODO to wire into Program.cs, add logging | Week 10 |
| L2-API-MIG-Initial | `TaskFlowAPI/Migrations/20251030171854_InitialCreate.cs` | Creates Task/Project tables | TODO to document seeding strategy | Week 7 |
| L2-API-TEST-Examples | `TaskFlowAPI.Tests/Examples/TaskServiceTests.Example.cs` | Provides sample unit tests scaffolding | Encourages AAA structure, TODO to replace placeholder asserts | Week 17 |
| L2-API-TEST-Placeholder | `TaskFlowAPI.Tests/Unit/PlaceholderTests.cs` | Empty test class for future work | TODO to implement real tests | Week 17 |

