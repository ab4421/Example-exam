'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).




'''

# Write a function to find a list of numbers that are larger than n, from a given list of numbers.
# for example:
# from an input list [1, 2, 3, 4, 5, 6] and n = 2
# returns [3, 4, 5, 6]
# weight = 2

def largerThanN(myList, n):
    outputList = []
    for num in myList:
        if num > n:
            outputList.append(num)
    return outputList

list1 = [1, 2, 3, 4, 5, 6]
print(largerThanN(list1, 2))
