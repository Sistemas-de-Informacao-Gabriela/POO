class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.setNome(nome)
        self.setIdade(idade)
        self.setPeso(peso)
        self.setAltura(altura)

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade
    
    def setPeso(self, peso):
        self.peso = peso

    def setAltura(self, altura):
        self.altura = altura

    def getEnvelhecer(self, id):
        self.idade = self.idade + id
        if(self.idade<21):
            self.altura = self.altura + id * 0.005
        return f"{self.nome} agora tem {self.idade} anos e mede {round(self.altura,3)}m"
    
    def getEngordar(self, eng):
        self.peso = self.peso + eng
        return self.peso
    
    def getEmagrecer(self, ema):
        self.peso = self.peso + ema

pessoa1 = Pessoa("Maria", 17, 63, 1.68)
print(pessoa1.getEnvelhecer(3))
