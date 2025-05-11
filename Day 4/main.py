from csv_operator import read_tasks,show_tasks,add_task,edit_task,remove_task, save_tasks
from complementary_features import random_task_pickup, show_analytics

def main():
    file_path = "tasks.csv"
    tasks = read_tasks(file_path)

    while True:
        print("\n=== YOUR TASKS: ===")
        show_tasks(tasks)
        print("\nMenu:")
        print("1. Add a task")
        print("2. Edit a task")
        print("3. Delete a task")
        print("4. Pick up a random task to complete")
        print("5. Show analytics")
        print("6. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_task(tasks)
            save_tasks(file_path, tasks)
        elif option == "2":
            edit_task(tasks)
            save_tasks(file_path, tasks)
        elif option == "3":
            remove_task(tasks)
            save_tasks(file_path, tasks)
        elif option == "4":
            pickup_task = random_task_pickup(tasks)
            print(f"You should complete the task: {pickup_task['task']}")
        elif option == "5":
            show_analytics(tasks)
        elif option == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()