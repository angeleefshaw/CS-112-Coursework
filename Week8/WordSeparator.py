# Program that takes in a string of works without spaces, and separates the words
# into a coherent sentence. 

import re

# INPUT = a sentence of words, no spaces, all capitalized
# OUTPUT = a string containing the words lowercased except for the first
def main ():
    sentence = input('Type a sentence of words with no spaces where each word is capitalized \n')

    parsedInput = re.findall('[a-zA-Z][^A-Z]*', sentence)

    for i in range(len(parsedInput)):
        if(i != 0):
            parsedInput[i] = parsedInput[i].lower()

    return ' '.join(parsedInput)

print(main())
