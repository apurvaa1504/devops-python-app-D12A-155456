```python
import json


def print_json(title: str, payload: dict) -> None:
    print(f"\n=== {title} ===")
    print(json.dumps(payload, indent=2))


def analyze_ticket(ticket: dict) -> dict:
    return {
        "status": "analyzed",
        "ticket_key": ticket.get("jira_key"),
        "summary": ticket.get("summary")
    }


if __name__ == "__main__":
    sample_ticket = {
        "jira_key": "TEST-123",
        "summary": "Sample Jira ticket"
    }

    result = analyze_ticket(sample_ticket)

    print_json("TICKET ANALYSIS", result)
```
