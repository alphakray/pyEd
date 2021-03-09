import random
win_number=random.randint(1,100)
guess=1
user_number=int(input("Enter a number between 1 to 100 : "))
game_over=False
while not game_over:
    if user_number==win_number:
        print(f"you WIN!!!, attemps taken {guess}")
        game_over=True
    else  :
        if user_number > win_number:
            print("Too high")
          
        else:
            print("Too low")
        guess+=1
        user_number=int(input("guess again :"))
