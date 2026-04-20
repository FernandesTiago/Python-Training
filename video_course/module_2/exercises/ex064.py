# app que permite digitar infinitos numeros ate digitar 999, mostrar quantos numeros foram e soma entre eles.

soma = 0
contagem = 0

while True:
    try:
        numero = int(input('Digite um numero: '))
        if numero == 999:
            print(f'a soma dos valroes eh de {soma}. Itens somados: {contagem}')
            break
        else:
            soma += numero
            contagem += 1
    except ValueError:
        print('Valor invalido')