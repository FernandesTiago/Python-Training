# checar se uma palavra eh um polindromo

while True:
    p = input('Escreva uma palavra ').upper().replace(' ','')
    if p.isnumeric() or p.isdigit() or p.find('.') != -1 or p == '':
        print('digite uma frase')
    else:
        break
pi = p[::-1]
if p == pi:
    print('eh um polindro')
else:
    print('nao eh um polindro')