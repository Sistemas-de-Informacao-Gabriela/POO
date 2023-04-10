class Area():
    pass

class Retangulo(Area):
    def __init__(self, comprimento, largura):
        self.setComprimento(comprimento)
        self.setLargura(largura)

    def setComprimento(self, comprimento):
        self.comprimento = comprimento

    def setLargura(self, largura):
        self.largura = largura
    
    def calculaArea(self):
        area = self.comprimento * self.largura
        return area

class Circulo(Area):
    def __init__(self, raio):
        self.setRaio(raio)

    def setRaio(self, raio):
        self.raio = raio
    
    def calculaArea(self):
        area = 2 * 3.1415 * self.raio
        return area

##teste
retangulo1 = Retangulo(2,2)
print(retangulo1.calculaArea())
circulo1 = Circulo(4)
print(circulo1.calculaArea())