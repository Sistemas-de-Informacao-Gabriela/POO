from enum import Enum

class Builder(Enum):
    FENDER = "fender"

class TypeG(Enum):
    ELETRIC = "eletric"
    ACOUSTIC = "acoustic"

class Wood(Enum):
    MAPLE = "maple"
    MOGNO = "mogno"
    ALDER = "alder"
    ASH = "ash"
    ROSEWOOD = "rosewood"
    EBANO = "ebano"

class Guitar():
    def __init__(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = GuitarSpec(builder, model, typeG, backWood, topWood)
    
    def getSerialNumber(self):
        return self.serialNumber
    
    def getPrice(self):
        return self.price
    
    def setPrice(self, newPrice):
        self.price = newPrice
    
    def getSpec(self):
        return self.spec
    
class GuitarSpec():
    def __init__(self, builder, model, typeG, backWood, topWood):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood
    
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
    
    def __str__(self):
        return f"{self.builder.value} {self.model} {self.typeG.value} guitar:\n   {self.backWood.value} back and sides,\n   {self.topWood.value} top."

class Inventory:
    def __init__(self):
        self.guitars = []
    
    def addGuitar(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        guitar = Guitar(serialNumber, price, builder, model, typeG, backWood, topWood)
        self.guitars.append(guitar)
    
    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def searchGuitar(self, searchGuitar):
        guitars = []
        for guitar in self.guitars:
            if searchGuitar.getBuilder() != guitar.getSpec().getBuilder():
                continue
            if searchGuitar.getModel() != guitar.getSpec().getModel():
                continue
            if searchGuitar.getTypeG() != guitar.getSpec().getTypeG():
                continue
            if searchGuitar.getBackWood() != guitar.getSpec().getBackWood():
                continue
            if searchGuitar.getTopWood() != guitar.getSpec().getTopWood():
                continue
            guitars.append(guitar)
        return guitars
    
inventory = Inventory()

inventory.addGuitar("V95693", 1499.95, Builder.FENDER, "Stratocastor", TypeG.ELETRIC, Wood.ALDER, Wood.ALDER)
inventory.addGuitar("V9512", 1549.95, Builder.FENDER, "Stratocastor", TypeG.ELETRIC, Wood.ALDER, Wood.ALDER)

whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELETRIC, Wood.ALDER, Wood.ALDER)

guitars = inventory.searchGuitar(whatErinLikes)

if guitars:
    for guitar in guitars:
        print(f"Erin, you might like this {guitar.getSpec()}:\nYou can have it for only ${guitar.getPrice()}!\n")
else:
    print("Sorry, Erin, we have nothing for you.")
