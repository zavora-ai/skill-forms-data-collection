# Forms & Data Collection Skill

> Form builder for AI agents — create forms with validated fields, publish, collect submissions, and analyze response patterns via mcp-forms.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--forms-green)](https://github.com/zavora-ai/mcp-forms)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Build Form | 3-4 | Create + add fields + validate + publish |
| Collect Responses | 1-2 | Submit + server-side validation |
| Analyze | 1-2 | Completion rates, averages, distribution |

### Without this skill:
- Forms created without validation rules
- No server-side validation (client-only = bypassable)
- Response data unanalyzed
- No consent notices for data collection

### With this skill:
- Every field has type-appropriate validation
- Server-side validation enforced
- Response analytics with completion rates and distributions
- Data minimization and consent built in

## Installation

```bash
git clone https://github.com/zavora-ai/skill-forms-data-collection.git \
  ~/.skills/skills/forms-data-collection
```

## Requirements

**Required:** `mcp-forms` (11 tools)

**Cross-MCP:**
- `mcp-crm` — lead capture forms → CRM contacts
- `mcp-email` — survey distribution
- `mcp-customer-service` — feedback forms → action items

## Folder Structure

```
forms-data-collection/
├── SKILL.md                       # Decision tree + workflows + validation rules
├── scripts/
│   └── analyze_responses.py       # Completion rate + rating distribution calculator
├── references/
│   ├── tool-sequences.md          # 11 tools
│   ├── cross-mcp-workflows.md     # Forms + CRM + Email + CS
│   └── examples.md                # Build form, analyze responses
├── README.md
└── LICENSE
```

## Example

**User:** "Create a customer feedback form"

**Result:**
```
✅ Form published: https://forms.company.com/f/abc
Fields: satisfaction (1-5 rating), feature used most (select), suggestions (text)
```

## Scripts

### `analyze_responses.py`
```bash
python scripts/analyze_responses.py '{"submissions": [{"rating": 4}, {"rating": 5}, ...]}'
# → {"total": 85, "completion_rate": 72.0, "avg_rating": 4.2}
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on form/survey queries |
| Validation | 100% server-side validation on required fields |
| Data minimization | Only collect what's needed |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
