import pytest

from app import create_task, update_task_status, get_project_summary

def test_create_task():
task = create_task(
"Implement login API",
"Develop authentication endpoint",
"High"
)

```
assert task["title"] == "Implement login API"
assert task["priority"] == "High"
assert task["status"] == "Pending"
```

def test_update_task_status():
task = create_task(
"Fix database issue",
"Resolve connection timeout",
"Medium"
)

```
updated_task = update_task_status(task, "Completed")

assert updated_task["status"] == "Completed"
```

def test_project_summary():
tasks = [
create_task("Task 1", "First project task", "High"),
create_task("Task 2", "Second project task", "Medium")
]

```
update_task_status(tasks[0], "Completed")

summary = get_project_summary(tasks)

assert summary["project"] == "DevTrack"
assert summary["total_tasks"] == 2
assert summary["completed"] == 1
assert summary["pending"] == 1
```

def test_invalid_priority():
with pytest.raises(ValueError):
create_task(
"Test task",
"Testing invalid priority",
"Critical"
)
