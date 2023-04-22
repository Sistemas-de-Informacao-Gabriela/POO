<<<<<<< HEAD
class Empregado():
    def __init__(self, codigo, nome, email, salario):
        self.setCodigo(codigo)
        self.setNome(nome)
        self.setEmail(email)
        self.setSalario(salario)

    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def setNome(self, nome):
        self.nome = nome
    
    def setEmail(self, email):
        self.email = email

    def setSalario(self, salario):
        self.salario = salario
    
    def getSalario(self):
        return self.salario

    def aumentoSalario(self, percentual):
        self.salario += self.salario * (percentual/100)
        return "Salário atual: " + str(self.salario)
    
class Chefe(Empregado):
    def __init__(self, codigo, nome, email, salario, beneficio):
        super().__init__(codigo, nome, email, salario)
        self.setBeneficio(beneficio)

    def setBeneficio(self, beneficio):
        self.beneficio = beneficio
    
    def aumentoSalario(self, percentual):
        self.salario += self.salario * (percentual/100) + self.beneficio
        return "Salario atual: " + str(self.getSalario())
    
class Estagiario(Empregado):
    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.setDesconto(desconto)
    
    def setDesconto(self, desconto):
        self.desconto = desconto
    
    def aumentoSalario(self, percentual):
        self.salario += (self.salario * (percentual/100)) - self.desconto
        return "Salario atual: " + str(self.salario)


##testes
Empregado1 = Empregado(1514, "Gabriela", "gabe@gmail.com", 2000)
print(Empregado1.aumentoSalario(30))
Chefe1 = Chefe(1916, "Boss", "boss@gmail.com", 5000, 300)
=======
class Empregado():
    def __init__(self, codigo, nome, email, salario):
        self.setCodigo(codigo)
        self.setNome(nome)
        self.setEmail(email)
        self.setSalario(salario)

    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def setNome(self, nome):
        self.nome = nome
    
    def setEmail(self, email):
        self.email = email

    def setSalario(self, salario):
        self.salario = salario
    
    def getSalario(self):
        return self.salario

    def aumentoSalario(self, percentual):
        self.salario += self.salario * (percentual/100)
        return "Salário atual: " + str(self.salario)
    
class Chefe(Empregado):
    def __init__(self, codigo, nome, email, salario, beneficio):
        super().__init__(codigo, nome, email, salario)
        self.setBeneficio(beneficio)

    def setBeneficio(self, beneficio):
        self.beneficio = beneficio
    
    def aumentoSalario(self, percentual):
        self.salario += self.salario * (percentual/100) + self.beneficio
        return "Salario atual: " + str(self.getSalario())
    
class Estagiario(Empregado):
    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.setDesconto(desconto)
    
    def setDesconto(self, desconto):
        self.desconto = desconto
    
    def aumentoSalario(self, percentual):
        self.salario += (self.salario * (percentual/100)) - self.desconto
        return "Salario atual: " + str(self.salario)


##testes
Empregado1 = Empregado(1514, "Gabriela", "gabe@gmail.com", 2000)
print(Empregado1.aumentoSalario(30))
Chefe1 = Chefe(1916, "Boss", "boss@gmail.com", 5000, 300)
>>>>>>> dae8616c3526b0808c8d01fd9715215a691bcd69
print(Chefe1.aumentoSalario(20))