# Forms Examples

## Example 1: "Create a feedback form"
```
create_form(title: "Product Feedback Q1")
add_field(type: "rating", label: "Overall satisfaction", scale: 5)
add_field(type: "select", label: "Feature used most", options: ["Dashboard", "Reports", "API"])
add_field(type: "textarea", label: "Suggestions")
publish_form(form_id)
```
Response: "✅ Form published: https://forms.company.com/f/abc"

## Example 2: "How are responses looking?"
```
get_analytics(form_id) → {total: 85, avg_rating: 4.2, completion_rate: 72%}
```
Response: "85 responses. Avg satisfaction: 4.2/5. 72% completion rate."
