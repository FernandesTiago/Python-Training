# n vezes da sequencia fibonacci de n

a = 0
b = 1

while True:
    try:
        quantidade = int(input('quantas casas quer ver a sequencia de Fibonacci? '))
        if quantidade > 0:
            break
        else:
            print('Valor invalido')
    except ValueError:
        print('Valor invalido')
while quantidade > 0:
    print(f'{a}', end=' ')
    a,b = b, a+b
    quantidade -= 1