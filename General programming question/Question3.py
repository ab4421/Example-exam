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

# Write a function that concatenates two sentences passed as inputs. The returned
# string is the first word from the first sentence, then the first word from the
# second sentence, alternating back forth. If the sentences are not the same number
# of words, the function will return None and print "The strings are of different lengths".
#    for example:
#       the input sentences 'the cow jumped over the moon' and 
#                            'jack and jill went up the'
#       returns 'the jack cow and jumped jill over went the up moon the'
# weight = 3

def merge_sentences(sentence1, sentence2):
    outputList = []
    sent1List = sentence1.split(" ")
    sent2List = sentence2.split(" ")
    if len(sent1List) != len(sent2List): 
        print("The strings are of different lengths")
        return None
    else: 
        for i in range(len(sent1List)): 
            outputList.append(sent1List[i])
            outputList.append(sent2List[i])
        return " ".join(outputList)

sent1 = 'the cow jumped over the moon'
sent2 = 'jack and jill went up the'

print(merge_sentences(sent1, sent2))
