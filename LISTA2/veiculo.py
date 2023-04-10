class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.setMarca(marca)
        self.setModelo(modelo)
        self.setAno(ano)
    
    def setMarca(self, marca):
        self._marca = marca
    
    def setModelo(self, modelo):
        self._modelo = modelo
    
    def setAno(self, ano):
        self._ano = ano
    
    def getMarca(self):
        return self._marca
    
    def getModelo(self):
        return self._modelo
    
    def getAno(self):
        return self._ano
    
    def infoVeiculo(self):
        return f"O veículo é da marca: " + self.getMarca() + " Modelo: " + self.getModelo() + " Ano: " + str(self.getAno())
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_de_portas):
        super().__init__(marca, modelo, ano)
        self.setQuantidadePorta(quantidade_de_portas)

    def setQuantidadePorta(self, quantidade_de_porta):
        self.__quantidade_de_porta = quantidade_de_porta

    def getQuantidadePorta(self):
        return self.__quantidade_de_porta
    
    def infoCarro(self):
        return f"O carro é da marca: " + self.getMarca() + ", modelo: " + self.getModelo() + ", ano: " + str(self.getAno()) +" e tem " + str(self.getQuantidadePorta()) + " portas!"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.setCilindradas(cilindradas)

    def setCilindradas(self, cilindradas):
        self._cilindradas = cilindradas
    
    def getCilindrdadas(self):
        return self._cilindradas
    
    def infoMoto(self):
        return f"A moto é da marca: " + self.getMarca() + ", modelo: " + self.getModelo() + ", ano: " + str(self.getAno()) +" e tem " + str(self.getCilindrdadas()) + " cilindradas!"


##teste
moto1 = Moto("Honda", "CG", 2020, 125)
print(moto1.infoMoto())
carro1 = Carro("Honda", "City", 2022, 4)
print(carro1.infoCarro())
