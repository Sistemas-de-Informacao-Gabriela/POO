class Pessoa():
    def __init__(self, nome, idade):
        self.setNome(nome)
        self.setIdade(idade)

    def setNome(self, nome):
        self._nome = nome

    def setIdade(self, idade):
        self._idade = idade
    
    def getNome(self):
        return self._nome
    
    def getIdade(self):
        return self._idade
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.setSalario(salario)

    def setSalario(self, salario):
        self._salario = salario

    def getSalario(self):
        return self._salario
    
    def aumentoSalarial(self, porcentagem):
        self._salario += self._salario * (porcentagem/100)
        return "O salário atual é: " + str(self.getSalario())
    
func1 = Funcionario("Gabriela", 23, 2000)
print(func1.aumentoSalarial(50))