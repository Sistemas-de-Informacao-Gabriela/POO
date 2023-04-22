class Animal():
    def __init__(self, som):
        self.setFala(som)
    
    def setFala(self, som):
        self.fala = som

    def falar(self):
        pass
    
class Cachorro(Animal):
    def __init__(self, som):
        super().__init__(som)
    
    def falar(self):
        return self.fala

class Gato(Animal):
    def __init__(self, som):
        super().__init__(som)
    
    def falar(self):
        return self.fala

class Peixe(Animal):
    def __init__(self, som):
        super().__init__(som)
    
    def falar(self):
        return self.fala


cachorro1 = Cachorro("Auau")
print(cachorro1.falar())
gato1 = Gato("Miau")
print(gato1.falar())
peixe1 = Peixe("Bubu")
print(peixe1.falar())