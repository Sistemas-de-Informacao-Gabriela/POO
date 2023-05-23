from enum import Enum

class Builder(Enum):
    FENDER = "fender"

class TypeG(Enum):
    ELECTRIC = "electric"
    ACOUSTIC = "acoustic"

class Wood(Enum):
    MAPLE = "maple"
    MOGNO = "mogno"
    ALDER = "alder"
    ASH = "ash"
    ROSEWOOD = "rosewood"
    EBANO = "ebano"

class Guitar():
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec
    
    def getSerialNumber(self):
        return self.serialNumber
    
    def getPrice(self):
        return self.price
    
    def setPrice(self, newPrice):
        self.price = newPrice
    
    def getSpec(self):
        return self.spec
    
class GuitarSpec():
    def __init__(self, builder, model, typeG, backWood, topWood, numStrings):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood
        self.numStrings = numStrings
    
    def getBuilder(self):
        return self.builder
    
    def getModel(self):
        return self.model
    
    def getTypeG(self):
        return self.typeG
    
    def getBackWood(self):
        return self.backWood
    
    def getTopWood(self):
        return self.topWood
    
    def getNumStrings(self):
        return self.numStrings

    def __str__(self):
        return f"{self.builder.value} {self.model} {self.typeG.value} guitar:\n   {self.backWood.value} back and sides,\n   {self.topWood.value} top."

    def matches(self, otherSpec):
        if self.builder != otherSpec.getBuilder():
            return False
        if self.model != otherSpec.getModel():
            return False
        if self.typeG != otherSpec.getTypeG():
            return False
        if self.backWood != otherSpec.getBackWood():
            return False
        if self.topWood != otherSpec.getTopWood():
            return False
        if self.numStrings != otherSpec.getNumStrings():
            return False
        return True

class Inventory:
    def __init__(self):
        self.guitars = []
    
    def addGuitar(self, serialNumber, price, spec):
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)
    
    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def search(self, searchGuitar):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.getSpec().matches(searchGuitar):
                matchingGuitars.append(guitar)
        return matchingGuitars
    
def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addGuitar("V95693", 1499.95, spec1)
    inventory.addGuitar("V99999", 1599.95, spec1)

def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:
        print("Erin, talvez você goste destas: ")
        for guitar in matchingGuitars:
            guitarSpec = guitar.getSpec()
            print(f"\nGuitarra: {guitar.getSerialNumber()} {guitarSpec.getBuilder().value} {guitarSpec.getModel()} {guitarSpec.getTypeG().value} guitar:\n{guitarSpec.getBackWood().value} na traseira e laterais,\n{guitarSpec.getTopWood().value} no tampo, com {guitarSpec.getNumStrings()} cordas\nEla pode ser sua por apenas US${guitar.getPrice():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

if __name__ == '__main__':
    main()
