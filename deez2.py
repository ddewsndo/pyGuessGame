#git add .
#git commit -m "(Your message/what you added or did)"
#git push
#To save and push code^
#clear screen only works for windows 


#add menu and make it pretty
#add failsafes for input


import random
import os

os.system('cls')

print("This is a random number guesser, you have ranges to guess from and three lives per level. Guess it correct and move on!")

level = 0
listOne = [1, 2, 3, 4, 5]
listTwo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listThree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

class guessGame:
    def __init__(self, numList, correctNum, lives):
        self.numList = numList
        self.correctNum = correctNum
        self.lives = lives
    def incorrect(self, userNum):
        os.system('cls')
        self.levelStatement()
        self.lives-= 1
        self.hint(userNum)
        print(f"You have {self.lives} lives left.\n")
    def correct (self):
        os.system('cls')
        #Should get rid of global level and level +=1 here, return it as true and use outside function to update level
        global level
        print ("\nGOOD JOB!!!!")
        level += 1
        self.levelStatement()
    def guess(self):
        userGuess = int(input("Enter Guess!   "))
        if userGuess == self.correctNum:
            self.correct()
        else:
            self.incorrect(userGuess)
    def hint(self, userNum):
        if userNum < self.correctNum:
            print("Too low...")
        if userNum > self.correctNum:
            print("Too high...")
    def levelStatement(self):
        if level == 0:
            print("\nLevel 1: Numbers range from 1 to 5, inclusive.\n")
        elif level == 1:
            print("\nLevel 2: Numbers range from 1 to 10, inclusive.\n")
        elif level == 2:
            print("\nLevel 3: Numbers range from 1 to 15, inclusive. Good luck!\n") 
        elif level == 3:
            print("\nLast Level! Numbers range from 1 through 10 again, however only one life now instead of three. Choose carefully...\n")

levelOne = guessGame(listOne, random.randint(1, 5), 3)
levelTwo = guessGame(listTwo, random.randint(1, 10), 3)
levelThree = guessGame(listThree, random.randint(1, 15), 3)
levelFour = guessGame(listTwo, random.randint(1 , 10), 1)

levelOne.levelStatement()

while level == 0 and levelOne.lives > 0:
    levelOne.guess()
while level == 1 and levelTwo.lives > 0:
    levelTwo.guess()
while level == 2 and levelThree.lives > 0:
    levelThree.guess()
while level == 3 and levelFour.lives > 0:
    levelFour.guess()
if levelOne.lives == 0 or levelTwo.lives == 0 or levelThree.lives == 0 or levelFour.lives == 0:
    os.system('cls')
    print("\n\nYOU LOSTTTTT\n\n")
if level == 4:
    print("\n\nY O U  F R E A K I N G  W O N ! ! ! ! ! !\n\n")