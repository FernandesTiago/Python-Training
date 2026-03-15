# Categoria atletica de acordo com a idade no esporte

from datetime import date

ano_atual = date.today().year

while True:
    try:
        ano = int(input('Quando voce nasceu? '))
        if 1900 <= ano <= ano_atual:
            break
        else:
            print(f'O deve ser um ano entre 1900 e {ano_atual}.')
    except ValueError:
        print(f'O deve ser um ano entre 1900 e {ano_atual}.')

idade = ano_atual - ano

while True:
    try:
        idade_natacao = int(input('com quantos anos voce comecou a natacao? '))
        if idade_natacao <= idade:
            break
        else:
            print(f'Voce treina a mais tempo que e vivo...')
    except ValueError:
        print(f'O valor deve ser Menor que sua idade.')

anos_de_natacao = idade - idade_natacao

if anos_de_natacao <= 1:
    print('MIRIM')
elif anos_de_natacao <= 2:
    print('INFANTIL')
elif anos_de_natacao <= 3:
    print('JUNIOR')
elif anos_de_natacao <= 4:
    print('SENIOR')
else:
    print('MASTER')
