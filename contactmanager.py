
dict={}

def addcontact():
    global dict
    n=int(input("ENter the no. of contact you want to ass:"))
    for i in range(n):
        name=input("Enter contact name:")
        mob=int(input("Enter Mobile number:"))
        dict[name]=mob
        print("="*10)
        print("contact added successfully...")
        
def showallcontact():
    global dict
    if len(dict)==0:
        print("No contacts")
    else:
        for name,value  in dict.items():
            print(name,value)
    
def deletecontact():
    global dict
    key=input("Enter name to delete:")
    dict.pop(key)  
    print("="*10)
    print("Delete successful") 
        

while True:
    print("1.View contacts")
    print("2.add contacts")
    print("3.delete contact")
    choice=int(input("ENter your option: "))
    if choice==1:
        showallcontact()
    elif choice==2:
        addcontact()
    elif choice==3:
        deletecontact()
    else:
        print("Invalid option")
            
    