# Media de alunos usando dicionario

aluno1 = {'nome': 'Tiago','notas': [7, 8, 9]}
aluno2 = {'nome': 'Juliana','notas': [2, 4, 8]}
aluno3 = {'nome': 'Mari','notas': [9, 2, 6]}

alunos =[aluno1, aluno2, aluno3]

for aluno in alunos:
    print(f" A media de {aluno['nome']} eh {sum(aluno['notas']) / len(aluno['notas']):.2f}")