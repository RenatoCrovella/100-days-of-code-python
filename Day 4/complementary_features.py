from random import randint, choice

task_amounts = {
    "fail": 0,
    "on progress": 0,
    "done": 0,
    "on review": 0,
    "pending": 0,
    "unknown": 0,
    "other": 0
}

def random_task_pickup(tasks):
    return choice(tasks)

def show_analytics(tasks):
    print(f"You have tasks {len(tasks)} in your list.")
    for task in tasks:
        status = task['status'].strip().lower()
        if status not in task_amounts:
            status = "other"
        task_amounts[status] += 1
    for status, value in task_amounts.items():
        print(f"{status:<12} -------> {value:<5}")
