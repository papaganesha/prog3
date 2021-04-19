

class Animal():
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def get_Animal(self):
        print("Animal\n        nome: {}\n        raça: {}".format(self.nome, self.raca))


cachorroLoco = Animal("Bob", "Cachorro")


class Gato(Animal):
    def __init__(self, nome, raca = 'Gato'):
        Animal.__init__(self, nome, raca)
        self.get_Gato()


    def get_Gato(self):
        print("\nGato\n   nome: {}\n   raça: {}".format(self.nome, self.raca))

    def mia(self):
        print("   {} faz miau, miau".format(self.nome))


class Cachorro(Animal):
    def __init__(self, nome, raca='Cachorro'):
        Animal.__init__(self, nome, raca)
        self.get_Cachorro()

    def get_Cachorro(self):
        print("\nCachorro\n   nome: {}\n   raça: {}".format(self.nome, self.raca))

    def late(self):
        print("   {} faz woof, woof".format(self.nome))


gatinho = Gato("Jerbes")
gatinho.mia()

cachorrinho = Cachorro("Tob")
cachorrinho.late()