import csv
from colorama import Fore, Style

colors = {
    "fail": Fore.RED,
    "on progress": Fore.YELLOW,
    "done": Fore.GREEN,
    "on review": Fore.BLUE,
    "pending": Fore.WHITE,
    "unknown": Fore.MAGENTA
}

task_amounts = {
    "fail": 0,
    "on progress": 0,
    "done": 0,
    "on review": 0,
    "pending": 0,
    "unknown": 0
}

def read_tasks(csv_path):
    tasks = []
    try:
        with open(csv_path, newline="", encoding='utf-8') as task_file:
            reader = csv.DictReader(task_file)
            for line in reader:
                task = line['task']
                status = line['status'].strip().lower()
                if status not in colors:
                    status = 'unknown'
                task_amounts[status] += 1
                tasks.append({
                    'task': task,
                    'status': status
                })
    except FileNotFoundError:
        print("CSV file not found.")
    except KeyError:
        print("Error: The CSV file must contain the columns 'task' and 'status'.")
    return tasks

def show_tasks(tasks):
    print(f"{'Nº':<5}{'TASK':<40} STATUS")
    print("-" * 60)
    for i, task in enumerate(tasks, start=1):
        color = colors.get(task['status'])
        print(f"{i:<5}{task['task']:<40} {color}{task['status']}{Style.RESET_ALL}")

def add_task(tasks):
    task_title = input("How would you like to name the new task? \n")
    task_status = input("What would be the task status? \n")
    task_status = status_validation(task_status)
    tasks.append({
        'task': task_title,
        'status': task_status
    })
    print(f"task {task_title} has been added to the tasks list with the status: {task_status}.")

def remove_task(tasks):
    try:
        index = int(input("\nType the number of the task you want to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_item = tasks.pop(index)
            print(f"{removed_item['task']} has been removed from the tasks list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid entry.")

def edit_task(tasks):
    try:
        index = int(input("\nType the number of the task you want to edit: ")) - 1
        if 0 <= index < len(tasks):
            print("1. Edit title")
            print("2. Edit status")
            choice = input("Chose an option (1 or 2): ").strip()
            if choice == '1':
                new_title = input("New title: ").strip()
                tasks[index]['task'] = new_title
            elif choice == '2':
                print("!! REMEMBER: you should choose one of the status below: !!")
                for keys, value in colors.items():
                    print(f"{Fore.YELLOW}{keys}{Style.RESET_ALL}")
                new_status = input("New status: ").strip().lower()
                new_status = status_validation(new_status)
                tasks[index]['status'] = new_status
            else:
                print("Invalid option.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid entry.")

def save_tasks(csv_path, tasks):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fields = ['task', 'status']
        reader = csv.DictWriter(csv_file, fieldnames=fields)
        reader.writeheader()
        for task in tasks:
            reader.writerow(task)

def status_validation(status):
    if status not in colors:
        while True:
            print("invalid status, please use one of these statuses:")
            for keys, value in colors.items():
                print(f"{Fore.YELLOW}{keys}{Style.RESET_ALL}")
            new_status = input("Type the new status: ")
            if new_status in colors:
                status = new_status
                break
    return status