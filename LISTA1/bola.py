class Bola:
    def __init__(self, cor, circunf, material):
        self.setCor(cor)
        self.setCircunf(circunf)
        self.setMaterial(material)

    def setCor(self, cor):
        self.cor = cor
    
    def setCircunf(self, circunf):
        self.circunf = circunf
    
    def setMaterial(self, material):
        self.material = material

    def getCor(self):
        return self.cor

Bola1 = Bola("Azul", 12, "Plastico")
print(Bola1.getCor())