## Curriculum Comparison Matrix (L1 ↔︎ L2)

| L1 Chunk ID | Theme / Asset | L2 Counterpart(s) | Notes & Gaps |
| --- | --- | --- | --- |
| L1-GEN-README | Program overview (27 weeks) | L2-SUP-README | 2.0 compresses program to 21 weeks with integrated project delivery; 2.0 emphasizes TaskFlow deliverables and stricter expectations. |
| L1-GEN-CODEWS | VS Code workspace config | *(No direct equivalent)* | Tooling guidance removed; could add optional VS Code profile note in 2.0 if needed. |
| L1-WK01-OV | Quality Manifesto intro, project selection | L2-DOC-W01, L2-SUP-QMAN, L2-SUP-CLEAN | 2.0 deepens setup tasks (run API/tests) and adds escalation plan; retains manifesto focus. |
| L1-WK02-OV / L1-WK02-EX / L1-WK02-AS | Meaningful names readings & refactor + JS activity | L2-DOC-W02, L2-DOC-EX01, L2-API-CTRL-TasksController (Week 2 assignment) | 2.0 replaces JS exercise with TaskFlow controller rename; ensures direct project tie-in. |
| L1-WK02-SUB | Sample submission | *(Implicit via L2-DOC standup prompts)* | 2.0 lacks explicit sample submission; consider adding exemplar in docs/examples. |
| L1-WK03-OV | Prompt engineering foundations | L2-DOC-W03 | 2.0 pivots to functions/comments; AI prompt engineering removed (gap if still desired). |
| L1-WK03-SUB | AI tooling reflection | *(No equivalent)* | Represents removed AI focus; note as potential supplemental topic. |
| L1-WK04-OV / L1-WK04-EX | Clean functions principles | L2-DOC-W03 (functions) & inline TaskFlow TODOs | 2.0 merges Week 3 functions/comments with TaskFlow-specific refactor tasks. |
| L1-WK05-OV / L1-WK05-EX / L1-WK05-AS | Git intro + activity | L2-DOC-W04 | 2.0 integrates Git workflow with TaskFlow branches; activity now centered on repo PR template. |
| L1-WK05-SUP | Week reflections | *(No direct doc)* | Reflection prompts embedded in L2 weekly doc journal sections. |
| L1-WK06-OV | Advanced Git | L2-DOC-W04 (sec on branching/PR) | 2.0 condenses Git coverage into one week; advanced Git depth reduced. |
| L1-WK07-OV / L1-WK07-EX | Code review practices | L2-DOC-W18 | Code review shifted later (Week 18) aligned with full-project reviews; emphasizes collaboration/retro. |
| L1-WK07-SUP | Reflection sample | *(No direct equivalent)* | 2.0 uses discussion prep sections for journaling. |
| L1-WK08-OV / L1-WK08-EX / L1-WK08-COMP | Classes & systems part 1 | L2-DOC-W05, L2-API-ENTITIES, L2-API-DATA | 2.0 grounds concepts in TaskFlow domain entities and DbContext. |
| L1-WK08-SUB1-6 | OrderProcessor refactor submissions | L2-API codebase (TasksController, TaskService, filters) | 2.0 uses TaskFlow as unified project; no multi-file sample submissions provided. |
| L1-WK08-SUP | Reflection | Covered by L2 journal prompts | — |
| L1-WK09-OV / EX / CODE* | Classes & systems part 2 + Python exercises | L2-DOC-W06, L2-API-REPO, L2-API-SERV | Shift from Python order system to C# TaskFlow repository/service pattern. |
| L1-WK10-OV / EX | Objects & data structures part 1 | L2-DOC-W05 & W06 combined | 2.0 integrates object/data structure lessons within TaskFlow architecture weeks. |
| L1-WK11-OV | Objects & data structures part 2 | *(Implicit in L2-DOC-W05/06/07)* | 2.0 does not explicitly separate part 2; ensure depth maintained via TaskFlow assignments. |
| L1-WK12-OV / EX | Error handling part 1 | L2-DOC-W08, L2-API-EXT-ExceptionMiddleware, L2-API-EXC* | 2.0 expands with middleware, custom exceptions, FluentValidation tasks. |
| L1-WK13-OV | Error handling part 2 | L2-DOC-W08 (advanced sections) | Content consolidated into single week with deeper tooling. |
| L1-WK14-OV / EX | Boundaries & integrations | L2-DOC-W14, L2-API-PROGRAM (DI), L2-API-HTTP | 2.0 frames boundaries as file organization & layering around API surfaces. |
| L1-WK15-OV / EX | SOLID – SRP | L2-DOC-W09, L2-API-SVC-TaskService | Week 9 TaskFlow assignments enforce SRP by refactoring service responsibilities. |
| L1-WK16-OV / EX | SOLID – OCP | L2-DOC-W10, L2-API-SERV-FLT-* | Filters compose to demonstrate extendable behaviors. |
| L1-WK17-OV / EX | SOLID – LSP | L2-DOC-W11, L2-API-SVC interfaces | LSP applied via interface-driven design; ensure assignments reinforce substitutability. |
| L1-WK18-OV / EX | SOLID – ISP | L2-DOC-W12, L2-API-REPO-INT, L2-API-SERV-INT | 2.0 uses repository/service interfaces for segregation practice. |
| L1-WK19-OV / EX | SOLID – DIP | L2-DOC-W13, L2-API-PROGRAM (DI setup) | 2.0 culminates DIP with DI container finalization. |
| L1-WK20-OV | API design & integration | L2-DOC-W19, L2-API-CTRL, L2-API-HTTP | 2.0 adds swagger/docs deliverables; direct project tie. |
| L1-WK21-OV / EX | Unit testing & TDD | L2-DOC-W15, L2-API-TEST-* | Testing remains but leverages xUnit scaffolding. |
| L1-WK22-OV / EX | Design patterns Part 1 | L2-DOC-W17 (combined patterns) | 2.0 condenses patterns into single week with API-specific refactors. |
| L1-WK23-OV | Design patterns Part 2 | L2-DOC-W17 (advanced sections) | Later-week backlog reduced; ensure coverage of patterns trimmed in 2.0. |
| L1-WK24-OV | Event-driven architecture | *(Gap)* | 2.0 removes dedicated event-driven content; consider optional module if still desired. |
| L1-WK25-OV / EX | Concurrency & performance | L2-DOC-W20 | Maintains focus via API caching/perf tasks. |
| L1-WK26-OV / EX | Refactoring & code smells | L2-DOC-W16, L2-API-SVC-TaskService TODO cleanup | Alignment maintained with targeted smell list. |
| L1-WK27-OV / EX | Documentation & communication | L2-DOC-W21, L2-DOC-FINALRETRO, L2-SUP-WKPROG | 2.0 includes retro template, demo prep, progress tracking. |
| *(L1 additional supplemental files)* | Submission examples, reflections | L2 docs journal & retro templates | 2.0 embeds reflective practice in weekly docs; lacks learner exemplars. |

### Topic Coverage Summary
- **Removed / Condensed in 2.0**: AI prompt engineering (Week 3), event-driven architecture (Week 24), some advanced Git depth, explicit part-2 object/data structure week, learner submission samples.
- **New / Expanded in 2.0**: Full-stack TaskFlow API project, FluentValidation, exception middleware, repository/service/filter architecture, migration management, production-ready expectations (Swagger, caching, coverage), agile ceremonies integration.
- **Mapped 1:Many**: Several legacy weeks map to combined TaskFlow-focused weeks (e.g., L1 Weeks 10–11 to L2 Weeks 5–7). Track to ensure learning objectives from condensed weeks are still met via assignments.

