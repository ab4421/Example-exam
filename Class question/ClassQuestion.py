'''
ClassQuestion.py


TOTAL POINTS AVAILABLE: 50


12 points per method, 42 across whole class, 8 points for the creation of the students and the task.

--------------------------------------
Marking for methods:
--------------------------------------

12 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

9-11 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

7-8 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

3-6 points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1-2 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

--------------------------------------
Marking for the creation of students:
--------------------------------------

8 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

6-7 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

4-5 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

2-3points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

'''



# Create a class called Student with one instance attribute called "courses"
# that is created in the constructor.
#   
#   - "courses" will be a dictionary and will start empty in the constructor 
#        but when populated later by other methods: 
#         - the keys will be string describing the name of the course (e.g. 'computing') 
#         - and the values will be a dictionary of two items
#                   1. the first item is 'year' in which the course takes place (an integer from 1 to 4)
#                   2. the second item is 'grade' (expressed with a float from 1 to 100)
#                   (e.g. {'computing': {'year': 1, 'grade': 87.5})

from numpy.lib.function_base import average
import random


class Student: 
    def __init__(self, courses: dict()):
        self.courses = courses


# Create a method called add_course(). It should:
#   - have 3 parameters: 'course_name', 'year' and grade
#   - 'grade' has a default value of "None"
#   - it should change the grade of the corresponding course in the "courses" attribute
#        - if the course exists already ask the user (via terminal) if they want to change the existing course.
#           if the user says "yes" or "y", change the grade and the year accordingly. If the grade was not specified, ask the user (via terminal) for the grade
#           if the user writes "no" or "n", ignore it. 
#           keep asking the question until the user inputs either yes/y or no/n
#        - if the course does not already exist in the dictionary, add a new entry

    def add_course(self, course_name, year, grade = "None"):
        if course_name in self.courses.keys(): 
            answer = " "
            while answer != "yes" or answer != "y" or answer != "no" or answer != 'n':
                answer = input("Do you want to change the existing course?: ")
            if answer == "yes" or answer == "y": 
                if grade == "None": 
                    specGrade = input("Please specify the grade: ")
                    self.courses[course_name] = {"year": year, "grade": specGrade}
                else: 
                    self.courses[course_name] = {"year": year, "grade": grade}
        else: 
            self.courses[course_name] = {"year": year, "grade": grade}
            



# Create a method called change_grade(). It should:
#   - have 2 parameters: 'course', grade
#   - it should change the grade of the course
#        - if the course exists already, change the grade accordingly
#        - if the course doesn't exist, notify the user that the course doesn't exist and ask them if they want to create one (via terminal).
#          if the user says "yes" or "y", ask for the year of the course and then add the new course accordingly,
#          if the user writes "no" or "n", ignore it. 
#           keep asking the question until the user inputs either yes/y or no/n

    def change_grade(self, course, grade):
        if course in self.courses.keys(): 
            self.courses[course]['grade'] = grade
        else: 
            answer = " "
            while answer != "yes" or answer != "y" or answer != "no" or answer != 'n':
                answer = input("This course does not exist. Do you want to create it: ")
            if answer == "yes" or answer == "y": 
                year = input("Please enter the year of the course: ")
                self.courses[course] = {'year': year, 'grade': grade}
            


# Create a method called calculate_mean(). It should: 
#   - have one parameter, either a list of strings or a year (from 1 to 4):
#   - if the parameter is the year, the method returns the average of all the courses for that specific year. If there are no courses for that year, the method
#     will return "None" and print "No courses added for year {year}"
#   - if the parameter is a list of strings, the method returns the average for all courses in that string. 
#        if any of the courses in the string are not present in the attribute "courses", the method will ignore them and just return
#        the mean for the ones that are present. If none of the courses are present the method will return "None" and print "The student "

    def calculate_mean(self, parameter): 
        if parameter.isdigit(): 
            gradeOfYear = [self.courses[course]['grade'] for course in self.courses.keys() if self.courses[course]['year'] == parameter]
            if len(gradeOfYear) > 0: 
                return (average(gradeOfYear))
            else: 
                print(f"No courses added for year {parameter}")
                return "None"
        else: 
            gradeOfYear = [self.courses[course]['grade'] for course in self.courses.keys() if course in parameter]
            if len(gradeOfYear) > 0: 
                return (average(gradeOfYear))
            else: 
                print("The student ")
                return "None"
            

# Create 10 instances of the class Student and to each one of them assign a course "computing I" and a
# course "Mathematics". 
#   - Both of them have year 1 as the year and a random grade between 1 and 100.
#   - Write a function called "calculate_overall_mean()" that takes as input any list of students and an optional argument "course" (default None).
#       
#       -If course is not specified the function will return a dictionary with, as keys, all the courses that the students have
#        (mathematics and computing in this example, but there could be more) and as value the mean across the list students.
#       - If course is specified, the function will return the mean for that specific course across the list of students.

    



listOfStudents = []
for i in range(10):
   listOfStudents.append(Student({"computing I":{"year": 1, "grade": random.uniform(1.0,100.0)}, "Mathematics":{"year": 1, "grade": random.uniform(1.0, 100.0)}}))

for student in listOfStudents:
    print(student.courses)

def calculate_overall_mean(students, course = None):
    outputDict = {}
    for student in students: 
        for courses in student.courses.keys():
            if courses not in outputDict.keys(): 
                outputDict[courses] = []
            outputDict[courses].append((student.courses[courses]["grade"]))
    for courses in outputDict.keys():
        outputDict[courses] = average(outputDict[courses])
    if course == None:       
        return outputDict
    else: 
        return outputDict[course]

print(calculate_overall_mean(listOfStudents))
print(calculate_overall_mean(listOfStudents, 'computing I'))

    
