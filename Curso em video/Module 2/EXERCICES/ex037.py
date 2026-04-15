# Converter um numero inteiro em Binario, Octal e Hexadecimal.

while True:

    numero = input('Digite um numero inteiro qualquer: ')
    if numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Digite um numero inteiro!')

while True:

    base = input('qual quase de conversao voce quer? (1-Binario, 2-octal, 3-hexadecimal) ')

    if base == '1':
        print(bin(numero)[2:])
        break
    elif base == '2':
        print(oct(numero)[2:])
        break
    elif base == '3':
        print(hex(numero)[2:])
        break
    else:
        print('Digitou o valor da base errado!!')
