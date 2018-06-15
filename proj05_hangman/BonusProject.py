# Create a program that will play the 'cows and bulls' game with the user. The game works
# like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a 'cow'. For
# every digit the user guessed correctly in the wrong place is a 'bull.' Every time the
# user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the
# user makes throughout the game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like
# this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

# Until the user guesses the number.


import random
number = str(random.randint(1000,9999))
print number
print "Welcome to Cows and Bulls. Bulls means that a number is correct, but not in the right place."
print "Cows means that a number is correct and in the right place."
guess = str(raw_input("Guess a 4-digit number. "))
listnumber = []
for digit in number:
    listnumber.append(digit)
listguess = []
for digit in guess:
    listguess.append(digit)
spot = 0
cows = 0
bulls = 0
for digit in range(0, 4):
    if listguess[spot] == listnumber[spot]:
        listguess[spot] = "%"
        listnumber[spot] = "*"
        spot = spot + 1
        cows = cows + 1
    elif listguess[spot] != listnumber[spot]:
        spot = spot + 1
if listguess[spot] == "*":
    spot = 0
    for item1 in listguess:
        for item2 in listnumber:
            bulls = bulls + 1
            listnumber[spot] = "*"
            break
        spot = spot + 1
    print "You have " + str(cows) + " cows and " + str(bulls) + " bulls."
