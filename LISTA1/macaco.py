class Macaco:
    def __init__(self, nome, bucho):
        self.setNome(nome)
        self.setBucho(bucho)

    def setNome(self, nome):
        self.nome = nome
    
    def setBucho(self, bucho):
        self.bucho = []
        self.bucho.append(bucho)
    
    def getNome(self):
        return self.nome

    def getBucho(self):
        return self.bucho

    def alimentaMacaco(self, comida):
        if comida.lower() != "macaco":
            self.bucho.append(comida)
            return self.nome + " comeu: " + comida
        else:
            return "Um macaco não pode se alimentar de outro!"

    def verBucho(self):
        if len(self.bucho) > 0:
            return self.bucho
        else: 
            return "O estômago do macaco está vazio!"

    def digerir(self):
        if len(self.bucho) > 0:
            del self.bucho[0]
        else:
            return "Não há alimentos para serem digeridos!"


##testes
Macaco1 = Macaco("caco", "Banana")
print(Macaco1.verBucho())
print(Macaco1.alimentaMacaco("MACACO"))
print(Macaco1.alimentaMacaco("Maça"))
print(Macaco1.verBucho())
Macaco1.digerir()
print(Macaco1.verBucho())
Macaco1.digerir()
print(Macaco1.verBucho())
print(Macaco1.alimentaMacaco("macaco"))
print(Macaco1.verBucho())
print(Macaco1.alimentaMacaco("laranja"))
print(Macaco1.verBucho())

