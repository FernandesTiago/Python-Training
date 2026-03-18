# nome idade e sexo de 4 pessoas: media de idade, homem mais velho e mulheres com menos de 20

sexos = []
nomes = []
idades = []

for c in range(1,5):
    while True:
        sexo = input('qual seu sexo? (H, F) ').strip().upper()
        if sexo == 'H' or sexo == 'F':
            sexos.append(sexo)
            break
        else:
            print('Digite M ou F')
    while True:
        nome = input('qual seu nome? ').strip().title()
        if nome.isnumeric() or nome.isdigit() or nome.find('.') != -1:
            print('digite seu nome!')
        else:
            nomes.append(nome)
            break
    while True:
        try:
            idade = int(input('qual sua idade? '))
            if 0 < idade <= 100:
                idades.append(idade)
                break
            else:
                print('digite um valor de 1 a 100')
        except ValueError:
            print('digite um valor de 1 a 100')

mulheres_menores = []
idade_homens = []

for b in range(len(sexos)):
    if sexos[b] == 'F' and idades[b] < 20:
        mulheres_menores.append(nomes[b])
    elif sexos[b] == 'H':
        idade_homens.append(idades[b])

print()
print(f'A media de idade eh de {sum(idades)/len(idades)}')
if idade_homens:
    print(f'O homem mais velho eh o {nomes[idades.index(max(idade_homens))]} e ele tem {max(idade_homens)} anos')
else:
    print('nenhum homem no grupo')
if mulheres_menores:
    print(f'As mulheres com menos de 20 anos sao: {', '.join(mulheres_menores)}')

