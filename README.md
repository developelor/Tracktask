# Task Tracker CLI

Task Tracker is a command-line interface (CLI) application that allows you to manage and track your tasks. You can add, update, delete, and list tasks, as well as mark them as in progress or done. All tasks are stored in a JSON file.

**ترکر تسک** یک برنامه واسط خط فرمان  است که به شما امکان می‌دهد وظایف خود را مدیریت و پیگیری کنید. شما می‌توانید وظایف جدید اضافه کنید، وظایف موجود را به‌روزرسانی کنید، حذف کنید و لیست کنید، همچنین آن‌ها را به عنوان در حال انجام یا انجام شده علامت‌گذاری کنید. همهٔ وظایف در یک فایل JSON ذخیره می‌شوند.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in progress or done
- List all tasks or filter by status (done, todo, in-progress)

## ویژگی‌ها

- اضافه کردن وظایف جدید
- به‌روزرسانی وظایف موجود
- حذف وظایف
- علامت‌گذاری وظایف به عنوان در حال انجام یا انجام شده
- لیست کردن همهٔ وظایف یا فیلتر کردن بر اساس وضعیت (انجام شده، در حال انجام، وظایف جدید)


## Commands

Here are the available commands and their usage:

### Adding a New Task
To add a new task, use the following command:
```bash
python TaskTracker.py add "Task Description"
```
**Example:**
```bash
python TaskTracker.py add "Buy groceries"
```
**Output:**
```
Task added successfully (ID: 1)
```


### Updating a Task
To update an existing task, use:
```bash
python TaskTracker.py update TASK_ID "New Task Description"
```

**Example:**
```bash
python TaskTracker.py update 1 "Buy groceries and cook dinner"
```


### Deleting a Task
To delete a task, use:
```bash
python TaskTracker.py delete TASK_ID
```
**Example:**
```bash
python TaskTracker.py delete 1
```

### Marking a Task as In Progress
To mark a task as in progress, use:
```bash
python TaskTracker.py mark-in-progress TASK_ID
```
**Example:**
```bash
python TaskTracker.py mark-in-progress 1
```


### Marking a Task as Done
To mark a task as done, use:
```bash
python TaskTracker.py mark-done TASK_ID
```
**Example:**
```bash
python TaskTracker.py mark-done 1
```

### Listing All Tasks
To list all tasks, use:
```bash
python TaskTracker.py list
```


### Listing Tasks by Status
To list tasks by their status, use:
```bash
python TaskTracker.py list STATUS
```
**Example for done tasks:**
```bash
python TaskTracker.py list done
```


## Conclusion

This Task Tracker CLI application provides a simple and effective way to manage your tasks from the command line. Feel free to modify and enhance it as per your needs!
