# ler exibir mengem perguntar se quer escrever mais

def escrita(a):
    """Escrever no dados17.txt — 'a' para adicionar, 'w' para apagar e reescrever."""
    while True:
        continuar = input('Deseja escrever algo? (S/N) (D) para deletar: ').upper().strip()
        if continuar == 'N':
            print('Nenhum texto adicionado.')
            break
        elif continuar == 'S':
            texto = input('Digite seu texto: ')
            with open('dados17.txt', a) as arquivo:
                arquivo.write(texto + '\n')
            with open('dados17.txt', 'r') as arquivo:
                print('Texto adicionado!\n' + arquivo.read())
            break
        elif continuar == 'D':
            with open('dados17.txt', 'w'):
                pass
            print('Arquivo esvaziado.')
            break
        else:
            print('Digite S, N ou D.')

try:
    with open('dados17.txt', 'r') as arquivo:
        texto = arquivo.read()
    if texto:
        print(texto)
        escrita('a')
    else:
        print('Arquivo vazio.')
        escrita('w')
except FileNotFoundError:
    escrita('w')