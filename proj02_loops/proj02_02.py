# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

previous = 0
current = 1
next = int(previous + current)
times = int(raw_input("How many Fibonacci numbers do you want?"))
for number in range(0, times):
    print current
    next = int(previous + current)
    previous = current
    current = next

previous2 = 2
times2 = int(raw_input("How many powers of 2 do you want?"))
for number in range(0, times2):
    print previous2
    previous2 = previous2 * 2
