class Ingresso():
    def __init__(self, valor):
        self.setValor(valor)

    def setValor(self, valor):
        self.valor = valor
    
    def imprimeValor(self):
        return self.valor

class Vip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.setAdicional(adicional)

    def setAdicional(self, adicional):
        self.adicional = adicional
    
    def imprimeValor(self):
        return self.valor + self.adicional
    
class Normal(Ingresso):
    def tipoIngresso():
        return "Ingresso Normal"

class CamaroteInferior(Vip):
    def __init__(self, localizacao):
        self.setLocalizacao(localizacao)
    
    def setLocalizacao(self, localizacao):
        self.localizacao = localizacao
    
    def imprimeLocalizacao(self):
        return "O local é: " + self.localizacao

class CamaroteSuperior(Vip):
    def __init__(self, valor, adicional, valorAdicional):
        super().__init__(valor, adicional)
        self.setValorAdicional(valorAdicional)

    def setValorAdicional(self, valorAdicional):
        self.valorAdicional = valorAdicional
    
    def imprimeValor(self):
        return "Valor do ingresso: " + str(self.valor + self.adicional + self.valorAdicional)

##teste
CamSup1 = CamaroteSuperior(50, 30, 20)
print(CamSup1.imprimeValor())
