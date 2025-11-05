# Week 5 · Classes & Encapsulation (Clean Code Ch. 10)

## 1. Learning Objectives
- Convert an anemic entity into a rich domain model with invariants.
- Hide mutable state behind methods that enforce business rules.
- Add unit-test-friendly factory methods for creating valid tasks.

## 2. Clean Code Reading (15 min)
- **Chapter 10: Classes (pp. 137-154).**
  - Focus on cohesion, encapsulation, and hiding implementation details.
  - Summary: Classes should expose a minimal public API, keep data and behavior together, and prevent invalid states.

## 3. This Week’s Work
- Refactor `TaskEntity` to use private fields and guarded property access.
- Add domain behaviors: `Complete()`, `Reopen()`, `UpdateDetails(...)`, `ChangePriority(...)`.
- Introduce static factory `TaskEntity.Create(...)` that validates inputs.

## 4. Files to Modify
- `TaskFlowAPI/Entities/TaskEntity.cs`
- `TaskFlowAPI/Entities/ProjectEntity.cs` (optional: add helper to attach tasks)
- Any affected migration snapshot (run `dotnet ef migrations add` only if schema changes).

## 5. Step-by-Step Instructions
1. Branch `week-05/<your-name>`.
2. Replace auto-properties with private fields + public getters where necessary.
3. Add constructor(s) or factory ensuring `Title`, `Priority`, and `ProjectId` are validated.
4. Implement domain methods:
   - `Complete(DateTime completedAt)` marks task complete and sets timestamp.
   - `Reopen()` resets completion state.
   - `UpdateDetails(string title, string? description, DateTime? dueDate)` guards null/empty titles.
   - `ChangePriority(int priority)` ensures priority range (0-5 default suggestion).
5. Ensure all state changes flow through these methods; remove public setters.
6. Update seed data in `TaskFlowDbContext` to use the new factory or constructor.
7. Build and run migrations if compilation demands (expected minimal changes if property names remain).

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Optional: temporary console app or `dotnet script` to instantiate `TaskEntity` and ensure methods behave.

## 7. Success Criteria
- No public setters on `TaskEntity` (other than EF Core required parameterless constructor if used).
- Domain methods enforce invariants and throw meaningful exceptions when inputs invalid.
- Seed data still builds; migrations remain valid.
- Build + tests succeed.

## 8. Submission Process
- Commit `Week 05 – task entity encapsulation`.
- PR summary must describe each new domain method and rule enforced.
- Weekly submission issue includes snippet of new `TaskEntity.Create` signature.

## 9. Discussion Prep
- Which invariants did you guard and why?
- How would another developer know how to create a valid `TaskEntity` now?
- What future bugs does this encapsulation prevent?

## 10. Time Estimate
- 10 min – Reading + design sketch.
- 40 min – Implementation + seed data adjustments.
- 10 min – Build/test + PR/issue.
**Total:** ~60 minutes.

## 11. Getting Help
- Share constructor/factory signatures in chat for naming feedback.
- Office hours: review exception strategy for invalid states.
- Mentor escalation if EF Core navigation properties cause confusion.
