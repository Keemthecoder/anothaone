# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random
var = random.randint(1,10)
guess = 0
guessnumber = int(raw_input("How many guesses do you want?"))
for x in range(0, guessnumber):
    guess = int(raw_input("Guess a number between 1 and 10, including 1 and 10."))
    if guess == var:
        print "Congrats, you guessed the number!"
        break
    elif guess < var:
        print "Too low!"
    elif guess > var:
        print "Too high!"
    guessnumber = guessnumber - 1
    print "You have " + str(guessnumber) + " tries left."
    if guessnumber == 0:
        print "You weren't able to guess the number! Try again!"





