import random

# Will generate random num between/including 3-10
# randomNum = random.randint(3, 10)

# Functions 
# two classes of functions - void and return
# write a function by using the def keyword

# base is defined in the function header (parameter)
# def power(base):
#     print('The base is:', base)

# main function is known as the driver
# def main(): 
#     print('This is a void function')

# def model_one():
#     print("This function will replace all the periods with !") 
#     sentence= input("enter a short sentence, with a period at the end: ")
#     result = sentence.replace('.','!') # replaces all periods with !
#     result

# model_one()   


def model_two(sentence):
    print(sentence)
    print("This function will replace all the periods in the sentence with ! "); 
    result = sentence.replace('.','!')
    print(result)

model_two('hi'+ 'there.')
