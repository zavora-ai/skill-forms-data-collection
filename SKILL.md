---
name: forms-data-collection
description: Build and manage forms — create forms, add fields with validation, publish, collect submissions, and analyze responses. Use when creating forms, building surveys, reviewing submissions, validating input, or analyzing response data.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [list_forms, get_form, create_form, add_field, publish_form, submit_form, validate_submission, list_submissions, get_submission, get_analytics, delete_form]
tags: [communication, forms, surveys, data-collection]
metadata:
  author: Zavora AI
  mcp-server: mcp-forms
---

# Forms & Data Collection

Build forms with validation, collect submissions, and analyze responses. Always validate server-side.

## Decision Tree
```
├── "create form", "build survey"? → create_form + add_field + publish_form
├── "submissions", "responses"? → list_submissions / get_submission
├── "analytics", "results"? → get_analytics
├── "validate"? → validate_submission
```

## MUST DO
- Validate all input server-side
- Include consent notices for data collection
- Set submission limits to prevent abuse

## MUST NOT DO
- Don't collect more data than needed (data minimization)
- Don't skip validation on required fields
