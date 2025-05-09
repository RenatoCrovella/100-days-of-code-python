import csv
from colorama import init, Fore

init(autoreset=True)

user_name = input('how would you like to be called? ')
print(f"Right, so you'll be called {user_name}.")
print("Loading your tasks list. Please, wait for a few seconds.")

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

def show_tasks(csv_path):
    try:
        with open(csv_path, newline="", encoding='utf-8') as task_file:
            reader = csv.DictReader(task_file)
            for line in reader:
                task = line['task']
                status = line['status'].strip().lower()
                if status not in colors:
                    status = 'unknown'
                color = colors.get(status)
                task_amounts[status] += 1
                print(f"{task} | Status: {color}{status}")
    except FileNotFoundError:
        print("CSV file not found.")
    except KeyError:
        print("Error: The CSV file must contain the columns 'task' and 'status'.")

def add_task(csv_path):
    try:
        with open(csv_path, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['task', 'status'])
            new_task = input("What would you like the task to be added? ")
            new_status = input("What would be the task status? ")
            writer.writerow({'task': new_task, 'status': new_status})
            print(f"{new_task} was added to the file with a {new_status} status.")
    except FileNotFoundError:
        print("CSV file not found.")
    except KeyError:
        print("Error: The CSV file must contain the columns 'task' and 'status'.")

show_tasks('tasks.csv')
print(f"Check your 'tasks score' below: \n {task_amounts}")
add_a_task = input("Would you like to add a new task? Type Y (yes) or N (no)")
if add_a_task.lower() == 'y' or add_a_task.lower() == 'yes':
    add_task('tasks.csv')
print(f"That's all for today. Thanks, {user_name}")