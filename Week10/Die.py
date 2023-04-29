from random import randint

class Die:
    #Constructor to initialize the instance variables (set values for instance variables)
    def __init__(self, numSides):
        if numSides >= 4:
            # Make variables private with __
            self.__numSides = numSides
        else:
            self.__numSides = 6

        self.__faceValue = 1

    # Always pass self in as a parameter. Manipulate class properties as needed.
    # Self is where the class is in memory - (if you were to print an instance of the die)
    # A getter method is also called an accessor
    def roll(self):
        self.__faceValue = randint(1, self.__numSides)

    # Getter method or Accessor methods - returns value of private property
    def getFaceValue(self):
        return self.__faceValue
    
    # Setters set values
    def setNumSides(self, numSides): 
        if numSides >= 4:
            self.__numSides = numSides
        else:
            self.__numSides = 6

    # String method
    def __str__(self):
        rtnStr = "Facevalue: " + str(self.__faceValue)
        return rtnStr

angDie = Die(10)
print(angDie)

# angDie.roll()

# print(angDie.getFaceValue())