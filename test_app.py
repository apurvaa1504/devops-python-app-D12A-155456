import pytest

from app import create_task, get_project_summary, update_task_status


def test_create_task():
	task = create_task("Deploy service", "Deploy the latest service build.")

	assert task["title"] == "Deploy service"
	assert task["description"] == "Deploy the latest service build."
	assert task["priority"] == "Medium"
	assert task["status"] == "Pending"


def test_update_task_status():
	task = create_task("Review logs", "Check the latest application logs.")

	updated_task = update_task_status(task, "Completed")

	assert updated_task["status"] == "Completed"


def test_get_project_summary():
	tasks = [
		create_task("Deploy service", "Deploy the latest build.", "High"),
		create_task("Review logs", "Check application logs.", "Low"),
	]
	update_task_status(tasks[0], "Completed")

	summary = get_project_summary(tasks)

	assert summary["total"] == 2
	assert summary["by_status"]["Completed"] == 1
	assert summary["by_status"]["Pending"] == 1
	assert summary["by_priority"]["High"] == 1
	assert summary["by_priority"]["Low"] == 1


def test_reject_invalid_priority():
	with pytest.raises(ValueError, match="Priority"):
		create_task("Deploy service", "Deploy the latest build.", "Urgent")
