class Carro():
    def dirigir(self):
        pass

class CarroGasolina(Carro):
    def dirigir(self):
        return "Gasolina"

class CarroEletrico(Carro):
    def dirigir(self):
        return "Bateria"

carrogasolina1 = CarroGasolina()
carroeletrico1 = CarroEletrico()
