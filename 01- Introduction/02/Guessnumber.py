import random

print("Welcome to Guess Game")
counterGuessing = 0


# Gameplay
def gameplay():
    global UserGuessing
    global counterGuessing
    UserGuessing = int(input("please Write your Guess number"))
    counterGuessing += 1
    if UserGuessing < GuessNumber:
        print("Your Guess is smaller than it")
    elif UserGuessing > GuessNumber:
        print("Your Guess is bigger than it")
    elif UserGuessing == GuessNumber:
        print("Win")
    else:
        print("your input is wrong")


# init Game
UserGuessing = 0

# Make Random number for Game
GuessNumber = random.randrange(1, 50)
print("the Random number is between 1-50")

# While not Guess correctly , play game
while GuessNumber != UserGuessing:
    gameplay()

print("Number of Your try to Guess = ", counterGuessing)
