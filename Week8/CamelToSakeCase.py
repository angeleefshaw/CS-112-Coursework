# Program that takes in a camelCase var and returns the var in snake_case
import re

def main(): 
    camelInput = input('Enter a variable name in camelCase \n')
    return '_'.join(re.findall('[a-zA-Z][^A-Z]*', camelInput)).lower()
        
print(main())