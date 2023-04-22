class Usuario():
    def __init__(self, pontos, nart):
        self.setPontos(pontos)
        self.setNumArtigos(nart)
    
    def setPontos(self, pontos):
        self.pontos = pontos
    
    def setNumArtigos(self, nart):
        self.nart = nart
    
    def getNumArtigos(self):
        return self.nart
    
    def calcPontuacao():
        pass


class Autor(Usuario):

    def __init__(self, pontos, nart):
        super().__init__(pontos, nart)

    def calcPontuacao(self):
        pontos = self.nart * 10 + 20
        self.setPontos(pontos)
        return self.pontos
    
class Editor(Usuario):

    def __init__(self, pontos, nart):
        super().__init__(pontos, nart)

    def calcPontuacao(self):
        pontos = self.nart * 6 + 15
        self.setPontos(pontos)
        return self.pontos

autor1 = Autor(0, 8)
print(autor1.calcPontuacao())
editor1 = Editor(0, 15)
print(editor1.calcPontuacao())

    