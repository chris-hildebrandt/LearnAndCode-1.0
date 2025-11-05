# Week 5 · AI Tools & Prompt Engineering

## 1. Learning Objectives
- Understand the strengths and limitations of Large Language Models in day-to-day engineering.
- Craft effective prompts that accelerate TaskFlow work (naming audits, refactors, documentation).
- Record ethical guardrails and escalation paths when AI output conflicts with Quality Manifesto values.

## 2. Reading (60 min)
- **The Prompt Engineering Guide** – Dario Amodei et al. (core sections on prompt patterns).
- **What are Large Language Models?** (Elastic) – overview of LLM capabilities and constraints.
- **AI Safety Fundamentals** (Alignment Forum) – skim sections on responsible usage.
- **llm.txt** (repo root) – In Time Tec AI usage policy.

## 3. This Week’s Work
- Experiment with at least **three** AI-powered tools (e.g., GitHub Copilot, Cursor, Perplexity, Claude/GPT playground) using real TaskFlow code or docs.
- Design two prompt playbooks:
  1. Refactoring support (e.g., helper extraction for Week 4 work).
  2. Documentation summarisation (e.g., comment cleanup insights from Week 3).
- Document findings, risks, and follow-up tasks in `docs/week-05-ai-tools.md#journal` section (add a short summary at the bottom of this file).
- Update `llm.txt` if you discover new do/don’t rules worth sharing (optional, coordinate with mentor).

## 4. Files to Modify
- This file (`docs/week-05-ai-tools.md`) – append your journal paragraph.
- `llm.txt` (optional enhancements approved by mentor).
- Any scratchpads or prompt logs you maintain (link from PR description).

## 5. Step-by-Step Instructions
1. Branch `week-05/<your-name>`.
2. Review `llm.txt` so you operate within policy.
3. Select three AI tools and define the TaskFlow scenario you will target.
4. Iterate on prompts; capture best version + produced insights (screenshots or text in journal).
5. Identify one risk per tool (hallucination, stale context, over-reliance) and mitigation.
6. Summarise outcomes in the Journal section of this doc (add a new bullet list under “Learner Notes”).
7. If you modified code/config while experimenting, run build/tests.

## 6. How to Test
```bash
dotnet build TaskFlowAPI.sln
dotnet test TaskFlowAPI.sln
```
- Only required if you committed code changes based on AI suggestions.

## 7. Success Criteria
- Journal captures tool name, prompt strategy, result, and risk for each AI tool.
- Any AI-generated code is reviewed manually before keeping.
- Updated `llm.txt` (if modified) aligns with Quality Manifesto values and mentor approval.

## 8. Submission Process
1. Commit `Week 05 – AI prompt engineering`.
2. PR summary links to journal bullets and attaches screenshots/logs as needed.
3. Weekly issue includes a brief comparison table of AI tools evaluated.

## 9. Journal and Discussion Prep
Journal (add responses under **Learner Notes** at the end of this file):
*Prompt Evolution:	Which prompt iteration delivered the best balance of accuracy and brevity?

*Human Oversight:	Describe a time AI output was misleading. How did you detect and correct it?

Discussion Prep:
- Share your favourite prompt template and the scenario it solves.
- What signals tell you to stop iterating with AI and switch to manual investigation?
- How will you communicate AI-derived insights to your mentor or teammates?
- Which future TaskFlow assignments could benefit from AI assistance, and which should remain manual?

## 10. Time Estimate
- 60 min – Reading + tool setup.
- 45 min – Prompt experimentation + documentation.
- 15 min – PR/issue + sharing artefacts.
**Total:** ~120 minutes.

## 11. Getting Help
- Ask in chat if unsure whether a prompt violates policy.
- Office hours: review prompt outcomes or iterate live with instructor.
- Mentor escalation if AI behaviour raises ethical or security concerns.

---

### Learner Notes
- *(Add your journal bullet points here before submitting.)*

