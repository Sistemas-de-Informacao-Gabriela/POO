class Quadrado:
    def __init__(self, lado):
        self.setLado(lado)
    
    def setLado(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado
    
    def calculaArea(self):
        return self.lado * self.lado

quadrado1 = Quadrado(2)
print(quadrado1.calculaArea())