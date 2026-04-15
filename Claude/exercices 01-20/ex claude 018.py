# lista de jogadores em arquivo .txt

try:
    with open('dados18.txt', 'r') as arquivo:
        lista = arquivo.read()
        if not lista:
            print('Lista de jogadores vazia')
        else:
            print(lista)
except FileNotFoundError:
    with open('dados18.txt', 'a'):
        pass
    print('Lista de jogadores vazia')

with open('dados18.txt', 'a') as arquivo:
    nome = input('Qual o nome que deseja adicionar? ').title().strip()
    if nome == 'D':
        with open('dados18.txt', 'w'):
            pass
        exit()
    else:
        while True:
            try:
                pontuacao = int(input('Qual a pontuacao dele(a): '))
                print(f'{nome}, {pontuacao} Foi adicionado!')
                arquivo.write(f'{nome}, {pontuacao}\n')
                break
            except ValueError:
                print('Digite um numero inteiro!')

with open('dados18.txt', 'r') as arquivo:
    lista_atualizada = arquivo.readlines()
    lista_ordenada = []
    for i in range(0,len(lista_atualizada)):
        jogador = lista_atualizada[i].split()
        jogador[0] = jogador[0].replace(',', '')
        jogador[1] = int(jogador[1])
        lista_ordenada.append(jogador)
    lista_ordenada = sorted(lista_ordenada, key=lambda x: x[1], reverse=True)
    for nomes in lista_ordenada:
        print(f'O jogador(a) {nomes[0]} Pontuou: {nomes[1]} pontos!!')
