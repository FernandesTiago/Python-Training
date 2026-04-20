while True:
    try:
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
            print(numero)
            break
        else:
            print('\nDigite o codigo de regiao ddd e numero tudo junto!\n')
    except ValueError:
        print('\nDigite um valor valido\n')