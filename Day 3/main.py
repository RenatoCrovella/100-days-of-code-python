from csv_operator import read_tasks,show_tasks,add_task,edit_task,remove_task, save_tasks, task_amounts

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
        print("4. Exit")
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
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()