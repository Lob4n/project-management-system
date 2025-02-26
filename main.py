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

def add_task(project_id, task_name):
    for project in projects:
        if project["id"] == project_id:
            project["tasks"].append(task_name)
            print(f"Задача '{task_name}' добавлена в проект '{project['name']}'")
            return
    print("Проект не найден.")

if __name__ == "__main__":
    print("Система управления проектами")
    create_project("Первый проект", "Тестовый проект для примера")
    add_task(1, "Настроить репозиторий")