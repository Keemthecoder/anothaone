# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

for a in range(0,5):
    print list1

y = int(raw_input("How many numbers you want boi?"))
for list1 in range(0,y):
    print list1

#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

for item in b:
    for item_c in c:
        if item == item_c:
            print item

#Part III
# Take a list, say for example this one:
d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.

for item_d in d:
    if item_d == "a":
        print "*"
    elif item_d != "a":
        print item_d

#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.



num = str(raw_input("What word would you like to palindrome test?"))
for item in num:
    if num[0] != num[-1]:
        print "It is not a palindrome."
        break
    elif num[0] == num[-1]:
        print "It is a palindrome."
        break


