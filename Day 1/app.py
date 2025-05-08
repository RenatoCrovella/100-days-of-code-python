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
    "pending": Fore.WHITE
}

def show_tasks(csv_path):
    try:
        with open(csv_path, newline="", encoding='utf-8') as task_file:
            reader = csv.DictReader(task_file)
            for line in reader:
                task = line['task']
                status = line['status'].strip().lower()
                color = colors.get(status)
                print(f"{task} | Status: {color}{status}")
    except FileNotFoundError:
        print("CSV file not found.")
    except KeyError:
        print("Error: The CSV file must contain the columns 'tasks' and 'status'.")

# Use o caminho para seu arquivo CSV
show_tasks('tasks.csv')

print(f"That's all for today. Thanks, {user_name}")