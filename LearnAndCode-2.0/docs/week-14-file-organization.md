# Week 14 · File Organization & Module Structure (Clean Code Ch. 5)

## 1. Learning Objectives
- Restructure files so each class lives in a focused module/folder.
- Break apart any remaining “god” files (e.g., legacy TaskService monolith, helpers).
- Establish namespace conventions aligned with directory structure.

## 2. Reading (15 min)
- **Clean Code Chapter 5: Formatting (pp. 77-96)** – emphasise readability, vertical openness, and logical grouping.
- Summary: Physical structure should mirror logical structure. Developers must discover behaviour quickly.

## 3. This Week’s Work
- Move mapper, validator, business rules into dedicated folders (`Services/Tasks/Mapping`, `.../Validation`, `.../Rules`).
- Create `Extensions/` modules for shared helpers (e.g., `ServiceCollectionExtensions`).
- Update namespaces to match new folders. Remove unused helpers.

## 4. Files to Modify
- `TaskFlowAPI/Services/Tasks/*`
- `TaskFlowAPI/Extensions/*`
- `TaskFlowAPI/Program.cs` (update using statements)
- `TaskFlowAPI.Tests` (fix namespaces where necessary)

## 5. Step-by-Step Instructions
1. Branch `week-14/<your-name>`.
2. Inspect `TaskService` and related classes; identify any lingering nested classes or TODO comment referencing monolith.
3. Create new subfolders: `Services/Tasks/Mapping`, `Services/Tasks/Validation`, `Services/Tasks/Rules`, `Services/Tasks/Filters` (already present—confirm naming).
4. Move files into appropriate folders and update namespaces.
5. Introduce `Extensions/ServiceCollectionExtensions.cs` consolidating DI registrations (repositories, services, filters, validators). Call it from `Program.cs`.
6. Delete any duplicate helper files or unused folder junk (e.g., old `Utils/Helpers.cs` if present).
7. Run build/tests to ensure namespaces and DI still work.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```

## 7. Success Criteria
- Directory structure reflects modules (Controllers, Services/Tasks/…, Validators, etc.).
- No circular namespace dependencies.
- DI registrations centralised via extension method.
- Build/tests succeed; git diff shows moves not rewrites (use `git mv`).

## 8. Submission Process
- Commit `Week 14 – file organization` (use `git mv` to preserve history).
- PR summary includes tree snippet of new structure.
- Weekly issue attaches screenshot from IDE solution explorer.

## 9. Discussion Prep
- How does the new structure improve onboarding for new devs?
- What naming conventions did you adopt for namespaces?
- Did you remove any dead files? Share before/after impact.

## 10. Time Estimate
- 10 min – Plan folder structure.
- 35 min – Move files + update namespaces/DI.
- 15 min – Build/test + PR/issue.
**Total:** ~60 minutes.

## 11. Getting Help
- Ask in chat for review of proposed folder tree before large moves.
- Office hours: live support for `git mv` vs. manual copy.
- Mentor escalation if DI or namespace resolution breaks.
