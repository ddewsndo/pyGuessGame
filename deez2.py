#git add .
#git commit -m "(Your message/what you added or did)"
#git push
#To save and push code^
#clear screen only works for windows 

#add easy mode that will give hints based on user input!!!
#add menu and make it pretty
#make the numbers genuinely random
import random
import os
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
        self.lives-= 1
        self.hint(userNum)
        print(f"You have {self.lives} left.")
    def correct (self):
        os.system('cls')
        #Should get rid of global level and level +=1 here, return it as true and use outside function to update level
        global level
        print ("GOOD JOB!!!!")
        level += 1
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

        

levelOne = guessGame(listOne, random.randint(1, 5), 3)
levelTwo = guessGame(listTwo, random.randint(1, 10), 3)
levelThree = guessGame(listThree, random.randint(1, 15), 3)
levelFour = guessGame(listTwo, random.randint(1 , 10), 1)

while level == 0 and levelOne.lives > 0:
    print("Level 1: Numbers range from 1 to 5, inclusive.")
    levelOne.guess()
while level == 1 and levelTwo.lives > 0:
    print("Level 3: Numbers range from 1 to 10, inclusive.")
    levelTwo.guess()
while level == 2 and levelThree.lives > 0:
    print("Level 3: Numbers range from 1 to 15, inclusive. Good luck!")
    levelThree.guess()
while level == 3 and levelFour.lives > 0:
    print("Last Level! Back to range being 1 through 10, however only one life now instead of three. Choose carefully...")
    levelFour.guess()
if levelOne.lives == 0 or levelTwo.lives == 0 or levelThree.lives == 0 or levelFour.lives == 0:
    print("YOU LOSTTTTT")
