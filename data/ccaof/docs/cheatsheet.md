# CCAO-F cheat sheet

## The exam

| | |
| --- | --- |
| Code | CCAO-F, Claude Certified Associate – Foundations |
| Items | 60, multiple choice and multiple response; each item says how many to pick |
| Time | 120 minutes |
| Pass | 720 on a scaled 100–1,000 |
| Fee | 99 USD |
| Audience | Business and technical people who use Claude's apps, not builders |

| Domain | Weight |
| --- | --- |
| Output evaluation and validation | 21% |
| Workflow integration and solution design | 16% |
| Governance, risk and responsible use | 15% |
| Prompting and task execution | 14% |
| Product and model selection | 12% |
| Configuration and knowledge management | 12% |
| Troubleshooting and optimisation | 10% |

Output evaluation is the biggest single domain: a fifth of the paper is about checking what Claude produced before you rely on it.

## Rules that decide most questions

1. **Verify before you share.** Specific-looking details such as citation numbers, figures and quotes can be wrong. Check them against the source, especially for compliance, legal or customer audiences. Claude's own confidence is not evidence.
2. **Bring in a human when the stakes are high.** Decisions about people, legal or medical advice, money and anything published need human review.
3. **Remove sensitive data before you upload it.** Anonymise or redact personal and regulated data as your policy requires. Telling Claude "don't keep this" is not a control.
4. **Match the model and the feature to the task.** Fast, low-cost models for simple high-volume work; more capable models and more effort for complex reasoning.
5. **Break big tasks into steps** and iterate on the prompt: give context, say what good looks like, show an example, and refine from the output you get.
6. **Fix the cause.** Poor output usually means missing context, vague instructions or stale knowledge files, not a broken model.

## Which feature for which job

| Need | Use | Why |
| --- | --- | --- |
| A quick question or a one-off draft | A normal chat | No setup needed |
| Repeated work on the same material, with shared context | A Project with instructions and knowledge files | Each project has its own chats, knowledge base and instructions |
| A simple current fact | Web search | One or two searches |
| Hard reasoning that needs no new web information | Extended thinking or a higher effort level | More reasoning, no browsing |
| An in-depth, multi-source report with citations | Research | Runs many searches that build on each other, over a few minutes |
| Something you would put in front of someone: a document, deck, dashboard or small tool | An artifact | Opens beside the chat and can be edited, reused and shared |
| Analysing a CSV or creating Excel, Word, PowerPoint or PDF files | Code execution and file creation, plus the built-in skills | Claude runs code in a sandbox and produces the files |
| Working with your email, calendar, drive or other tools | Connectors | Claude can read, and with your approval act, using your own permissions |
| A repeatable workflow or house style | A Skill | Instructions and resources that load only when relevant |
| A chat that must not be saved or remembered | An incognito chat | Not saved to history or memory |

Sources: [Research](https://support.claude.com/en/articles/11088861-use-research-on-claude), [When to use web search, extended thinking or Research](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research), [Artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them), [Skills](https://support.claude.com/en/articles/12512176-what-are-skills), [Files](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude).

## Projects and knowledge

- A Project is a workspace with its own chat history, **knowledge** (uploaded documents, text or code used as background) and **instructions** (tone, role, perspective). ([What are Projects](https://support.claude.com/en/articles/9517075-what-are-projects))
- On paid plans, when project knowledge nears the context limit, Claude switches to retrieval (RAG mode) automatically, which expands capacity up to about ten times. (same page)
- On Team and Enterprise plans, projects can be shared with people, groups or the whole organisation: **Can view** members chat with the project but cannot change it; **Can edit** members change instructions and knowledge and manage members. (same page)
- Keep knowledge current: replace outdated files rather than adding new versions beside them, or Claude may draw on the stale one.
- Each project has its own memory, separate from other projects and from chats outside projects. ([Chat search and memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context))

## Connectors

- Connectors let Claude retrieve data from apps and take actions there, and Claude inherits **your** permissions in the connected service. ([Connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities))
- On Team and Enterprise, an Owner or Primary Owner enables each connector for the organisation, then each person connects their own account. Owners can restrict actions org-wide, for example to read-only. (same page)
- Google Workspace connectors can search and read Gmail, Calendar and Drive and, with approval, draft, send, schedule or move items. By default Claude asks for approval before each action. ([Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors))
- Custom connectors to remote MCP servers can be added; on Team, only Owners or Primary Owners add them. Turn off write tools you do not need. ([Custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp))

## Memory, chat search and incognito

- **Chat search** finds and uses relevant past chats (paid plans); inside a project it searches only that project's chats. ([Chat search and memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context))
- **Memory** is on by default for individual plans; on Team and Enterprise, owners decide whether it is available. You can view, edit or delete memories under Settings, pause memory, or reset it. (same page)
- **Incognito chats** are not saved to history or memory. (same page)
- Deleting a chat does not remove memories already created from it; edit or delete those memories directly. (same page)

## Long chats, limits and models

- Usage limits apply across claude.ai, Claude Desktop and Claude Code; paid plans have a session limit that resets every five hours plus weekly limits. Long chats use more of your limit. ([Usage and length limits](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work))
- When a long chat gets close to the limit or drifts off topic, start a new chat, carrying over a short summary, or move the work into a Project. Remove files and connectors you no longer need. (same page)
- You can switch models mid-chat; the change applies from the next response. Effort and thinking are separate controls; raise them for maths, hard analysis or planning. ([Change model, effort and thinking](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings))
- Haiku is the fast, low-cost choice for simple high-volume work; Sonnet balances speed and capability; Opus and Fable are for the most demanding reasoning.

## Data and privacy

- Consumer plans (Free, Pro, Max): chats are used to improve models only if the model-improvement setting is on. Incognito chats are never used. ([How long do you store my data](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data))
- Commercial plans (Team, Enterprise and the API): inputs and outputs are not used for training by default. The exception is feedback you send (thumbs up or down) or another explicit opt-in. ([Is my data used for training](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training))
- Deleting a chat removes it from your history at once and from Anthropic's systems within 30 days. (consumer data page above)
- Follow your organisation's AI policy: which data may be uploaded, which connectors are approved, and when output needs review.

## Validating output: a quick checklist

- Are names, numbers, dates and citations correct against the source?
- Is anything important missing, or is something stated more confidently than the evidence allows?
- Is the tone and level right for the audience?
- Could the output be biased, for example in how it describes or ranks people?
- Does it need a human reviewer before it is used or sent?

Anthropic's guidance on reducing errors: let Claude say it doesn't know, ask it to quote the source first for long documents, and have it cite sources for each claim. ([Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations))
