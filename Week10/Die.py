from random import randint

class Die:
    #Constructor to initialize the instance variables
    def __init__(self, numSides):
        if numSides >= 4:
            # Make variables private with __
            self.__numSides = numSides
        else:
            self.__numSides = 6

        self.__faceValue = 1

    # Always pass self in as a parameter. Manipulate class properties as needed.
    def roll(self):
        self.__faceValue = randint(1, self.__numSides)

    #Getter method or Accessor methods - returns value of private property
    def getFaceValue(self):
        return self.__faceValue

angDie = Die(10)
print(angDie.getFaceValue())

angDie.roll()

print(angDie.getFaceValue())