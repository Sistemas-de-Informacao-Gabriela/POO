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

class Guitar:
    def __init__(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        self.serialNumber = serialNumber
        self.price = price
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

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
    
class Inventory:
    def __init__(self):
        self.guitars = []

# addGuitar() pega todas as propriedades necessárias para criar uma nova instância da Classe Guitar, 
# cria uma e a adiciona ao inventário
    def addGuitar(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        guitar = Guitar(serialNumber, price, builder, model, typeG, backWood, topWood)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

# Este método é um pouco confuso... ele compara cada propriedade do objeto Guitar 
# que é passado com cada objeto Guitar no inventário (estoque) do Rick
    def searchGuitar(self, searchGuitar):
        guitars = []
        for guitar in self.guitars:
            # ignora o 'serialNumber' porque é único
            # ignora o 'price' porque é único
            builder = searchGuitar.getBuilder()
            if builder is not None and builder != "" and builder != guitar.getBuilder():
                continue
            model = searchGuitar.getModel()
            if model is not None and model != "" and model != guitar.getModel():
                continue
            typeG = searchGuitar.getTypeG()
            if typeG is not None and typeG != "" and typeG != guitar.getTypeG():
                continue
            backWood = searchGuitar.getBackWood()
            if backWood is not None and backWood != "" and backWood != guitar.getBackWood():
                continue
            topWood = searchGuitar.getTopWood()
            if topWood is not None and topWood != "" and topWood != guitar.getTopWood():
                continue
            guitars.append(guitar)
        return guitars
    

# Testando o Sistema

# Set up Rick’s guitar inventory
inventory = Inventory()

# Adiciona guitarras ao estoque
inventory.addGuitar("V95693", 1499.95, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
inventory.addGuitar("V95695", 1200.90, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
#inventory.addGuitar("11277", 3999.95, "Collings", "CJ", "acoustic", "Indian Rosewood", "Indian Rosewood")


# Buscando por uma guitarra que o Erin gosta: Fender Stratocastor elétrica com corpo de Alder e tampo de Alder
whatErinLikes1 = Guitar("", 0, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)

guitars = inventory.searchGuitar(whatErinLikes1)
for guitar in guitars:
    if guitar:
        print(f"Erin, you might like this {guitar.getBuilder()} {guitar.getModel()} {guitar.getTypeG()} guitar:\n{guitar.getBackWood()} back and sides,\n{guitar.getTopWood()} top.\nYou can have it for only ${guitar.getPrice()}!")
else:
    print("Sorry, Erin, we have nothing for you.")