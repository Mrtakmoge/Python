contact={}

def add_contact():
    global contact
    
    n=int(input("Enter num of contacts you want to add::"))
    for i in range(n):
        name=input("Enter contact name::")
        Mob=int(input('Enter contact num::'))
        contact[name]=Mob
        print("Contact added successfully....")
        
def delete_contact():
    global contact
    
    n=list(contact.keys())
    for i in enumerate(contact.items()):
        print(i)
    i=int(input("Enter index num to delete::"))
    contact.pop(n[i])
    print("Contact removed successfully...")
    
def show_contact():
    global contact
    
    for i in enumerate(contact.items()):
        print(i)
        
while True:
    print("1.Show contact")
    print("2.Add Contact")
    print("3.delete contact")
    print("4.exit")
    op=int(input("Enter your option::"))
    
    if op==1:
        print("="*20)
        show_contact()
        print("="*20)
    elif op==2:
        print("="*20)
        add_contact()
        print("="*20)
    elif op==3:
        print("="*20)
        delete_contact()
        print("="*20)
    elif op==4:
        print("="*20)
        print("Program ended")
        exit()
        print("="*20)
    else:
        print("Invalid Option....")