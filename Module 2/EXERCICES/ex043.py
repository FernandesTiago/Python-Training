# calculo IMC

while True:
    try:
        peso = float(input('qual o seu peso? '))
        if 1 <= peso <= 500:
            break
        else:
            print('O valor deve estar entre 1 e 500')
    except ValueError:
        print('O valor deve estar entre 1 e 500')

while True:
    try:
        altura = float(input('qual a sua altura em metros? '))
        if 1 <= altura <= 3:
            break
        else:
            print('O valor deve estar entre 1 e 3')
    except ValueError:
        print('O valor deve estar entre 1 e 3')

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')

print(f'{imc:.2f}')
