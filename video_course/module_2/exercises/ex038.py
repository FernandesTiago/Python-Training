# comparacao de dois numeros (maior/menor/igual)

while True:
    numero1 = input('Digite um numero inteiro qualquer: ')
    if numero1.isnumeric():
        numero1 = float(numero1)
        break
    else:
        print('digite um numero valido!')

while True:
    numero2 = input('Digite outro numero inteiro qualquer: ')
    if numero2.isnumeric():
        numero2 = float(numero2)
        break
    else:
        print('digite um numero valido!')

if numero1 > numero2:
    print('O primeiro valor e maior que o segundo')
elif numero1 < numero2:
    print('O segundo valor e maior que o primeiro')
else:
    print('Os valores sao iguais')