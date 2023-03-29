def main():
    createCode(getAlphabet(), 5)


def getAlphabet():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return [x.upper() for x in alphabet]

def createCode(alpha, offset):
    slice = alpha[0:offset]
    remainder = alpha[offset: 25]
    remainder.extend(slice)

main()