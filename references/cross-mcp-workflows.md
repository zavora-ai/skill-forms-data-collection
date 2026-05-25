# Forms Cross-MCP Workflows

## Forms + CRM: Lead Capture
```
FORMS: list_submissions(form_id: "lead_form") → [{name: "Alex", email: "alex@co.com", company: "TechCo"}]
CRM: create_contact(name: "Alex", email: "alex@co.com")
CRM: create_company(name: "TechCo")
CRM: associate_contact_company(contact_id, company_id)
```

## Forms + Customer Service: Feedback → Action
```
FORMS: get_analytics(form_id: "csat_form") → {avg_rating: 3.1, low_scores: 5}
CS: start_conversation(customer_id: low_scorer, subject: "Following up on your feedback")
```

## Forms + Email: Survey Distribution
```
FORMS: publish_form(id: "nps_survey") → {url: "https://forms.co/nps"}
EMAIL: send_email(to: customer_list, subject: "Quick survey — 2 min", body: "Share your feedback: [url]")
```
