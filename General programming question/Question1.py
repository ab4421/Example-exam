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

# Lists

# Write a function to find the list of words that are longer than n from a given list of words.
# for example: 
# from an input list of ["cat", "dog", "hello", "list", "hi"] and n = 3
# returns ["hello", "list"]
# weight = 2

def longerThanN(myList, n):
    outputList = []
    for word in myList: 
        if len(word)>n: 
            outputList.append(word)
    return outputList

List1 = ["cat", "dog", "hello", "list", "hi"]
print(longerThanN(List1, 3))