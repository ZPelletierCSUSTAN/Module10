class Todo:
    def __init__(self):
        self._task_list = []

    def addTask(self, task):
        self._task_list.append(task)

    def __repr__(self):
        return f"Task List: {self._task_list}"

    def __str__(self):
        string = "Generic Todo List\n"
        for index, task_item in enumerate(self._task_list, start=1):
            string += f"Task {index}: {task_item}\n"
        return string

class SchoolTasks(Todo):
    def __init__(self):
        super().__init__()

    def addTask(self, task_date, task):
        self._task_list.append((task_date, task))
    
    def __str__(self):
        string = "School Tasks\n"
        for index, task_item in enumerate(self._task_list, start=1):
            if isinstance(task_item, tuple) and len(task_item) == 2:
                date, task = task_item
                string += f"Task {index} Date: {date} Task: {task}\n"
            else:
                string += f"Task {index} Task: {task_item}\n"
        return string

class TaskTracker(SchoolTasks):
    def __init__(self, task_type):
        super().__init__()
        self._task_type = task_type
        
    def clearTaskList(self):
        self._task_list.clear()

    def removeTask(self, task):
        for i, task_item in enumerate(self._task_list):
            if isinstance(task_item, tuple) and len(task_item) == 3:
                date, task_desc, complete_date = task_item
                if task == task_desc:
                    del self._task_list[i]
                    return
        print(f"Task '{task}' not found.")
        
    def addTask(self, start_date, task, complete_date ="In Process"):
        self._task_list.append((start_date, task, complete_date))
        
    def __str__(self):
        string = self._task_type + "\n"
        for index, task_item in enumerate(self._task_list, start=1):
            if isinstance(task_item, tuple) and len(task_item) == 3:
                date, task, complete_date = task_item
                string += f"Task {index} Date: {date} Task: {task} Completed: {complete_date}\n"
            else:
                string += f"Task {index} Task: {task_item}\n"
        return string

def generate_list(t):
    if not isinstance(t, Todo):
        print("not Todo List")
        return NotImplemented
    print("\n--- Generate List Function ---")
    print(t)

def main():
    todo_list = Todo()
    todo_list.addTask("Make the bed")
    todo_list.addTask("Do homework")
    todo_list.addTask("Check email")
    print(repr(todo_list))
    school = SchoolTasks()
    school.addTask("11/4/2025", "Write Essay")
    school.addTask("11/4/2025", "Read Chapter 10")
    school.addTask("11/4/2025", "Complete Online Programming Quiz")
    print(repr(school))
    print(school)
    tracker = TaskTracker("Workout for the day")
    tracker.addTask("11/01/2025", "Deadlift")
    tracker.addTask("11/01/2025", "Run 3 miles")
    tracker.addTask("11/05/2025", "Swim 50 laps")
    tracker.addTask("11/02/2025", "HIIT Training")
    print(repr(tracker))
    tracker.removeTask("Deadlift")
    print(repr(tracker))
    print(str(tracker))
    generate_list(todo_list)
    generate_list(school)
    generate_list(tracker)
    class Person: pass
    generate_list(Person())

main()






main()