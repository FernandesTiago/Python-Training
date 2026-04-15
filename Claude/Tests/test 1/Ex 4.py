# Crie uma função que recebe uma lista de dicionários de alunos
# (cada um com 'nome' e 'nota') e retorna apenas os aprovados
# (nota >= 6).
# Imprima os aprovados formatados com nome alinhado à esquerda
# em 15 caracteres e nota com 1 casa decimal.

# Teste com:
alunos = [
    {'nome': 'Ana', 'nota': 8.0},
    {'nome': 'Bruno', 'nota': 4.5},
    {'nome': 'Carla', 'nota': 6.0},
    {'nome': 'Diego', 'nota': 3.0},
    {'nome': 'Elena', 'nota': 9.5}
]

def alunos_aprovados(lista_alunos):
    """RECEBE UMA LISTA DE DICIONARIOS DE ALUNOS E RETORNA A LISTA DOS APROVADOS"""
    alunos_aprovados = []
    for aluno in alunos:
        if aluno['nota'] >= 6:
            alunos_aprovados.append(aluno)
    return alunos_aprovados

alunos_aprovados = alunos_aprovados(alunos)

print('Alunos aprovados:')
for i in range(0, len(alunos_aprovados)):
    print(f'Aluno: {alunos_aprovados[i]['nome']:<15} Nota: {alunos_aprovados[i]['nota']:.1f}')