# media de numeros, pergunta de continuacao, maior, menor

while True:
    try:
        v = int(input('digite um valor: '))
        soma = maior = menor = v
        quantidade = 1
        break
    except ValueError:
        print('Valor invalido')
while True:
    v = input('''Se nao desejar continuar digite ( sair )
digite outro valor: ''')
    try:
        v = int(v)
        soma += v
        quantidade += 1
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    except ValueError:
        v = v.strip().upper()
        if v == 'SAIR':
            break
        else:
            print('Valor invalido')
print(f'''
A media dos valores eh de {soma/quantidade}
O maior valor foi {maior}
O menor valor foi {menor}
''')
