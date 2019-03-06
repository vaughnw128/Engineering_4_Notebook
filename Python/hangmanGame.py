#VAUGHN WOERPEL & CHARLIE WERMTER
#HANGMAN GAME

#Imports
import os

#Global Variables
gameEnd = False
score = 0
wordDisplay = []
progWord = 0

#Update display
def updateDisplay():
    displayList = ["   o", "   |", "   |", "  /|","  /|\\", "   |", "  /", "  / \\"]
    print("---|")
    for i in range(0, score):
        if(score==8 and (i==6 or i==3 or i==2)):
           i+=1
        elif(score>=5 and (i==2 or i==3)):
            i+=1
        elif(score==4 and (i==2)):
           i+=1
        else:
           print(displayList[i])
    for i in range(0, len(wordDisplay)):
        print(wordDisplay[i], end="")
           
#Entering the word
print("Player 1 Enter your word!")
word = str(input("Word: "))
wordDisplay =  [''] * len(word)
for i in range(0, len(word)):
    wordDisplay[i] = '_'
os.system('clear') #Clears the shell

while not gameEnd:
    #Updates the Display    
    updateDisplay()
    print("")
    
    #Check if the game is over
    if(score == 8):
        print("You Lose.")
        endif = input()
        gameEnd = True
    if(progWord == len(word)):
        print("You Win!")
        endif = input()
        gameEnd = True

    #Handles the player guess, subtracts score or adds progress
    if not gameEnd:
        guess = str(input("Player 2, Guess: "))
        if(guess not in word):
            score = score + 1
        else:
            for i in range(0, len(word)):
                if(word[i] == guess):
                    wordDisplay[i] = guess
                    progWord += 1
        


