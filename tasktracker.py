from schooltasks import SchoolTasks
class TaskTracker(SchoolTasks):
    def _init_(self, task_type):
        super()._init_(self)
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
            if isinstance(task_item, tuple):
                date, task, complete_date = task_item
                string += f"Task {index} Date: {date} Task: {task} Completed: {complete_date}\n"
            else:
                string += f"Task {index} Task: {task_item}\n"
        return string