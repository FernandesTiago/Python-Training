# Menu conta de valores

lo = 0

while True:
    try:
        n1 = int(input('qual o primeiro valor? '))
        break
    except ValueError:
        print('digite um numero inteiro')
while lo != 1:
    try:
        n2 = int(input('qual o segundo valor? '))
        lo += 1
    except ValueError:
        print('digite um numero inteiro')
#usei ambos while apenas para testar e aprender.

while True:
    print(f'''
    Oque deseja fazer com os numeros: \033[1;33m{n1}\033[m e \033[1;33m{n2}\033[m?
    
    \033[1;33m[1]\033[m Somar
    \033[1;33m[2]\033[m Multiplicar
    \033[1;33m[3]\033[m Maior
    \033[1;33m[4]\033[m Novos numeros
    \033[1;33m[5]\033[m Sair do programa
    ''')

    try:
        acao = int(input('qual a acao ?'))
        if 0 < acao <=5:
            if acao == 1:
                print(f'{n1} + {n2} = {n1 + n2}')
            elif acao == 2:
                print(f'{n1} * {n2} = {n1 * n2}')
            elif acao == 3:
                if n1 > n2:
                    print(f'{n1} > {n2}')
                elif n1 < n2:
                    print(f'{n1} < {n2}')
                else:
                    print(f'{n1} = {n2}')
            elif acao == 4:
                while True:
                    try:
                        n1 = int(input('qual o primeiro valor? '))
                        break
                    except ValueError:
                        print('digite um numero inteiro')
                while True:
                    try:
                        n2 = int(input('qual o segundo valor? '))
                        break
                    except ValueError:
                        print('digite um numero inteiro')
            else:
                print('Obrigado por testar meu programa!!')
                break
        else:
            print('O valor precisa ser um numero entre 1 e 5')
    except ValueError:
        print('O valor precisa ser um numero entre 1 e 5')
