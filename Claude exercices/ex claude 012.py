# casdastro de alunos def

def cadastrar_aluno(nome, notas):
    return {'nome': nome, 'notas': notas}
def media(notas):
    return sum(notas)/len(notas)
def situacao(media_real):
    if media_real <6:
        return 'reprovado'
    else:
        return 'aprovado'
def printar(lista_alunos,lista_aprovados):
    for aluno in lista_alunos:
        nome = aluno['nome']
        notas = aluno['notas']
        media_real = media(notas)
        print(f'''Aluno: {nome}
Media: {media_real:.2f}
Situacao: {situacao(media_real)}
''')
    print('Alunos aprovados: ', end='')
    for aprovado in lista_aprovados:
        print(aprovado['nome'], end=' ')

def filtrar_aprovados(lista_alunos):
    alunos_aprovados = []
    for aluno in lista_alunos:
        if media(aluno['notas']) >= 6:
            alunos_aprovados.append(aluno)
    return alunos_aprovados


aluno1 = cadastrar_aluno('Tiago', [10,5,10,6])
aluno2 = cadastrar_aluno('Mari', [7,2,5,9])
aluno3 = cadastrar_aluno('Juliana', [9,7,8,5])

alunos = [aluno1,aluno2,aluno3]
aprovados = filtrar_aprovados(alunos)

printar(alunos,aprovados)
