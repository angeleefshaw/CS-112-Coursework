class Atom:
    """An element from the periodic table."""

    def neutrons(self):
        """Returns the number of neutons the element has"""
        number = self.isotope - self.atomic
        print(self.symbol + " has " + str(number))
        return(number)

    def grams_to_moles(self, grams):
        print(self)
        """Converts the mass of an element in a gram"""
        moles = grams / self.mass
        print(str(grams) +"g  is "+ str(moles) +" of " + self.symbol)
        return(moles)

def main():
    oxygen = Atom()
    oxygen.symbol = 'O'
    oxygen.atomic = 8
    oxygen.mass = 15.999
    oxygen.isotope = 16
    # print(type(oxygen))
    # print(oxygen.symbol)
    # print(oxygen)

    carbon = Atom()
    carbon.symbol = 'C'
    carbon.mass = 12.001
    oxygen.neutrons()
    oxygen.grams_to_moles(24)

    hydrogen = Atom()
    hydrogen.symbol = 'H'

    print(type(oxygen))

    carbon.neutrons()

main()
