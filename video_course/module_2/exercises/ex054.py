# contador de pessoas com mais de 18 anos

from datetime import date

ano_atual = date.today().year
anos = 0

for c in range(1,8):
    while True:
        try:
            ano_nascimento = int(input('quando voce nasceu? '))
            break
        except ValueError:
            print('digite um numero')
    if ano_atual - ano_nascimento >= 18:
        anos += 1
if anos > 0:
    print(f'{anos} pessoas sao 18+')
else:
    print('ninguem eh 18+')
