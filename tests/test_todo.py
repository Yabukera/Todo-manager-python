import pytest
import os
import json
from todo import add_task, list_tasks, complete_task, delete_task, load_todos

TEST_FILE = "test_todos.json"

@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup: backup original data
    if os.path.exists("todos.json"):
        os.rename("todos.json", "todos_backup.json")
    
    # Use test file
    global DATA_FILE
    DATA_FILE = TEST_FILE
    
    yield  # Run tests
    
    # Teardown
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists("todos_backup.json"):
        os.rename("todos_backup.json", "todos.json")

def test_add_task():
    add_task("Test task")
    todos = load_todos()
    assert len(todos) == 1
    assert todos[0]["description"] == "Test task"

def test_complete_task():
    add_task("Task to complete")
    complete_task(1)
    todos = load_todos()
    assert todos[0]["completed"] is True

def test_delete_task():
    add_task("Task to delete")
    delete_task(1)
    todos = load_todos()
    assert len(todos) == 0
