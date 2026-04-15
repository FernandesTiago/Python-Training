#  analizar o ano de nascimento de um Homem e verificar a relacao de recrutamente militar

import datetime

ano_atual = datetime.date.today().year

while True:

    ano = input('Digite seu ano de nascimento: ')

    if ano.isnumeric():
        ano = int(ano)
        if 1900 <= ano <= ano_atual:
            break
        else:
            print(f'O ano deve estar entre \033[32m1900\033[m e \033[32m{ano_atual}\033[m')
    else:
        print('O ano deve ser um numero inteiro.')

idade = ano_atual - ano

if idade < 18:
    print(f'Voce tem \033[32m{18 - idade}\033[m anos para se alistar.')
elif idade == 18:
    print(f'\033[32mVoce se alista esse ano.\033[m')
else:
    print(f'voce tinha que se alistar \033[32m{idade - 18}\033[m anos atras.')
