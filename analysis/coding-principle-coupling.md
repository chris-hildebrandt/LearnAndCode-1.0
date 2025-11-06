## Coding Principle Coupling Assessment

### Approach
- Reviewed weekly objectives and assignments from `LearnAndCode-2.0/docs/week-XX*.md` alongside TaskFlow API source scaffolding.
- Mapped principles to concrete code-touch points (controllers, services, repositories, validators, filters, migrations).
- Evaluated whether each assignment reinforces the targeted Clean Code/SOLID principle and contributes to the evolving TaskFlow architecture.

### Phase 1 · Foundation (Weeks 1–4)
- **Week 1 (Quality Manifesto & setup):** Learners contextualise Clean Code within TaskFlow mission. Running the solution and tests ensures immediate familiarity with API structure, priming for future refactors.
- **Week 2 (Meaningful Names):** Direct rename exercise on `TasksController` and `ITaskService` connects naming principles to API surface. Refactor improves readability and sets stage for later async semantics.
- **Week 3 (Functions & Comments):** Builds upon Week 2 by enforcing single-purpose methods and meaningful comments across controller/service pair. Coupling is strong because students refactor the same codebase before implementing new features.
- **Week 4 (Git Workflow):** Focus shifts to disciplined branching/PR habits; indirect but critical for maintaining clean history as TaskFlow evolves. Optional Clean Code refresh keeps principle alignment.

### Phase 2 · Architecture (Weeks 5–8)
- **Week 5 (Classes & Encapsulation):** Moves into entity design (`TaskEntity`, `ProjectEntity`) and DbContext review. Encapsulation lessons apply to domain model shape, reinforcing that TaskFlow entities must hide persistence detail.
- **Week 6 (Repository Pattern):** Students examine repository interfaces and EF implementation. Clean separation of policy/implementation emphasises DIP preparation. Coupling is tight: repository tasks immediately feed Week 7 service work.
- **Week 7 (Service Layer & DTOs):** Learners implement TaskService logic (`GetAll`, `Get`, `Add`) utilising repository abstractions and mapping helpers. This enforces SRP at service layer and clarifies DTO/entity boundaries.
- **Week 8 (Error Handling & Validation):** Introduction of FluentValidation and exception middleware binds error-handling principles directly to TaskFlow request pipeline. Adds production-grade behaviour while reinforcing Clean Code Chapter 7.

### Phase 3 · SOLID (Weeks 9–13)
- **Week 9 (SRP):** Students extract mapping/validation responsibilities into dedicated classes or refine TaskService to respect single responsibilities, aligning with previously introduced helpers.
- **Week 10 (OCP):** Filter architecture (`CompositeTaskFilter`, `PriorityTaskFilter`, etc.) demonstrates open for extension/closed for modification. Learners extend behaviour by adding new filters without touching existing logic.
- **Week 11 (LSP) & Week 12 (ISP):** Focus on interface design and substitution across repositories/services. TaskFlow already provides interfaces, so assignments likely include refining contract boundaries and ensuring substitutability.
- **Week 13 (DIP):** Finalises DI configuration (`Program.cs` registrations), ensuring high-level modules depend on abstractions. Ties back to repository/service interfaces built earlier.

### Phase 4 · Quality & Patterns (Weeks 14–18)
- **Week 14 (File Organization):** Encourages consistent project structure, aligning with readability/time-to-comprehend metrics. TaskFlow’s modular structure (controllers, services, repositories) makes this tangible.
- **Week 15 (Unit Testing & TDD):** xUnit scaffolding (`TaskFlowAPI.Tests`) demonstrates how to write tests for business logic. Reinforces earlier Clean Code test chapter while ensuring architecture is testable.
- **Week 16 (Code Smells & Refactoring):** Students address intentional smells left in TaskService and other layers, closing the loop on earlier TODOs.
- **Week 17 (Design Patterns):** Encourages strategic refactors (e.g., strategy/composite already in filters). Coupling is natural; TaskFlow provides real code to retrofit patterns.
- **Week 18 (Code Review & Collaboration):** Aligns with Agile ceremonies; fosters critical evaluation of ongoing code changes.

### Phase 5 · Production Ready (Weeks 19–21)
- **Week 19 (API Design & Documentation):** Students finalise Swagger, docs, versioning, ensuring API contract quality and aligning with Clean Code boundaries.
- **Week 20 (Performance & Caching):** Introduces caching/performance enhancements, ensuring architecture scales.
- **Week 21 (Final Polish):** Consolidates work, emphasising demos, retros, and readiness metrics.

### Fitness of Tasks to Architecture
- **Progressive Reveal:** Each assignment builds on prior refactors; learners iterate on same code paths (controllers → services → repositories → filters → validators), ensuring deep understanding.
- **Intentional Smells:** Stubbed methods and TODOs (e.g., `TaskService` throwing `NotImplementedException`) create clear entry points for weekly objectives.
- **Full Stack Coverage:** TaskFlow includes domain, data access, service, API surface, validation, tests, and configuration, supporting holistic learning.
- **Potential Overloads:** Condensing multiple Clean Code topics into single weeks (e.g., objects/data structures spanning Weeks 5–7) risks cognitive overload; ensure instructions highlight legacy week equivalents to reinforce comprehension.

### Risks & Opportunities
- **Removed Concepts:** AI prompt engineering and event-driven architecture are absent; if still strategic, integrate optional labs without diluting TaskFlow focus.
- **Testing Depth:** Ensure Week 15 expands beyond placeholder tests to cover service/repository behaviours introduced earlier, reinforcing TDD principles.
- **Repository Abstraction:** Monitor that repository assignments include async/cancellation improvements; current scaffolding hints at missing tokens in interface.
- **Refactor Tracking:** Provide guidance for measuring impact of refactors (e.g., maintain checklist of eliminated smells) to connect actions to principles explicitly.

