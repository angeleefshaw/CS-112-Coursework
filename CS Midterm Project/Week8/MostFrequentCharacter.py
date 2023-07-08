# Write a program that lets the user enter a string and displays the character that appears 
# most frequently in the string

def main():
    string = input('Enter a random string of characters \n')

    mostFreqChar = ''
    charCount = 0

    for char in string:
        if(string.count(char) > charCount):
            mostFreqChar = char
            charCount = string.count(char)

    return mostFreqChar

print(main())