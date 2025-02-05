from model import TaskManager

class TaskController:
    def __init__(self):
        self.task_manager = TaskManager()

    def add_task(self, title):
        self.task_manager.add_task(title)
        return self.task_manager.get_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.task_manager.tasks):
            self.task_manager.tasks[index].complete()
        return self.task_manager.get_tasks()