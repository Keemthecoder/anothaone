# Name:
# Date:

# proj01: A Simple Program

current_day = int(11)
current_month = int(6)

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

name = raw_input("What is your name?")
grade =  int(raw_input("What grade are you in?"))
print (name[1].upper() + name[2:].lower()) + " will graduate from high-school in " + str(12 - grade) + " years."

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

day = int(raw_input("What day of the month were you born on?"))
month = int(raw_input("What month were you born in?"))

if month == current_month:
    print "Your birthday is in about 11 months "
if month < current_month:
    print "Your birthday is in about " + str(month - current_month + 12) + " months "
else:
    print "Your birthday is in about " + str(month - current_month) + " months "
if day < current_day:
    print "and " + str(day - current_day + 30) + " days."
else:
    print "and " + str(day - current_day) + " days."


# If you complete extensions, describe your extensions here!

