class Animal():
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Latidos"

class Gato(Animal):
    def falar(self):
        return "Miados"

animais = (Cachorro(), Gato())

for animal in animais:
    print(animal.falar())