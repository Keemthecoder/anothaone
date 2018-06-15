# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
word = choose_word(wordlist)
list1 = []
for letter in word:
    list1.append(letter)
list2 = []
for letter in word:
    list2.append(str("_ "))
#print list1
print "Welcome to Cole and Connor's Hangman Game!"
guess = int(raw_input("How many guesses do you want?"))
spot = 0
s = ""
alphabet = string.lowercase
for item in list2:
    s = s + item
print "The word has this many letters in it:" + s
print "-----------------------------------------------------------------"
while guess > 0:
    y = raw_input("Guess a letter in the word.")
    alphabet = alphabet.replace(y, "_")
    spot = 0
    if y in list1:
        guess = guess - 1
        print "Correct! You have " + str(guess) + " guesses left. You have completed this much of the word:"
        for letter in list1:
            if letter == y:
                list2[spot] = y
                s = ""
                for item in list2:
                    s = s + item
            spot = spot + 1
        print s
        print "You have this many letters of the alphabet left: " + alphabet
        print "-----------------------------------------------------------------"
    elif y not in list1:
        guess = guess - 1
        print "Incorrect! You have " + str(guess) + " guesses left. You have completed this much of the word:"
        print s
        print "You have this many letters of the alphabet left: " + alphabet
        print "-----------------------------------------------------------------"
    if "_ " not in list2:
        print "Congratulations, you won the game! Don't forget to play again."
        break
if "_ " in list2:
    print "You couldn't guess the word. Try again!"