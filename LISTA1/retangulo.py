class Retangulo:
    def __init__(self, largura, comprimento):
        self.setLargura = largura
        self.setComprimento = comprimento
    
    def setLargura(self, largura):
        self.largura = largura
    
    def setComprimento(self.comprimento):
        self.comprimento =  comprimento
    
    def getLargura(self):
        return self.largura
    
    def getComprimento(self):
        return self.comprimento

    def calculaArea(self):
        return self.largura * self.comprimento
    
    def calculaPerimetro(self):
        return (self.largura * 2) + (self.comprimento * 2)

def calculaPisos():
    dist1 = input("Informe a medida do comprimento: ")
    dist2 = input("Informe a medida da largura: ")




##TERMINAR