def cadastrar_livro(titulo, autor, ano, disponivel):
    livro = {'titulo': titulo, 'autor': autor, 'ano': ano, 'disponivel': disponivel}
    return livro

def livros_disponiveis(acervo_livros):
    list_livros_disponiveis = []
    for livro in acervo_livros:
        if livro['disponivel']:
            list_livros_disponiveis.append(livro)
    return list_livros_disponiveis

def buscar_por_autor(acervo_livros, autor):
    livros_do_autor = []
    for livro in acervo_livros:
        if livro['autor'] == autor:
            livros_do_autor.append(livro)
    return livros_do_autor

def livro_mais_antigo(acervo_livros):
    livro_antigo = 10000
    dic_livro_antigo = 0
    for livro in acervo_livros:
        if livro['ano'] < livro_antigo:
            livro_antigo = livro['ano']
            dic_livro_antigo = livro
    return dic_livro_antigo

def resumo(acervo_livros):
    quantidade_disponivel = 0
    print()
    for livro in acervo_livros:
        disponivel = livro['disponivel']
        status = 'disponivel' if disponivel else 'indisponivel'
        print(f'Livro: {livro['titulo']:<20} Autor: {livro['autor']:20} Ano: {livro['ano']:^6} Disponibilidade: {status:<10}')
        if disponivel:
            quantidade_disponivel += 1
    print(f'\n{quantidade_disponivel} livro estao disponiveis')
    livro_antigo = livro_mais_antigo(acervo_livros)
    print(f'\nO mais antigo eh {livro_antigo['titulo']}')

acervo = [
    cadastrar_livro('Dom Casmurro', 'Machado de Assis', 1899, True),
    cadastrar_livro('O Cortico', 'Aluisio Azevedo', 1890, False),
    cadastrar_livro('Iracema', 'Jose de Alencar', 1865, True),
    cadastrar_livro('Memorias Postumas', 'Machado de Assis', 1881, False),
    cadastrar_livro('O Guarani', 'Jose de Alencar', 1857, True),
]

resumo(acervo)