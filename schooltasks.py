class Todo:
    def __init__(self):
        self._task_list = []

    def addTask(self, task):
        self._task_list.append(task)

    def __repr__(self):
        return f"Task List: {self._task_list}"

class SchoolTasks(Todo):
    def __init__(self, initial_data=None):
        super().__init__()
        self.initial_data = initial_data

    def addTask(self, task_date, task):
        self._task_list.append((task_date, task))
    
    def __str__(self):
        string = ""
        for index, task_item in enumerate(self._task_list, start=1):
            if isinstance(task_item, tuple):
                date, task = task_item
                string += f"Task {index} Date: {date} Task: {task}\n"
            else:
                string += f"Task {index} Task: {task_item}\n"
        return string

if __name__ == "__main__":
    tasks = SchoolTasks([("11/4/2025", "Write Essay"), ("11/4/2025", "Read Chapter 10")])
    print(tasks)
