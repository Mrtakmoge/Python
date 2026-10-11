import random

choice=["rock","paper","scissor"]


while True:
    computer=random.choice(choice)
    print(computer)
    userguess=input("Enter Rock,Paper,Scissor :")
    
    if userguess==computer:
        print("Its a Tie")
    elif (userguess=="rock" and computer=="scisssor") or (userguess=="paper" and computer=="rock") or (userguess=="scissor" and computer=="paper"):
        print("You won")
        exit()
    else:
        print("You loose")
        print("Userguess: "+userguess,"computer guess: "+computer)
    
        
    