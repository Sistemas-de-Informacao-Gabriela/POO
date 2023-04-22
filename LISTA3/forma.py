class Forma():
    def area():
        pass

class Circulo(Forma):
    def area(self, raio):
        self.area = 2 * 3.1415 * raio
        return self.area

class Quadrado(Forma):
    def area(self, lado):
        self.area = lado * lado
        return self.area

formas = (Circulo(), Quadrado())

for forma in formas:
    print(forma.area(10))