# agenda de contatos
# adicionado a funcao de excluir contatos


nomes = []
numeros = []

while True:
    print('\n--- Agenda de contatos ---')
    print('''
[1] Adicionar contato
[2] Buscar contato
[3] Abrir agenda
[4] Excluir contato
[5] Sair
''')
    while True:
        try:
            acao = int(input('Oque deseja fazer? '))
            if 1 <= acao <= 5:
                break
            else:
                continue
        except ValueError:
            print('Digite um valor de 1 a 5')
    if acao == 1:
        while True:
            print(f'\n--- adicionar contato {len(nomes)+1} ---\n')
            nome = input('Qual nome deseja salvar? ').strip().title()
            if nome.replace(' ','').isalpha():
                nomes.append(nome)
                break
            else:
                print('\nNome invalido\n')
        while True:
            numero = input('Qual o numero de telefone? (13 digitos): ').strip()
            if numero.isdigit() and len(numero) == 13:
                numero = list(numero)
                numero.insert(0,'+')
                numero.insert(3,' ')
                numero.insert(4,'(')
                numero.insert(7,')')
                numero.insert(8,' ')
                numero.insert(14,'-')
                numero = ''.join(numero)
                numeros.append(numero)
                print(f'\nContato {nome} adicionado com numero {numero}!\n')
                break
            else:
                print('\nDigite o codigo de regiao ddd e numero tudo junto!\n')
    elif acao == 2:
        if len(nomes) > 0:
            parar = False
            while not parar:
                buscar = input('\nQual nome deseja buscar? ').strip().title()
                if buscar.replace(' ','').isalpha():
                    for b in range(len(nomes)):
                        if buscar in nomes[b]:
                            print(f'''
{nomes[b]}
{numeros[b]}''')
                            parar = True
                    else:
                        if not parar:
                            print('Nome nao encontrado')
                            while True:
                                continuar = input('Deseja tentar denovo? (S/N) ').strip().upper()
                                if continuar == 'S' or continuar == 'N':
                                    if continuar == 'S':
                                        break
                                    else:
                                        parar = True
                                        break
                                else:
                                    print('Digite "S" ou "N"')
                else:
                    print('\nDigite uma nome valido')
        else:
            print('\nLista de contatos vazia')
    elif acao == 3:
        if len(nomes) > 0:
            for b in range(len(nomes)):
                print(f'''
{nomes[b]}
{numeros[b]}''')
        else:
            print('\nLista de contatos vazia')      
    elif acao == 4:
        if len(nomes) > 0:
            parar = False
            while not parar:
                indices_encontrados = []
                buscar = input('\nQue contato deseja excluir? ').strip().title()
                if buscar.replace(' ','').isalpha():
                    for b in range(len(nomes)):
                        if buscar in nomes[b]:
                            indices_encontrados.append(b)
                            print(f'''
/ [{len(indices_encontrados)}]
/ {nomes[b]}
/ {numeros[b]}''')
                    if len(indices_encontrados) > 1:
                        while not parar:
                            try:
                                escolha = int(input(f'\nQual contato deseja excluir? (1 a {len(indices_encontrados)}) '))
                                if 1<= escolha <= len(indices_encontrados):
                                    indice_real = indices_encontrados[escolha - 1]
                                    print(f'''
{nomes[indice_real]}
{numeros[indice_real]}
''')
                                    while not parar:
                                        excluir = input('\nTem certeza que dejesa excluir esse contato? (S/N) ').strip().upper()
                                        if excluir == 'S' or excluir == 'N':
                                            if excluir == 'S':
                                                nomes.pop(indice_real)
                                                numeros.pop(indice_real)
                                                print('\nNome excluido')
                                                parar = True
                                            else:
                                                print('\nNome não excluido')
                                                parar = True
                                        else:
                                            print('Digite "S" ou "N"')    
                                        break
                            except ValueError:
                                print('Digite um valor valido')
                    elif len(indices_encontrados) == 1:
                        while True:
                            excluir = input('\nTem certeza que dejesa excluir esse contato? (S/N) ').strip().upper()
                            if excluir == 'S' or excluir == 'N':
                                if excluir == 'S':
                                    indice_real = len(indices_encontrados) - 1
                                    nomes.pop(indice_real)
                                    numeros.pop(indice_real)
                                    print('\nNome excluido')
                                    parar = True
                                    break
                                else:
                                    print('\nNome não excluido')
                                    parar = True
                                    break
                            else:
                                print('Digite "S" ou "N"')
                    else:
                        if not parar:
                            print('Nome nao encontrado')
                            while True:
                                continuar = input('Deseja tentar denovo? (S/N) ').strip().upper()
                                if continuar == 'S' or continuar == 'N':
                                    if continuar == 'S':
                                        break
                                    else:
                                        parar = True
                                        break
                                else:
                                    print('Digite "S" ou "N"')
                else:
                    print('Digite um nome valido')
        else:
            print('\nLista de contatos vazia')
    else:
        print('\nObrigado Por usar usar a agenda!!\n')
        break