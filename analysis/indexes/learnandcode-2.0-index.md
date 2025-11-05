## LearnAndCode 2.0 Reference Index

| Chunk ID | Path | Type | Focus | Key Links / Notes |
| --- | --- | --- | --- | --- |
| L2-SUP-README | `LearnAndCode-2.0/README.md` | Overview | 21-week TaskFlow API curriculum roadmap | Highlights phases, deliverables, expectations. |
| L2-SUP-SETUP | `LearnAndCode-2.0/SETUP.md` | Setup Guide | Environment checklist for TaskFlow API | Includes tooling prerequisites. |
| L2-SUP-WKPROG | `LearnAndCode-2.0/WEEKLY_PROGRESS.md` | Tracking | Completion tracker | Used weekly for accountability. |
| L2-SUP-LLM | `LearnAndCode-2.0/llm.txt` | Policy | AI usage guidance / prompts | Defines AI collaboration rules. |
| L2-SUP-QMAN | `LearnAndCode-2.0/Quality Manifesto.pdf` | Reference | Quality Manifesto source | Supplemental reading. |
| L2-SUP-CLEAN | `LearnAndCode-2.0/Clean Code.pdf` | Reference | Clean Code textbook PDF | Supplemental reading. |
| L2-SUP-SLN | `LearnAndCode-2.0/TaskFlowAPI.sln` | Solution | Visual Studio solution file | Entry point for TaskFlow API + tests. |
| L2-DOC-W01 | `LearnAndCode-2.0/docs/week-01-introduction.md` | Weekly Doc | Orientation, manifesto deep dive, environment setup | Includes journal, discussion prep, testing instructions. |
| L2-DOC-W02 | `LearnAndCode-2.0/docs/week-02-meaningful-names.md` | Weekly Doc | Naming standards applied to TaskFlow | Contains assignments, review prompts. |
| L2-DOC-W03 | `LearnAndCode-2.0/docs/week-03-functions-comments.md` | Weekly Doc | Functions & comments best practices | Tailored to API refactoring tasks. |
| L2-DOC-W04 | `LearnAndCode-2.0/docs/week-04-git-workflow.md` | Weekly Doc | Git workflow, branching around TaskFlow | Integrates standups + retro prompts. |
| L2-DOC-W05 | `LearnAndCode-2.0/docs/week-05-classes-encapsulation.md` | Weekly Doc | Entities, encapsulation in API domain | Introduces EF Core modeling tasks. |
| L2-DOC-W06 | `LearnAndCode-2.0/docs/week-06-repository-pattern.md` | Weekly Doc | Repository pattern implementation | Connects to `TaskRepository`. |
| L2-DOC-W07 | `LearnAndCode-2.0/docs/week-07-service-layer-dtos.md` | Weekly Doc | Service layer design, DTO mapping | Focus on service composition. |
| L2-DOC-W08 | `LearnAndCode-2.0/docs/week-08-error-handling-validation.md` | Weekly Doc | Validation + global error handling | Introduces FluentValidation + middleware. |
| L2-DOC-W09 | `LearnAndCode-2.0/docs/week-09-single-responsibility.md` | Weekly Doc | SOLID SRP applied to API modules | Audits responsibilities across layers. |
| L2-DOC-W10 | `LearnAndCode-2.0/docs/week-10-open-closed-principle.md` | Weekly Doc | OCP in TaskFlow | Extensibility strategies. |
| L2-DOC-W11 | `LearnAndCode-2.0/docs/week-11-liskov-substitution.md` | Weekly Doc | LSP enforcement | Interface contracts and inheritance. |
| L2-DOC-W12 | `LearnAndCode-2.0/docs/week-12-interface-segregation.md` | Weekly Doc | ISP on services/repos | Encourages granular interfaces. |
| L2-DOC-W13 | `LearnAndCode-2.0/docs/week-13-dependency-inversion.md` | Weekly Doc | DIP & dependency injection | Aligns with .NET DI container. |
| L2-DOC-W14 | `LearnAndCode-2.0/docs/week-14-file-organization.md` | Weekly Doc | File organization, modular architecture | Focus on cleanup & structure. |
| L2-DOC-W15 | `LearnAndCode-2.0/docs/week-15-unit-testing-tdd.md` | Weekly Doc | Unit testing & TDD pipeline | Connects to `TaskFlowAPI.Tests` scaffolding. |
| L2-DOC-W16 | `LearnAndCode-2.0/docs/week-16-code-smells-refactoring.md` | Weekly Doc | Smell catalog, refactoring plan | Targets known issues in codebase. |
| L2-DOC-W17 | `LearnAndCode-2.0/docs/week-17-design-patterns.md` | Weekly Doc | Design patterns aligned to TaskFlow | Encourages strategic refactors. |
| L2-DOC-W18 | `LearnAndCode-2.0/docs/week-18-code-review-collaboration.md` | Weekly Doc | Code review etiquette, retrospectives | Provides standup prompts. |
| L2-DOC-W19 | `LearnAndCode-2.0/docs/week-19-api-design-documentation.md` | Weekly Doc | API design, documentation, versioning | Includes Swagger + docs tasks. |
| L2-DOC-W20 | `LearnAndCode-2.0/docs/week-20-performance-caching.md` | Weekly Doc | Performance tuning, caching strategy | Targets API efficiency upgrades. |
| L2-DOC-W21 | `LearnAndCode-2.0/docs/week-21-final-polish.md` | Weekly Doc | Final polish, demo prep, retrospectives | Wrap-up tasks + success criteria. |
| L2-DOC-EX01 | `LearnAndCode-2.0/docs/Examples/MeaningfulNames.md` | Example | Naming improvements example (Task DTO focus) | Supports Week 2 doc. |
| L2-DOC-FINALRETRO | `LearnAndCode-2.0/docs/final-retro-template.md` | Template | Retrospective template | Used in Phase 5 retro. |
| L2-DOC-IMG | `LearnAndCode-2.0/docs/image.png` | Asset | Screenshot for setup / codespaces | Referenced in Week 1 doc. |
| L2-API-ROOT | `LearnAndCode-2.0/TaskFlowAPI/README.md` | Project Guide | TaskFlow API overview, architecture notes | Describes intentional smells, TODOs. |
| L2-API-CSProj | `LearnAndCode-2.0/TaskFlowAPI/TaskFlowAPI.csproj` | Config | Project configuration, package references | Defines target frameworks, dependencies. |
| L2-API-APPSET | `LearnAndCode-2.0/TaskFlowAPI/appsettings.json` | Config | Base app settings | Includes logging, connection strings placeholder. |
| L2-API-APPSETDEV | `LearnAndCode-2.0/TaskFlowAPI/appsettings.Development.json` | Config | Dev overrides | Local database configuration. |
| L2-API-PROGRAM | `LearnAndCode-2.0/TaskFlowAPI/Program.cs` | Entry Point | Web application bootstrap, DI wiring | Contains TODOs for composition root. |
| L2-API-HTTP | `LearnAndCode-2.0/TaskFlowAPI/TaskFlowAPI.http` | REST Client | Sample HTTP requests | Used for manual testing. |
| L2-API-CTRL | `LearnAndCode-2.0/TaskFlowAPI/Controllers/TasksController.cs` | Controller | REST endpoints, orchestrates service calls | Includes validation & error handling gaps. |
| L2-API-DTO-REQ | `LearnAndCode-2.0/TaskFlowAPI/DTOs/Requests` | DTO Folder | Request DTO definitions | Houses `Create` & `Update` requests. |
| L2-API-DTO-REQ-Create | `.../DTOs/Requests/CreateTaskRequest.cs` | DTO | Task creation payload | Contains validation attributes (if any). |
| L2-API-DTO-REQ-Update | `.../DTOs/Requests/UpdateTaskRequest.cs` | DTO | Task update payload | Tracks optional fields. |
| L2-API-DTO-RESP | `LearnAndCode-2.0/TaskFlowAPI/DTOs/Responses` | DTO Folder | Response DTOs | Paged response + summaries. |
| L2-API-DTO-RESP-Task | `.../DTOs/Responses/TaskDto.cs` | DTO | Task detail projection | Maps entity to shape exposed via API. |
| L2-API-DTO-RESP-Project | `.../DTOs/Responses/ProjectSummaryDto.cs` | DTO | Project summary projection | |
| L2-API-DTO-RESP-Paged | `.../DTOs/Responses/PagedResponse.cs` | DTO | Pagination wrapper | Supports filtering results. |
| L2-API-DATA | `LearnAndCode-2.0/TaskFlowAPI/Data/TaskFlowDbContext.cs` | Data Layer | EF Core DbContext | Seeds, DbSets, configuration placeholders. |
| L2-API-ENTITIES | `LearnAndCode-2.0/TaskFlowAPI/Entities` | Domain | Entity definitions | `ProjectEntity`, `TaskEntity`. |
| L2-API-ENT-Project | `.../Entities/ProjectEntity.cs` | Entity | Project domain model | Contains navigation properties. |
| L2-API-ENT-Task | `.../Entities/TaskEntity.cs` | Entity | Task domain model | Tracks status, due date, etc. |
| L2-API-EXC | `LearnAndCode-2.0/TaskFlowAPI/Exceptions` | Domain | Custom exceptions | Domain validation + not found. |
| L2-API-EXC-Domain | `.../Exceptions/DomainValidationException.cs` | Exception | Validation exception | Raised by service layer. |
| L2-API-EXC-NotFound | `.../Exceptions/TaskNotFoundException.cs` | Exception | Missing task scenario | |
| L2-API-EXT | `LearnAndCode-2.0/TaskFlowAPI/Extensions/ExceptionMiddlewareExtensions.cs` | Middleware | Exception handling extensions | Sets up middleware pipeline. |
| L2-API-MIG | `LearnAndCode-2.0/TaskFlowAPI/Migrations` | EF Migration | Database migrations | Initial create migration + snapshot. |
| L2-API-MIG-Init | `.../Migrations/20251030171854_InitialCreate.cs` | Migration | Initial schema creation | Aligns with EF models. |
| L2-API-MIG-Designer | `.../Migrations/20251030171854_InitialCreate.Designer.cs` | Generated | Designer metadata | Auto-generated by EF. |
| L2-API-MIG-Snapshot | `.../Migrations/TaskFlowDbContextModelSnapshot.cs` | Snapshot | Current schema snapshot | Reference for future diffs. |
| L2-API-MIG-README | `.../Migrations/README.md` | Notes | Explains migration usage | |
| L2-API-REPO | `LearnAndCode-2.0/TaskFlowAPI/Repositories` | Data Access | Repository implementations + interfaces | Separates persistence logic. |
| L2-API-REPO-INT | `.../Repositories/Interfaces/ITaskRepository.cs` | Interface | Repository contract | Defines CRUD abstractions. |
| L2-API-REPO-Impl | `.../Repositories/TaskRepository.cs` | Repository | EF-backed repository | Contains TODOs for optimizations. |
| L2-API-SERV | `LearnAndCode-2.0/TaskFlowAPI/Services` | Business Logic | Service layer + filters | Orchestrates domain rules. |
| L2-API-SERV-INT | `.../Services/Interfaces/ITaskService.cs` | Interface | Service contract | Defines operations for controller. |
| L2-API-SERV-Task | `.../Services/Tasks/TaskService.cs` | Service | Business logic, filters, validations | Contains TODOs & smell opportunities. |
| L2-API-SERV-FLT | `.../Services/Tasks/Filters` | Filter Folder | Task filtering chain | Implements strategy/composite patterns. |
| L2-API-SERV-FLT-Interface | `.../Filters/ITaskFilter.cs` | Interface | Filter contract | |
| L2-API-SERV-FLT-Composite | `.../Filters/CompositeTaskFilter.cs` | Filter | Compose multiple filters | |
| L2-API-SERV-FLT-DueDate | `.../Filters/DueDateTaskFilter.cs` | Filter | Due date filtering | |
| L2-API-SERV-FLT-Priority | `.../Filters/PriorityTaskFilter.cs` | Filter | Priority filtering | |
| L2-API-SERV-FLT-Status | `.../Filters/StatusTaskFilter.cs` | Filter | Status filtering | |
| L2-API-VAL | `LearnAndCode-2.0/TaskFlowAPI/Validators` | Validation | FluentValidation validators | Create & update validation rules. |
| L2-API-VAL-Create | `.../Validators/CreateTaskValidator.cs` | Validator | Validator for create requests | Notes required fields, constraints. |
| L2-API-VAL-Update | `.../Validators/UpdateTaskValidator.cs` | Validator | Validator for update requests | Handles optional fields. |
| L2-API-PROP | `LearnAndCode-2.0/TaskFlowAPI/Properties` | Config | Assembly info & launch settings | |
| L2-API-PROP-Assembly | `.../Properties/AssemblyInfo.cs` | Config | Assembly metadata | |
| L2-API-PROP-Launch | `.../Properties/launchSettings.json` | Config | Launch profiles | |
| L2-API-PROP-README | `.../Properties/README.md` | Notes | Clarifies launch profiles | |
| L2-TEST-ROOT | `LearnAndCode-2.0/TaskFlowAPI.Tests/TaskFlowAPI.Tests.csproj` | Test Config | Test project definition | |
| L2-TEST-README | `LearnAndCode-2.0/TaskFlowAPI.Tests/Examples/TaskServiceTests.Example.cs` | Example Tests | Illustrative xUnit tests | Scaffolds test patterns. |
| L2-TEST-UNIT | `LearnAndCode-2.0/TaskFlowAPI.Tests/Unit/PlaceholderTests.cs` | Unit Test | Placeholder tests | Template for participants. |

