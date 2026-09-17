VALID_PRIORITIES = {"Low", "Medium", "High"}
VALID_STATUSES = {"Pending", "In Progress", "Completed"}


def create_task(title, description, priority="Medium"):
	"""Create a validated DevTrack task."""
	if not isinstance(title, str) or not title.strip():
		raise ValueError("Task title cannot be empty")
	if priority not in VALID_PRIORITIES:
		raise ValueError("Priority must be Low, Medium, or High")

	return {
		"title": title.strip(),
		"description": description,
		"priority": priority,
		"status": "Pending",
	}


def update_task_status(task, status):
	"""Update a task status after validating the requested value."""
	if status not in VALID_STATUSES:
		raise ValueError("Status must be Pending, In Progress, or Completed")
	task["status"] = status
	return task


def get_project_summary(tasks):
	"""Return counts of tasks grouped by status and priority."""
	summary = {
		"total": len(tasks),
		"by_status": {status: 0 for status in VALID_STATUSES},
		"by_priority": {priority: 0 for priority in VALID_PRIORITIES},
	}
	for task in tasks:
		summary["by_status"][task["status"]] += 1
		summary["by_priority"][task["priority"]] += 1
	return summary


if __name__ == "__main__":
	sample_task = create_task(
		"Prepare release checklist",
		"Review deployment steps before the next release.",
		priority="High",
	)
	update_task_status(sample_task, "In Progress")
	project_summary = get_project_summary([sample_task])
	print("Task:", sample_task)
	print("Project summary:", project_summary)
