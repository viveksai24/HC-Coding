from datetime import datetime

# Memento Pattern
class TaskMemento:
    def __init__(self, task):
        self.task = task

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def mark_pending(self):
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        return f"{self.description} - {status}{due_date_str}"

# Builder Pattern
class TaskBuilder:
    def __init__(self, description):
        self.task = Task(description)

    def set_due_date(self, due_date):
        self.task.due_date = due_date
        return self

    def set_completed(self, completed):
        self.task.completed = completed
        return self

    def build(self):
        return self.task

# To-Do List Manager
class ToDoListManager:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, description, due_date=None):
        task = TaskBuilder(description).set_due_date(due_date).build()
        self.tasks.append(task)
        self.history.append(TaskMemento(task))

    def mark_completed(self, description):
        task = next((t for t in self.tasks if t.description == description), None)
        if task:
            task.mark_completed()
            self.history.append(TaskMemento(task))

    def delete_task(self, description):
        self.tasks = [t for t in self.tasks if t.description != description]
        # Note: Deletion is not added to the history for simplicity

    def view_tasks(self, filter_type="all"):
        filtered_tasks = self.tasks if filter_type == "all" else [t for t in self.tasks if t.completed == (filter_type == "completed")]
        for task in filtered_tasks:
            print(task)

    def undo(self):
        if len(self.history) > 1:
            self.history.pop()
            self.tasks = [memento.task for memento in self.history]

# Example Usage
todo_manager = ToDoListManager()

todo_manager.add_task("Buy groceries", due_date="2023-09-20")
todo_manager.add_task("Complete project", due_date="2023-09-25")

todo_manager.view_tasks("all")

todo_manager.mark_completed("Buy groceries")

todo_manager.view_tasks("completed")

todo_manager.undo()

todo_manager.view_tasks("all")
