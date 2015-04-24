"""guess the number"""
# Aqui escribe tu codigo

import random #Import random library

PLAY = "Y" #Declare variable PLAY

while PLAY == "Y" and PLAY.isalpha(): #While PLAY be equal to "Y" and it be text
    NUMBER_RANDOM = random.randrange(1, 21) #Generates a random number between 1 and 20
    TURN_NUMBER = 1 #Declares a variable to assign the number of turns

    while TURN_NUMBER < 5: #If it still have not reached to the turn 4 makes the following code
        print "YOU ARE IN TURN:", TURN_NUMBER #Shows the turn in which we are
        try: #It start a try to prove the errors
            #One number is entered between 1 and 20 and becomes integer
            NUMBER_ENTERED = int(raw_input("GUESS THE NUMBER BETWEEN 1 AND 20: "))
            #If the number is between 1 and 20 makes the following code
            if NUMBER_ENTERED < 21 and NUMBER_ENTERED > 0:
                #If the entered number is equal to the number generated makes the following code
                if NUMBER_ENTERED == NUMBER_RANDOM:
                    print "you win!" #Prints on consola "you win!" if the code above is true
                    break #Breaks the condition if
                #If the number entered is different and the turn is less than 5 makes the next code
                elif NUMBER_ENTERED != NUMBER_RANDOM and TURN_NUMBER < 5:
                    #If number entered is greater than number generated
                    if NUMBER_ENTERED > NUMBER_RANDOM:
                        #Prints this on consola if the code above is true
                        print "you guessed to high, please try again"
                    #Otherwise if number entered is smaller than the number generated
                    elif NUMBER_ENTERED < NUMBER_RANDOM:
                        #Prints this on consola if the code above is true
                        print "you guessed to low, please try again"
                if TURN_NUMBER == 4: #If the turn comes to 4 maskes the following code
                    #If the code above is true print this on consola
                    print "this was the number generated:", NUMBER_RANDOM
                    print "Game Over" #And print this on consola too
                    break #Breaks the condition
                TURN_NUMBER += 1 #It goes up a turn
            #If number entered is smaller than 0 and is greater than 20 makes the next code
            elif NUMBER_ENTERED < 0 or NUMBER_ENTERED > 20:
                #If the code above is true print this on consola asking a number between 1 amd 20
                print "PLEASE WRITE A NUMBER BETWEEN 1 AND 20"
        except ValueError: #Starts the exception and the type of exception
            print "PLEASE ENTER ONLY NUMBERS" #Prints this and ask that it enter numbers

    PLAY = raw_input("DO YOU WANT TO PLAY AGAIN? WRITE Y OR N: ") #Asks if you want to play again
    PLAY = PLAY.upper() #Becomes uppercase the input
    if PLAY == "Y": #If the input is equals to "Y"
        PLAY = PLAY.upper() #Becomes the input in uppercase
    elif PLAY == "N": #Otherwise if the input is equals to "N"
        print "GAME HAS ENDED" #Prints on consola this
        break #Breaks the condition
    #Starts a cycle "while" the input is a number or if is different to "Y" or "N"
    while PLAY.isdigit() or PLAY != "Y" and PLAY != "N":
        #Again asks that the user enter "Y" or "N"
        PLAY = raw_input("PLEASE WRITE IN TEXT \"Y\" or \"N\": ")
        PLAY = PLAY.upper() #Becomes the input in uppercase
        if PLAY == "Y" and PLAY.isalpha(): #Starts a condition if is equals to "Y" and if is text
            PLAY = PLAY.upper() #Becomes the input in uppercase
            break #Breaks the condition
        elif PLAY == "N" and PLAY.isalpha(): #Otherwise if the input is equals to "N" and if is text
            print "GAME HAS ENDED" #Prints on consola this
            break #Breaks the condition
