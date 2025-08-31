# Simple To-Do List Application
lst=[]
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task=input("Enter the task: ")
        lst.append(task)
        print("Task added.")
    elif choice==2:
        if len(lst)==0:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i in range(len(lst)):
                print(f"{i+1}.{lst[i]}")
    elif choice==3:
        task=input("enter the task to remove: ")
        if not lst:
            print("No tasks available to remove.")
        elif task in lst:
            lst.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
# Simple To-Do List Application