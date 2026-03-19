# 5 valores em uma lista, maior, menor e posicoes

lista = []
loop = 0

while loop < 5:
    try:
        n = int(input('digite um valor: '))
        lista.append(n)
        loop += 1
    except ValueError:
        print('Valor invalido')

maior = max(lista)
menor = min(lista)

print(f'{', '.join(str(i) for i in lista)} {maior} {menor} {lista.index(maior)} {lista.index(menor)}')