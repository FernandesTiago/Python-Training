# try except else

def ler_numero_do_arquivo(caminho):
    try:
        arquivo = open(caminho, 'r')
        try:
            numero = float(arquivo.readline())
        except ValueError:
            print('Conteudo nao eh um numero')
        else:
            return numero
        finally:
            arquivo.close()
    except FileNotFoundError:
        print('Arquivo nao encontrado')

ler = ler_numero_do_arquivo('dados20.txt')
if ler:
    print(ler)