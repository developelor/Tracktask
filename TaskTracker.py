import os
import sys
import time
import json
from datetime import datetime

TASK_FILE = 'tasks.json'

if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully.')
            return
    print(f'Task {task_id} not found.')

def delete_task(task_id):
    tasks = load_tasks()
    if(input(f"Are You sure you want to delete {task_id} ?(yes/no)").lower() =="yes"):
        tasks = [task for task in tasks if task['id'] != task_id]
        save_tasks(tasks)
        print(f'Task {task_id} deleted successfully.')
    else:
        print(f'Task {task_id} is not deleted .')


def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as in-progress.')
            return
    print(f'Task {task_id} not found.')

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as done.')
            return
    print(f'Task {task_id} not found.')

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    else:
        status="All"

    if(len(tasks) != 0):
        for task in tasks:
            print(f"[{task['id']}] {task['description']} - {task['status']}")
    else:
        print (f'List {status} is Empty')


def GetList():
    result=None
    os.system("cls")
    print("\n Please Choise View Task :\n")
    print("   [0] List all tasks ")
    print("   [1] List tasks : Todo")
    print("   [2] List tasks : in-progress")
    print("   [3] List tasks : Done")
    
    list=input("Choose a menu option, or press Any Key to view All List:")
    match list:
            case "1":
                result="todo"
            case "2":
                result="in-progress"
            case "3":
                result="done"
            case _:
                result=None
    return result

def getMenu():
    os.system("cls")
    print("\n Please Choise :\n")
    print("   [0] List all tasks or filter by status (done, todo, in-progress)")
    print("   [1] Add New Task")
    print("   [2] Update existing tasks")
    print("   [3] Delete tasks")
    print("   [4] Mark tasks as in progress or done")
    print("   [5] Mark tasks as done \n")
    
    choise=input("Choose a menu option, or press Any Key to Exit:")
    match choise:
            case "0":
                list=GetList()
                list_tasks(list)

            case "1":
                description = input("\nPlease Enter Description:")
                if(len(description)>1):
                    add_task(description)
                else:
                    print("The Description should not be empty")

            case "2":
                list_tasks()
                task_id = int(input("\nEnter Task ID:"))
                new_description = input("Enter Description:")
                update_task(task_id, new_description)

            case "3":
                list_tasks()
                task_id = int(input("\nEnter Task ID:"))
                delete_task(task_id)

            case "4":
                list_tasks("todo")
                task_id = int(input("\nEnter Task ID:"))
                mark_in_progress(task_id)

            case "5":
                list_tasks("in-progress")
                task_id = int(input("\nEnter Task ID:"))
                mark_done(task_id)

            case "list":
                if len(sys.argv) == 3:
                    status = sys.argv[2]
                    list_tasks(status)
                else:
                    print("All List")
                    list_tasks()
            case _:
                return False
    return True
                

if __name__ == "__main__":
    os.system("cls")                                
    print(" _____         _  _____         _             ")
    time.sleep(0.03)
    print("|_   _|       | ||_   _|       | |            ")
    time.sleep(0.03)
    print("  | | __ _ ___| | _| |_ __ __ _| | _____ _ __ ")
    time.sleep(0.03)
    print("  | |/ _` / __| |/ / | '__/ _` | |/ / _ \ '__|")
    time.sleep(0.03)
    print("  | | (_| \__ \   <| | | | (_| |   <  __/ |   ")
    time.sleep(0.03)
    print("  \_/\__,_|___/_|\_\_/_|  \__,_|_|\_\___|_|   ")
    time.sleep(0.03)
    print("                                              ")
    print("")

    if len(sys.argv) > 1:
        command = str(sys.argv[1]).lower()
        match command:
            case "add":
                description = sys.argv[2]
                add_task(description)
            case "update":
                task_id = int(sys.argv[2])
                new_description = sys.argv[3]
                update_task(task_id, new_description)
            case "delete":
                task_id = int(sys.argv[2])
                delete_task(task_id)
            case "mark-in-progress":
                task_id = int(sys.argv[2])
                mark_in_progress(task_id)
            case "mark-done":
                task_id = int(sys.argv[2])
                mark_done(task_id)
            case "list":
                if len(sys.argv) == 3:
                    status = sys.argv[2]
                    list_tasks(status)
                else:
                    print("All List")
                    list_tasks()
            case _:
                print("Invalid command.")
        input("\n\nPress any key to exit...")
    else:
        time.sleep(0.5)
        check=True
        while check:
            check=getMenu()
            if not check:
                continue
            i =input("View Menu ? (Y/N) ")
            if(i.lower() == "n"):
                check=False