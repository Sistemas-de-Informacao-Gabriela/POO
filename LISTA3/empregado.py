class Empregado():
    def pagarSalario():
        pass

class EmpregadoHora(Empregado):
    def pagarSalario(self, salario, horas):
        self.salario = salario * horas
        return self.salario

class EmpregadoMes(Empregado):
    def pagarSalario(self, salario, dias):
        self.salario = salario * dias
        return self.salario

funchorista = EmpregadoHora()
funcmensalista = EmpregadoMes()

funcionarios = (funchorista, funcmensalista)

for funcionario in funcionarios:
    print(funcionario.pagarSalario(50, 30))