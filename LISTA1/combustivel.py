class BombaCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, qtdCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQtdCombustivel(qtdCombustivel)
    
    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = valorLitro
    
    def setQtdCombustivel(self, qtdCombustivel):
        self.qtdCombustivel = qtdCombustivel

    def getTipoCombustivel(self):
        return self.tipoCombustivel

    def getValorLitro(self):
        return self.valorLitro

    def getQtdCombustivel(self):
        return self.qtdCombustivel

    def abastecerPorValor(self, valor):
        abastecido = valor / self.valorLitro
        self.qtdCombustivel -= abastecido
        return "O carro foi abastecido com " + str(round(abastecido,2)) + " litros"

    def abastecerPorLitro(self, litro):
        abastecido = litro * self.valorLitro
        self.qtdCombustivel -= litro
        return "O valor a ser pago pelo cliente é: " + str(round(abastecido,2)) + " reais"
    
    


##teste
abastece1 = BombaCombustivel("Gasolina", 3, 2000)
print(abastece1.abastecerPorValor(50))
print(abastece1.abastecerPorLitro(10))
print(abastece1.getQtdCombustivel())
