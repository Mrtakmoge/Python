import random
def play_game():
    
    lucky_num=random.randint(1,50)
    
    while True:
        user_num=int(input("Guess the num:"))
        
        if user_num==lucky_num:
            print("Correct Guess\n","You Won The Game")
            break
        elif user_num>lucky_num:
            print("Num is High")
        elif user_num<lucky_num:
            print("Num is Low")
        
play_game()        