from controller import TaskController


def display_tasks(tasks):
    for index, task in enumerate(tasks):
        status = "✓" if task.completed else "✗"
        print(f"{index}: [{status}] {task.title}")


def main():
    controller = TaskController()

    while True:
        action = input("Введите 'add' для добавления задачи, 'complete' для завершения задачи, 'exit' для выхода: ")

        if action == 'add':
            title = input("Введите название задачи: ")
            controller.add_task(title)
        elif action == 'complete':
            index = int(input("Введите индекс задачи для завершения: "))
            controller.complete_task(index)
        elif action == 'exit':
            break

        print("Текущие задачи:")
        display_tasks(controller.task_manager.get_tasks())


if __name__ == "__main__":
    main()