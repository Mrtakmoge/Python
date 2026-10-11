tasks=[]

while True:
    print("1.view tasks")
    print("2.add tasks")
    print("3.remove tasks")
    print("Exit")
    
    
    op=int(input("Enter option:"))
    
    if op==1:
        if len(tasks)<=0:
            print("*"*10)
            print("No Tasks available")
            print("*"*10)
        else:
            print("*"*10)
            print(*tasks,sep="\n")
            print("*"*10)

    elif op==2:
        print("*"*10)
        n=int(input("Enter no. of tasks u want to add"))
        for i in range(n):
            nameoftasks=input("Enter task name:")
            tasks.append(nameoftasks)
            print("*"*10)
            print("Task added succesfully....")
            print("*"*10)
    elif op==3:
        name=input("Enter name of task to remove:")
        tasks.remove(name)
        print("Removal successful...")
    elif op==4:
        exit()
        
        


