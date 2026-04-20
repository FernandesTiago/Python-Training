# emprestimo bancario para compra de casa

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('qual seu salario? R$'))
anos = int(input('em quantos anos deseja pagar a casa? '))

prestacao = casa / (anos * 12)
saldo_maximo = salario * 30 / 100

if prestacao < saldo_maximo:
    print(f'voce \033[32mpode \033[mfinanciar a casa e deve pagar \033[30;42mR${prestacao:.2f}\033[m de prestacao.')
else:
    print(f'Voce \033[31mnao \033[mpode financiar a casa.')
    print(f'O valor da prestacao eh de \033[32mR${prestacao:.2f}\033[m e o valor maximo que voce pode pagar eh \033[32mR${saldo_maximo:.2f}\033[m')


