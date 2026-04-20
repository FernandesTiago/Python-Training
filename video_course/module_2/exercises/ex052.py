# Checagem de numero primo

while True:
    try:
        n = int(input('qual o numero que deseja saber se eh primo? '))
        break
    except ValueError:
        print('deve ser um numero inteiro')

primo = 0
if n == 0 or n == 1:
    print('nao eh um numero primo')
else:
    for c in range(1,n+1):
        if n % c == 0:
            print(f'\033[1;32m{c}\033[m', end=' ')
            primo += 1
        else:
            print(c, end=' ')
    print()
    if primo > 2:
        print(f'nao eh um numero primo, ele eh divisivel {primo} vezes')
    else:
        print(f'eh um numero primo')
