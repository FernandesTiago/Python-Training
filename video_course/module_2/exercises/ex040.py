# calculo de media do aluno

while True:
    try:
        nota_1 = float(input('\033[1;31mDigite sua primeira nota: \033[m'))
        if 0 <= nota_1 <= 10:
            break
        else:
            print(' a nota deve ser um numero inteiro entre 0 e 10.')
    except ValueError:
        print(' a nota deve ser um numero inteiro entre 0 e 10.')

while True:
    try:
        nota_2= float(input('\033[1;31mDigite sua segunda nota: \033[m'))
        if 0 <= nota_2 <= 10:
            break
        else:
            print(' a nota deve ser um numero inteiro entre 0 e 10.')
    except ValueError:
        print(' a nota deve ser um numero entre 0 e 10.')

media = (nota_1 + nota_2) / 2

if media >= 7:
    print('\033[1;32mVOCE FOI APROVADO!! PARABENS!!\033[m')
    print(f'MEDIA: \033[1;32m{media:.2f}\033[m')
elif media < 5:
    print('\033[1;31mVoce foi reprovado...\033[m')
    print(f'MEDIA: \033[1;31m{media:.2f}\033[m')
else:
    print('Voce esta de \033[1;33mrecuperacao\033[m')
    print(f'MEDIA: \033[1;33m{media:.2f}\033[m')
