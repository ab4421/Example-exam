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

# Write a function that takes a string as parameter, which will contain single digit numbers, 
# letters, and question marks, and check if there are exactly 3 question marks 
# between every pair of two numbers, whose sum is 10. 
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers then your program should return false 
# as well.
# Example1: input = "sdfhdsl4??sfasdfga?1sdjkfhbdsjhfkb" output = False (the two numbers do not sum to 10)
# Example2: input = "sdfhdsl4??sfasdfga?6sdjkfhbdsjhfkb" output = True (the two numbers sum to 10)
# weight = 8

#generalise

def question_mark(string1):
    numTotal = 0
    questionMarkCount = 0
    digitCount = 0
    for letter in string1:
        if letter.isdigit(): 
            digitCount += 1
            numTotal += int(letter)
        elif letter == "?" and digitCount%2 != 0: 
            questionMarkCount += 1
    if numTotal == 10 and questionMarkCount == 3: 
        return "True"
    else: 
        return "False"

def question_mark2(string2):
    digits = [digit for digit in string2 if digit.isdigit()]
    trueCount = 0 
    for place, num in enumerate(digits):
        try: 
            if int(num)+int(digits[place+1]) == 10:
                if string2[string2.index(num):string2.index(digits[place+1])].count("?") == 3:
                    trueCount += 1
                    
        except IndexError:
            if int(num)+int(digits[place-1]) == 10:
                if string2[string2.index(digits[place-1]):string2.index(num)].count("?") == 3:
                    trueCount += 1        
            else: 
                return False
        else: 
            if trueCount == (len(digits)-1):
                print(trueCount)
                return True
        
                
        


input1 = "sdfhdsl4??sfasdfga?1sdjkfhbdsjhfkb"
input2 = "sdfhdsl4??sfasdfga?6sdjkfhbdsjhfkb"
input3 = "8???2???8"
print(question_mark(input1))
print(question_mark(input2))
print(input1[8:19].count("?"))
digits = [int(letter) for letter in input1 if letter.isdigit()]
print(digits)
print(input1.index("1"))
print(question_mark2(input1))
print(question_mark2(input2))
print(question_mark2(input3))

