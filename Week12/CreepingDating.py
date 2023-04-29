from random import randint

class DateClient:
    #Constructor to initialize the instance variables (set values for instance variables)
    def __init__(self, name, phoneNumber, age):
        self.__name  = name
        self.__phoneNumber = phoneNumber
        self.__age = age

    # Getters
    def getLowerBound(self):
        youngestDatableAge = (int(self.__age)/2) + 7
        return int(youngestDatableAge)
    
    def getUpperBound(self):
        youngestDatableAge = (int(self.__age)/2) + 7
        oldestDatableAge = ((int(self.__age) - youngestDatableAge)*2) + int(self.__age)
        return int(oldestDatableAge)

    # String method
    def __str__(self):
        rtnStr = f"The youngest datable age is {self.getLowerBound()}. The oldest datable age is {self.getUpperBound()}"
        return rtnStr
        
client1 = DateClient('David', '7043339283', 29)
print(client1)

client2 = DateClient('Mary', '7043928111', 37)
print(client2)