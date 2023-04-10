class CCorrente():
    def __init__(self, numero, saldo, cliente):
        self.setNumero(numero)
        self.setSaldo(saldo)
        self.setCliente(cliente)
    
    def setNumero(self, numero):
        self.numero = numero

    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def setCliente(self, cliente):
        self.cliente = cliente
    
    def getSaldo(self):
        return self.saldo
    
    def creditar(valor):
        self.saldo += valor
        return "O saldo atual é de: " + str(self.getSaldo()) + " reais"
    
    def debitar(valor):
        self.saldo -= valor
        return "O saldo atual é de: " + str(self.getSaldo()) + " reais"

class CEspecial(CCorrente):
    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.setLimite(limite)

    def setLimite(self, limite):
        self.limite = limite
    
    def debitar(self, valor):
        if valor > (self.saldo + self.limite):
            return "Você não possui limite suficiente para esse valor"
        else:
            self.saldo -= valor
            return "O saldo atual é de: " + str(self.getSaldo()) + " reais"

class CPoupanca(CCorrente):
    def __init__(self, numero, saldo, cliente, saldoMinimo):
        super().__init__(numero, saldo, cliente)
        self.setSaldoMinimo(saldoMinimo)
    
    def setSaldoMinimo(self, saldoMinimo):
        self.saldoMinimo = saldoMinimo
    
    def getSaldoMinimo(self):
        return self.saldoMinimo
    
    def debitar(self, valor):
        if (self.saldo - valor) < self.saldoMinimo:
            return "Você não possui limite suficiente para esse valor"
        else:
            self.saldo -= valor
            return "O saldo atual é de: " + str(self.getSaldo()) + " reais"

class CInvestimento(CCorrente):
    def __init__(self, numero, saldo, cliente, diaInvestimento, periodo):
        super().__init__(numero, saldo, cliente)
        self.setDiaInvestimento(diaInvestimento)
        self.setPeriodo(periodo)
    
    def setDiaInvestimento(self, diaInvestimento):
        self.diaInvestimento = diaInvestimento
    
    def setPeriodo(self, periodo):
        self.periodo = periodo

    def atualizarSaldo(self, saldo):
        self.saldo = saldo
        return "Saldo atual: " + str(self.saldo)

##teste

CEspecial1 = CEspecial(1415, 1000, "Gabriela", 500)
print(CEspecial1.debitar(1501))
CPoupanca1 = CPoupanca(1614, 2000, "Chris", 200)
print(CPoupanca1.debitar(1801))
CInvestimento1 = CInvestimento(1719, 6000, "Joana", 15, 15)
print(CInvestimento1.atualizarSaldo(7000))

