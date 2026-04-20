# inheritance

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f'{self.nome} está comendo')


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
    def fazer_som(self):
        print(f'{self.nome} diz: Au au!')
    def __str__(self):
        return f'{self.nome} da raca {self.raca}'


class Gato(Animal):
    def fazer_som(self):
        print(f'{self.nome} diz: Miau!')

cachorro = Cachorro('Mocoto','lulu da palmeranea')
gato = Gato('gabriel')

animais = [gato, cachorro]

for i in range(0,len(animais)):
    animais[i].fazer_som()