# Forms Tool Sequences

## Tools (11)
| Tool | Purpose |
|------|---------|
| `list_forms` | All forms |
| `get_form` | Form structure + fields |
| `create_form` | Create new form |
| `add_field` | Add field with validation |
| `publish_form` | Make form live |
| `submit_form` | Submit response |
| `validate_submission` | Check against rules |
| `list_submissions` | All responses |
| `get_submission` | Single response |
| `get_analytics` | Response stats |
| `delete_form` | Remove form |

## Sequence: Build and Publish (3-4 calls)
```
1. create_form(title: "Customer Feedback", description: "...")
2. add_field(form_id, type: "rating", label: "How satisfied are you?", required: true)
3. add_field(form_id, type: "text", label: "Comments", required: false)
4. publish_form(form_id) → {url: "https://forms.company.com/f/abc"}
```

## Sequence: Analyze Responses (2 calls)
```
1. list_submissions(form_id, limit: 100) → all responses
2. get_analytics(form_id) → {total: 85, avg_rating: 4.2, completion_rate: 72%}
```
