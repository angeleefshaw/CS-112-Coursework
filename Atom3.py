class Atom:
    """An element from the periodic table."""
    
    def __init__(self,symbol,atomic, mass, isotope=12):
        self.symbol = symbol
        self.atomic = atomic
        self. mass = mass
        self.isotope = isotope

    def __str__(self):
        return(self.symbol + "  "+ str(self.isotope) + ", mass: "+ str(self.mass))
        
    def neutrons(self):
        """Returns the number of neutons the element has"""
        number = self.isotope - self.atomic
        #print(self.symbol + " has " + str(number))
        return(number)

    def grams_to_moles(self, grams):
        """Converts the mass of an element in a gram"""
        moles = grams / self.mass
        #print(grams +"g  is "+ str(moles) +" of " + self.symbol)
        return(moles)


def main():
    oxygen = Atom("O",8,15.999,16)
    print(oxygen)
    print("Thre are " + str(oxygen.grams_to_moles(24)) + " moles in 24 grams")

main()    
    
