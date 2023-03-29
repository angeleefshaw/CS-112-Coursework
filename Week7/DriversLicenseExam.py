# Grade students drivers license exam. Passing grades will be given to 
# those students who answer 15 out of 20 questions correctly. Print out
# all missed questions

from StudentsAnswers import getStudentAnswers

correctAns= ['a','c','a','a','d','b','c','a','c','b','a','d','c','a','d','c','b','b','d','a']
studentsAns = getStudentAnswers()
incorrectAns = []

for i in range(len(studentsAns)):
    if(correctAns[i] == studentsAns[i]):
        continue
    else:
        incorrectAns.append(i+1)


if(len(incorrectAns) > 5):
    print(f'You have failed the exam, You missed {len(incorrectAns)} questions and correctly answered {20 - len(incorrectAns)} questions. Look below to see wich questions you missed.\n')
    print(incorrectAns)
else:
    print(f'Congrats! You passed. You missed {len(incorrectAns)} questions and correctly answered {20 - len(incorrectAns)} questions. Look below to see which questions you missed.')
    print(incorrectAns)

