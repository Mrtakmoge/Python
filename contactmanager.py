
contact={}

def addcontact():
    global contact
    n=int(input("ENter the no. of contact you want to add:"))
    for i in range(n):
        name=input("Enter contact name:")
        mob=int(input("Enter Mobile number:"))
        contact[name]=mob
        print("="*10)
        print("contact added successfully...")
        
def showallcontact():
    global contact
    if len(contact)==0:
        print("No contacts")
    else:
        for name,value  in enumerate(contact.items()):
            print(name,value)
    
def deletecontact():
    global contact
    for i in enumerate(contact.items()):
            print(i)
    n=list(contact.keys())
    i=int(input("Enter index num to delete::"))
    contact.pop(n[i])
    print("Contact removed successfully...")
 
        

while True:
    print("1.View contacts")
    print("2.add contacts")
    print("3.delete contact")
    choice=int(input("ENter your option: "))
    if choice==1:
        print("="*20)
        showallcontact()
        print("="*20)
    elif choice==2:
        print("="*20)
        addcontact()
        print("="*20)
    elif choice==3:
        print("="*20)
        deletecontact()
        print("="*20)
    elif choice==4:
        print("="*20)
        print("Program ended....")
        exit()
    else:
        print("Invalid option")
            
    