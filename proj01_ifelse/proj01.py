# Name: Cole Patterson
# Date:

# proj01: A Simple Program



# Part I:
# This program asks the user for his/her name and grade.
# Then, it prints out a sentence that says the number of years until they graduate.

current_day = int(12)
current_month = int(6)
print "While using this program don't put a space between the question and your answer!"
name = raw_input("What is your name?")
grade =  int(raw_input("What grade are you in?"))
print (name[0].upper() + name[1:].lower()) + " will graduate from high-school in " + str(12 - grade) + " years."

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

day = int(raw_input("What day of the month were you born on?"))
month = int(raw_input("What month were you born in?"))
if month == current_month and day < current_day:
    print "Your birthday is in about 11 months "
elif month < current_month:
    print "Your birthday is in about " + str(month - current_month + 12) + " months and "
else:
    print "Your birthday is in about " + str(month - current_month) + " months and "
if day < current_day:
    print str(day - current_day + 30) + " days."
else:
    print str(day - current_day) + " days."
age = int(raw_input("How old are you?"))
if age < 13:
    print "You can see PG movies."
if age < 17 and age >= 13:
    print "You can see PG and PG-13 movies."
if age >= 17:
    print "You can see PG, PG-13, and R movies."

#If you complete extensions, describe your extensions here!

