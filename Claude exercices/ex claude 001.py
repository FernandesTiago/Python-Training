# 5 funcionarios, media salario, quem ganha mais que a media e qual o menor e maior salario

funcionarios = []
salarios = []

c = 0

while c < 5:
    print(f'\n--- Casdastro do {c+1} Funcionario ---')
    funcionario = input('\nQual o nome do funcionario? ').strip().title()
    if funcionario.replace(' ','').isalpha():
        funcionarios.append(funcionario)
    else:
        print('\nDigite um nome valido')
        continue
    try:
        salario = float(input('Qual o salario dele(a)? R$'))
        salarios.append(salario)
        c += 1
    except ValueError:
        print('\nDigite um valor valido\n')
print(f'A media do salario é de {sum(salarios)/c}')
print('Os funcionarios que ganham igual ou mais que a media sao: ', end='')
for b in range(len(salarios)):
    if salarios[b] >= sum(salarios)/c:
        print(funcionarios[b], end= ', ')
print(f'\nO maior salario é de R${max(salarios)}')
print(f'E o menor é de R${min(salarios)}')
