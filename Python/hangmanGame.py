#VAUGHN WOERPEL & CHARLIE WERMTER
#HANGMAN GAME

#Imports
import os

#Global Variables
gameEnd = False
score = 8
displayList = ["   o", "   |", "   |", "  /|","  /|\\", "   |", "  /", "  / \\"]


#Update display
def updateDisplay():
    print("---|")
    for i in range(0, score):
        #TODO: ADD A CHECK FOR DUPLICATE STRINGS!
        print(displayList[i])
        
        



#Entering the word
print("Player 1 Enter your word!")
word = str(input("Word: "))
os.system('clear') #Clears the shell

while not gameEnd:
    updateDisplay()
    guess = str(input("Player 2, Guess: "))
    score = score - 1
    


