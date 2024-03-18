#HangMan - Life Mode

import random

#init
UserTry=0
WordListFruits=["Apple","Orange"]
UserGuess=""

#select random From len list
SelectedWord = random.randint(0,len(WordListFruits)-1)

#GamePlay
while UserTry<6:
    print("life : ", "❤️"*(6-UserTry),"🖤"*UserTry)
    UserGuess=input("Whats Your Guess ?")
    UserTry +=1
    if UserGuess.upper()==WordListFruits[SelectedWord].upper():
        print("Win")
        break
    else:
        print("Try Again")



