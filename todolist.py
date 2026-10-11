tasks={}

def add_tasks():
    global tasks
    
    n=int(input("Enter no of tasks you want to add:"))
    for i in enumerate(range(n)):
        name=input("Enter task name:")
        tasks[name]="pending"
        print("Task added successfully...")
def check_status():
    global tasks
    
    
    n=list(tasks.keys())
    for i in enumerate(tasks.items()):
        print(i)
    i=int(input("Enter index to change status:"))
    tasks[n[i]]="completed"
    for i in tasks.items():
        print(i)
        
def delete_task():
    global tasks
    n=list(tasks.keys())
    for i in enumerate(tasks.items()):
        print(i)
    i=int(input("Enter index no.:"))
    tasks.pop(n[i])
    print("Task deleted successfully...")
    
def show_tasks():
    if len(tasks)==0:
        print("No tasks...")
    else:
        for i in tasks.items():
            print(i)
            
            
while True:
    print("1.Show All Tasks")
    print("2.add taks")
    print("3.Change status")
    print("4.delete task")
    print("5.Exit")
    op=int(input("Enter option from above::"))
    if op==1:
        print("="*20)
        show_tasks()
        print("="*20)
    elif op==2:
        print("="*20)
        add_tasks()
        print("="*20)
    elif op==3:
        print("="*20)
        check_status()
        print("="*20)
    elif op==4:
        print("="*20)
        delete_task()
        print("="*20)
    elif op==5:
        print("="*20)
        exit()
        print("="*20)
    else:
        print("Invalid option....")
        
    
    
    
        