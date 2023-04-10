class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)
    
    def setNome(self, nome):
        self.nome = nome

    def setFome(self, fome):
        self.fome = fome

    def setSaude(self, saude):
        self.saude = saude
    
    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude
    
    def getIdade(self):
        return self.idade
    
    def calculaHumor(self):
        if (self.fome + self.saude)/2 < 50:
            return "Tamagushi está triste!"
        else:
            if (self.fome + self.saude)/2 >= 50 and (self.fome + self.saude)/2 < 70:
                return "Tamagushi está feliz!"
            else:
                return "Tamagushi está muito feliz!"

##teste
tama = Tamagushi("Lily", 30, 60, 4)
print(tama.calculaHumor())
print(tama.getNome())
tama.setNome("Luki")
print(tama.getNome())
        