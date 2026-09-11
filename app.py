from datetime import datetime

PROJECT_NAME = "DevTrack"

def create_task(title, description, priority="Medium"):
"""Create a new task for the project."""
if not title.strip():
raise ValueError("Task title cannot be empty")

```
if priority not in ["Low", "Medium", "High"]:
    raise ValueError("Invalid priority")

return {
    "title": title,
    "description": description,
    "priority": priority,
    "status": "Pending",
    "created_at": datetime.now().strftime("%Y-%m-%d")
}
```

def update_task_status(task, status):
"""Update the status of an existing task."""
valid_statuses = ["Pending", "In Progress", "Completed"]

```
if status not in valid_statuses:
    raise ValueError("Invalid task status")

task["status"] = status
return task
```

def get_project_summary(tasks):
"""Return a summary of tasks in the project."""
return {
"project": PROJECT_NAME,
"total_tasks": len(tasks),
"completed": sum(
1 for task in tasks if task["status"] == "Completed"
),
"pending": sum(
1 for task in tasks if task["status"] == "Pending"
)
}

if **name** == "**main**":
task = create_task(
"Implement login API",
"Develop and test the user authentication endpoint",
"High"
)

```
update_task_status(task, "In Progress")

summary = get_project_summary([task])

print("Project:", PROJECT_NAME)
print("Task:", task)
print("Summary:", summary)
```
