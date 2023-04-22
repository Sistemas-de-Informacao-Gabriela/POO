class ContaBancaria():
    def deposito(self, depositar):
        self.saldo = depositar
        return self.saldo
    
    def retirada(self, retirar):
        self.saldo -= retirar
        return self.saldo

class ContaPoupanca(ContaBancaria):
    def deposito(self, depositar, juros = 1.3):
        self.saldo = depositar * juros
        return self.saldo
    
    def retirada(self, retirar):
        self.saldo -= retirar
        return self.saldo

class ContaCorrente(ContaBancaria):
    def deposito(self, depositar, juros = 1.2):
        self.saldo = depositar * juros
        return self.saldo
    
    def retirada(self, retirar):
        self.saldo -= retirar
        return self.saldo

contap = ContaPoupanca()
contac = ContaCorrente()

contas = (contap, contac)

for conta in contas:
    print(conta.deposito(100))
    print(conta.retirada(50))
