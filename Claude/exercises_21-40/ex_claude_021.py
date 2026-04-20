# starting learning class

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
    def adicionar_pontos(self, quantidade):
        self.pontuacao += quantidade
    def resetar(self):
        self.pontuacao = 0
    def __str__(self):
        return f'{self.nome} Pontuacao:{self.pontuacao}'

jogador1 = Jogador('Tiago')
jogador2 = Jogador('Juliana')

jogador1.adicionar_pontos(100)
jogador1.resetar()
jogador2.adicionar_pontos(500)
print(jogador2)
print(jogador1)
