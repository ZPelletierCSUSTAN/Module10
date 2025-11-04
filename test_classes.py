def main():
    #The Todo class
    from Todo import Todo
    Todo = Todo()
    Todo.addTask("Make the bed")
    Todo.addTask("Do homework")
    Todo.addTask("Check email")
    print(repr(Todo))
    
    #The SchoolTask class
    from schooltasks import SchoolTasks
    school = SchoolTasks()
    school.addTask("11/4/2025", "Write Essay")
    school.addTask("11/4/2025", "Read Chapter 10")
    school.addTask("11/4/2025", "Complete Online Programming Quiz")
    print(repr(school))
    print(school)

    # The TaskTracker class
    from tasktracker import TaskTracker
    tracker = TaskTracker("workout for the day")
    tracker.addTask("11/01/2025", "Deadlift")
    tracker.addTask("11/01/2025", "Run 3 miles")
    tracker.addTask("11/05/2025", "Swim 50 laps")
    tracker.addTask("11/02/2025", "HIIT Training")
    print(repr(tracker))  
    tracker.removeTask("Deadlift")
    print(repr(tracker))        
    print(str(tracker))

    #call generate_list
    generate_list(Todo)
    generate_list(school)
    generate_list(tracker)
    
    
def generate_list(t):
    from Todo import Todo
    if not isinstance(t, Todo):
        print("not Todo List")
        return NotImplemented
    print("Generate List Function")
    print(t)







main()