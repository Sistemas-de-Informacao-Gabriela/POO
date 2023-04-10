class Pessoa():
    def __init__(self, nome, idade):
        self.setNome(nome)
        self.setIdade(idade)
    
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

    def retornaInfo(self):
        return "Nome: " + self.nome + " Idade: " + self.idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.setNota(nota)

    def setNota(self, nota):
        self.nota = nota
    
    def getNota(self):
        return self.nota

    def retornaInfo(self):
        return "Nome: " + self.getNome() + " Idade: "+ str(self.getIdade()) + " Nota: " + str(self.nota)

aluno1 = Aluno("Gabriela", 23, 9.5)
print(aluno1.retornaInfo())