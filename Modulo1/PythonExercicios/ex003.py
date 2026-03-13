while True:
    try:
        valor1 = int(input('qual o primeiro valor? '))
        operador = input('qual o operador? (+, -, x, / )? ')
        valor2 = int(input('qual o segundo valor? '))

        if operador == '+':
            print(valor1+valor2)
        elif operador == '-':
            print(valor1-valor2)
        elif operador == 'x':
            print(valor1*valor2)
        elif operador == '/':
            print(valor1/valor2)
        else:
            print('o operador deve conter na lista!')

        break

    except:
        print('o valor deve ser um numero!')