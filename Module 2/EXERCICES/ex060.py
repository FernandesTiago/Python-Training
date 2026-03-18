# fatorial de um numero

while True:
    try:
        factor = int(input('Qual valor deseja fatoriar? '))
        break
    except ValueError:
        print('Valor invalido')

answer = factor

if factor > 0:
    print(f'{factor}! = ', end='')
    while factor > 1:
        print(f'{factor} * ', end='')
        factor -= 1
        answer *= factor
    print(f'{factor} = ', end='')
    print(answer)
elif factor == 0:
    print('O fatorial de 0 eh 1')
else:
    print('O valor deve ser maior ou igual a zero!')