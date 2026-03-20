# agenda de contatos

nomes = []
numeros = []

while True:
    print('\n--- Agenda de contatos ---')
    print('''
[1] Adicionar contato
[2] Buscar contato
[3] Abrir agenda
[4] Sair
''')
    while True:
        try:
            acao = int(input('Oque deseja fazer? '))
            if 1 <= acao <= 4:
                break
            else:
                continue
        except ValueError:
            print('Digite um valor de 1 a 4')
    if acao == 1:
        while True:
            print(f'\n--- adicionar contato {len(nomes)+1} ---\n')
            nome = input('Qual nome deseja salvar? ').strip().title()
            if nome.replace(' ','').isalpha():
                nomes.append(nome)
                break
            else:
                print('\nNome invalido\n')
                continue
        while True:
            numero = input('Qual o numero de telefone? (13 digitos): ').strip()
            if numero.isdigit and len(numero) == 13:
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
            while parar == False:
                buscar = input('\nQual nome deseja buscar? ').strip().title()
                for b in range(len(nomes)):
                    if buscar in nomes[b]:
                        print(f'''
        {nomes[b]}
        {numeros[b]}''')
                        parar = True
                else:
                    if parar == False:
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
            print('Lista de contatos vazia')
    elif acao == 3:
        if len(nomes) > 0:
            for b in range(len(nomes)):
                print(f'''
{nomes[b]}
{numeros[b]}''')
        else:
            print('Lista de contatos vazia')                        
    else:
        print('\n Obrigado Por usar usar a agenda!!')
        break