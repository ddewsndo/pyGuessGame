#git add .
#git commit -m "(Your message/what you added or did)"
#git push
#To save and push code^

level = 0
listOne = [1, 2, 3, 4, 5]
listTwo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class guessGame:
    def __init__(self, numList, correctNum, lives):
        self.numList = numList
        self.correctNum = correctNum
        self.lives = lives
    def incorrect(self):
        self.lives-= 1
        print(f"wrong! you have {self.lives} left.")
    def correct (self):
        global level
        print ("GOOD JOB!!!!")
        level += 1
    def printTS(self):
        print("tspmo")
    def guess(self):
        userGuess = int(input("Enter Guess!"))
        if userGuess == self.correctNum:
            self.correct()
        else:
            self.incorrect()

levelOne = guessGame(listOne, 1 , 3)
levelTwo = guessGame(listTwo, 7, 3)

while level == 0 and levelOne.lives > 0:
    levelOne.guess()
if levelOne.lives == 0:
    print("YOU LOSTTTTT")
if level == 1:
    print("sry ur done son")