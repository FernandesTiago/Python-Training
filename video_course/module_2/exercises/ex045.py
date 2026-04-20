# Jokenpo

from random import randint
from time import sleep

print('-=-'*20)
print('                  BEM VINDO AO JOKENPO!!!!')
print('-=-'*20)

# 1 Pedra, 2 Papel, 3 Tesoura

while True:
    cpu = randint(1, 3)
    while True:
        try:
            jogada = input('Qual a sua jogada? (Pedra, Papel, Tesoura) ').strip().upper()
            if jogada == 'PEDRA' or jogada == 'PAPEL' or jogada == 'TESOURA':
                break
            else:
                print(('Pedra, papel ou tesoura? '))
        except ValueError:
            print('Pedra, papel ou tesoura? ')

    print('CALCULANDO...')
    sleep(3)

    if jogada == 'PEDRA' and cpu == 1 or jogada == 'PAPEL' and cpu == 2 or jogada == 'TESOURA' and cpu == 3:
            print('EMPATE!')
    elif jogada == 'PEDRA' and cpu == 2 or jogada == 'PAPEL' and cpu == 3 or jogada == 'TESOURA' and cpu == 1:
        print('voce perdeu...')
    else:
        print('VOCE GANHOUU!!!!!')
        break


# VERSÃO AVANÇADA - estudar depois

# 1. Usar dicionário para mapear jogadas e resultados:
# opcoes = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
# cpu_jogada = opcoes[randint(1, 3)]

# 2. Usar dicionário para definir quem vence quem:
# vence = {'PEDRA': 'TESOURA', 'PAPEL': 'PEDRA', 'TESOURA': 'PAPEL'}
# if vence[jogada] == cpu_jogada: print('VOCE GANHOU!')

# 3. Usar função para validar input:
# def pedir_jogada():
#     while True:
#         jogada = input('...').strip().upper()
#         if jogada in ['PEDRA', 'PAPEL', 'TESOURA']:
#             return jogada

# 4. Contador de pontos com placar:
# vitorias, derrotas, empates = 0, 0, 0

# 5. Perguntar se quer jogar de novo em vez de parar só na vitória