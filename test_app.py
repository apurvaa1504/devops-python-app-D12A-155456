```python
from app import analyze_ticket


def test_analyze_ticket():
    ticket = {
        "jira_key": "TEST-123",
        "summary": "Login page is not working"
    }

    result = analyze_ticket(ticket)

    assert result["status"] == "analyzed"
    assert result["ticket_key"] == "TEST-123"
    assert result["summary"] == "Login page is not working"
```
