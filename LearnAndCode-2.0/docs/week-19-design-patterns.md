# Week 19 · Essential Design Patterns

## 1. Learning Objectives
- Implement Factory pattern for creating tasks with context-aware defaults.
- Review and solidify Strategy pattern usage (filters) and Repository pattern.
- Document when each pattern is appropriate within TaskFlow API.

## 2. Reading (50 min)
- **Patterns.dev** – Browse sections on creational and behavioural patterns.
- **Refactoring Guru: Design Patterns** – Reference implementations and UML diagrams.
- **Sourcemaking: Design Patterns** – Additional explanations with variations.
- **Tutorialspoint Design Patterns Overview** – Quick refresher on categories.
- **YouTube: 10 Design Patterns Explained in 10 Minutes** (optional, 10 min) – High-level tour.
- Focus on Factory & Strategy sections as they align with this week’s work.

## 3. This Week’s Work
- Create `TaskFactory` responsible for constructing `TaskEntity` instances based on request type (default due dates, priority rules).
- Update `TaskService` to use factory instead of `MapToEntity` for creation.
- Document existing Strategy usage for filters and ensure it’s extensible (no direct instantiation in service).

## 4. Files to Modify
- `TaskFlowAPI/Services/Tasks/TaskFactory.cs` (new)
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/Services/Tasks/Mapping/TaskMapper.cs` (adjust to rely on factory)
- Update DI registration (`Program.cs` or `ServiceCollectionExtensions`)
- `docs/` add short explanation snippet if relevant

## 5. Step-by-Step Instructions
1. Branch `week-19/<your-name>`.
2. Design `TaskFactory` with methods like `CreateNewTask(CreateTaskRequest request, ISystemClock clock)` returning a fully initialised entity.
3. Move creation logic (default priority, CreatedAt) from mapper/business rules into factory.
4. Update `TaskService` to call factory before saving; ensure tests updated to mock factory.
5. Review filter strategy registration—ensure service receives filters via abstraction (no `new` in service). Refactor if needed.
6. Add XML doc or inline comments summarising when to use each pattern.
7. Update tests to use fake factory as needed.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Ensure unit tests mocking factory still reach 80% coverage.

## 7. Success Criteria
- `TaskService` no longer constructs entities directly; factory handles creation.
- Strategy pattern remains intact with DI-based filter registration.
- Tests updated to use factory mock.
- Build/tests succeed.

## 8. Submission Process
- Commit `Week 19 – design patterns`.
- PR summary lists patterns implemented/refined and rationale.
- Weekly issue includes short paragraph on when to use Factory vs. Strategy.

## 9. Journal and Discussion Prep
Journal:
*Pattern Selection:* Document why you chose factory vs. keeping logic in mapper/business rules.

*Future Pattern Ideas:* Note one additional pattern you considered and whether it fits the current scope.

Discussion Prep:
- How did the factory improve creation logic clarity?
- What trade-offs exist when adding more patterns?
- Which future features could reuse this factory?
- How will you guard against over-patterning the codebase?

## 10. Time Estimate
- 10 min – Pattern review + design.
- 40 min – Implement factory + service/test updates.
- 15 min – Build/test + PR/issue.
**Total:** ~65 minutes.

## 11. Getting Help
- Share factory interface in chat for naming feedback.
- Office hours: review pattern diagrams.
- Mentor escalation if tests become overly coupled to factory.
