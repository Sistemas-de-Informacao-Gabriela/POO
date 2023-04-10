class Animal():
    def __init__(self, nome, peso):
        self.setNome(nome)
        self.setPeso(peso)

    def setNome(self, nome):
        self._nome = nome

    def setPeso(self, peso):
        self._peso = peso
    
    def getNome(self):
        return self._nome
    
    def getPeso(self):
        return self._peso
    
    def comer(self, comida):
        return self.getNome() + " comeu: " + comida
    

class Cachorro(Animal):    

    def latir(self):
        return "AU AU"

class Gato(Animal):
    
    def miar(self):
        return "Miau"
    
##Teste

doguinho = Cachorro("Nino", 15)
print(doguinho.latir())
print(doguinho.comer("Carne"))