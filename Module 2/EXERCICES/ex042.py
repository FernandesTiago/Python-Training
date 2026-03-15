# Diga se eh um triangulo e qual triangulo ele eh

a = int(input('qual a medida de uma reta? '))
b = int(input('qual a medida de outra reta? '))
c = int(input('qual a medida de outra reta? '))

lista = [a, b, c]
nova_lista = sorted(lista)

if nova_lista[0] + nova_lista[1] > nova_lista[2]:
    print('é um triangulo!!')
    if a == b == c:
        print('Equilatero')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('não é um triangulo')
