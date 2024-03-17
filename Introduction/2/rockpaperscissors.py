#code writed from tutorial 

import random

#init var
computer_score = 0
user_score = 0
computer_choice =""
user_choice=""

#Gameplay 
def RockPaperScissors():
    global computer_score,computer_choice,user_score,user_choice

    y = int(input("please Write number , 1:rock, 2:paper, 3:scissors"))
    match y:
        case 1:user_choice = "rock"
        case 2:user_choice = "paper"
        case 3:user_choice = "scissors"

    x=random.randint(1,3)
    if x==1:
        computer_choice = "rock"
    elif x==2:
        computer_choice = "paper"
    elif x==3:
        computer_choice = "scissors"

    if computer_choice == "rock":
        if user_choice == "paper":
            user_score +=1
            print("hooora Win")
        elif user_choice == "scissors":
            computer_score +=1
            print("oops lose")
        else :
            print("draw")
    elif computer_choice == "paper":
        if user_choice == "rock":
            computer_score +=1
            print("oops lose")
        elif user_choice == "scissors":
            user_score +=1
            print("hooora Win")
        else :
            print("draw")
    elif computer_choice == "scissors":
        if user_choice == "rock":
            user_score +=1
            print("hooora Win")
        elif user_choice == "paper":
            computer_score +=1
            print("oops lose")
        else :
            print("draw")

#How many times run game
Turns=int(input("how many Turn you want play it ?"))
for i in range(Turns):

    RockPaperScissors()

#HighScore
print("computer Score = ",computer_score)
print("User Score",user_score)

