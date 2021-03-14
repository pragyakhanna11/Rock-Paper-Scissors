#rock paper scissors

import random
while True:
    mood = input("Do you wish to play a game of rock paper scissors? Y/N ")
    if mood=='y' or mood=='Y':
        
        n = int(input("Number of rounds you want to play: "))
        print("1. Rock\n2. Paper\n3. Scissors\n")
        r = 0 #round number
        us = 0 #user score
        cs = 0 #computer score
        tie = 0 #number of ties

        while(r<n):
            print("Round no.: ", r+1)
            ui = int(input("Please choose a number: "))
            ci = random.randint(1,3)
            print("Computer chose: ", ci)
            if ui == ci:
                tie+=1
            elif ui==1 and ci==2:
                cs+=1
            elif ui==1 and ci==3:
                us+=1
            elif ui==2 and ci==1:
                us+=1
            elif ui==2 and ci==3:
                cs+=1
            elif ui==3 and ci==1:
                cs+=1
            elif ui==3 and ci==2:
                us+=1
            else:
                print("You are stupid!!")
            r+=1
            print("Your score: ", us)
            print("Computer's score: ", cs, "\n")

        if us>cs:
            print("You won!!")

        elif us<cs:
            print("You lose ://")

        else:
            print("It's a tie.")
    else:
        break
