projects = []

def create_project(name, description):
    project = {
        "id": len(projects) + 1,
        "name": name,
        "description": description,
        "tasks": []
    }
    projects.append(project)
    print(f"Проект '{name}' создан!")

def add_task(project_id, task_name, status="В процессе"):
    for project in projects:
        if project["id"] == project_id:
            task = {"name": task_name, "status": status}  # Добавляем статус задачи
            project["tasks"].append(task)
            print(f"Задача '{task_name}' ({status}) добавлена в проект '{project['name']}'")
            return
    print("Проект не найден.")

if __name__ == "__main__":
    print("Система управления проектами")
    create_project("Первый проект", "Тестовый проект для примера")
    add_task(1, "Настроить репозиторий")
    add_task(1, "Написать отчет", "Завершено")  # Добавляем задачу со статусом