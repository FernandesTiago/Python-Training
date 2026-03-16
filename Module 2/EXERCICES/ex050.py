# digitacao de 6 numeros e soma apenas dos pares

soma = 0

for c in range(0,6):
    while True:
        try:
            n = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Digite um numero inteiro!!')
    if n % 2 == 0:
        soma = soma + n

print(soma)