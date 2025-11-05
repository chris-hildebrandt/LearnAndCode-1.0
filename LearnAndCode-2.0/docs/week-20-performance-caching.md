# Week 20 · Performance & Caching

## 1. Learning Objectives
- Apply basic performance improvements (async, caching, response compression).
- Instrument simple metrics/logs to validate impact.
- Ensure caching invalidation flows through repository/service layers.

## 2. Reading (15 min)
- Microsoft docs on in-memory caching (`IMemoryCache`).
- Article: “Async best practices in ASP.NET Core”.
- Summary: Cache read-heavy endpoints, always invalidate on writes, avoid blocking calls.

## 3. This Week’s Work
- Add in-memory caching for `GetAllTasksAsync` results (keyed by filter parameters + pagination).
- Ensure cache invalidated on create/update/delete.
- Confirm all repository/service methods use async/await (no `.Result` or `.Wait`).
- Enable response compression middleware if not already active (verify config).

## 4. Files to Modify
- `TaskFlowAPI/Services/Tasks/TaskService.cs`
- `TaskFlowAPI/Services/Tasks/Interfaces` if adding caching abstraction
- `TaskFlowAPI/Program.cs` (cache configuration)
- Optional: add `TaskFlowAPI/Infrastructure/Caching/ITaskCache.cs`, `MemoryTaskCache.cs`
- Update tests to account for caching (e.g., verifying invalidation)

## 5. Step-by-Step Instructions
1. Branch `week-20/<your-name>`.
2. Design caching strategy: create abstraction `ITaskCache` to get/set cached `PagedResponse` by filter signature.
3. Implement `MemoryTaskCache` using `IMemoryCache` with TTL (e.g., 60 seconds) and configurable options.
4. Inject cache into `TaskService`; apply when fetching tasks.
5. Invalidate cache on create/update/delete operations.
6. Verify all repository/service methods use async/await (no leftover synchronous calls).
7. Confirm `app.UseResponseCompression()` is enabled and configure MIME types if needed.
8. Add logging around cache hits/misses for observability.
9. Run build/tests + manual GET to verify caching (log output confirms hits).

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Manual: call `GET /api/v1/tasks` twice and confirm second call logs cache hit.

## 7. Success Criteria
- Cache abstraction introduced; no direct `IMemoryCache` usage outside infrastructure class.
- Cache invalidated after any write operations.
- Async patterns consistent (no synchronous blocking).
- Build/tests succeed; logs show cache activity.

## 8. Submission Process
- Commit `Week 20 – caching & performance`.
- PR summary includes caching strategy, TTL, and sample logs.
- Weekly issue documents performance observations (stopwatch results optional).

## 9. Discussion Prep
- How did caching change the service design?
- What risks exist if cache invalidation fails?
- What metrics would you add in a production environment?

## 10. Time Estimate
- 15 min – Design caching strategy.
- 45 min – Implement cache + async audit.
- 15 min – Testing/log verification + PR/issue.
**Total:** ~75 minutes.

## 11. Getting Help
- Share cache key strategy in chat for review.
- Office hours: debug cache invalidation behaviour.
- Mentor escalation if asynchronous changes cause deadlocks or failing tests.
