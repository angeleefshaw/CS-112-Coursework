# A program that asks the user to enter a 10-character telephone number in the format
# XXX-EGG-TREE, Translate user input to its numeric equivalent 

def main():

    phoneNumInput = input('Enter an alphabetic phone number in the form of XXXXXX-XXXX \n').upper()
    phoneNumber = ''

    for char in range(len(phoneNumInput)):
        if(phoneNumInput[char] == 'A' or  phoneNumInput[char] == 'B' or phoneNumInput[char] == 'C'):
            phoneNumber += '2'
        elif(phoneNumInput[char] == 'D' or phoneNumInput[char] == 'E' or phoneNumInput[char] == 'F'):
            phoneNumber  += '3'
        elif(phoneNumInput[char] == 'G' or phoneNumInput[char] == 'H' or phoneNumInput[char] == 'I'):
            phoneNumber += '4'
        elif(phoneNumInput[char] == 'J' or phoneNumInput[char] == 'K' or phoneNumInput[char] == 'L'):
            phoneNumber += '5'
        elif(phoneNumInput[char] == 'M' or phoneNumInput[char] == 'N' or phoneNumInput[char] == 'O'):
            phoneNumber  += '6'
        elif(phoneNumInput[char] == 'P' or phoneNumInput[char] == 'Q' or phoneNumInput[char] == 'R' or phoneNumInput[char] == 'S'):
            phoneNumber += '7'
        elif(phoneNumInput[char] == 'T' or phoneNumInput[char] == 'U' or phoneNumInput[char] == 'V'):
            phoneNumber += '8'
        elif(phoneNumInput[char] == 'W' or phoneNumInput[char] == 'X' or phoneNumInput[char] == 'Y' or phoneNumInput[char] =='Z'):
            phoneNumber += '9'
        else:
            phoneNumber += phoneNumInput[char]

    return phoneNumber

print(main())

