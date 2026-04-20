#Crie um sistema de menu no terminal com as opções:

import sqlite3

# --------- ESTRUTURA DO BANCO DE DADOS ---------

class BancoDados:

    def __init__(self):
        self.conexao = sqlite3.connect('MenuFuncionarios.db')
        self.cursor = self.conexao.cursor()
        self.conexao.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        salario INTEGER
    )''')   
        
    def ler(self):
        self.cursor.execute('SELECT * FROM funcionarios')
        return self.cursor.fetchall()
    
    def buscar_id(self, id_buscado):
        self.cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id_buscado,))
        return self.cursor.fetchone()

    def salvar(self, novo_nome, novo_salario):
        self.cursor.execute('INSERT INTO funcionarios (nome, salario) VALUES (?,?)', (novo_nome, novo_salario))
        self.conexao.commit()

    def atualizar_nome(self, id_lista, novo_nome):
        self.cursor.execute('UPDATE funcionarios SET nome = ? WHERE id = ?', (novo_nome, id_lista))
        self.conexao.commit()

    def atualizar_salario(self, id_lista, novo_salario):
        self.cursor.execute('UPDATE funcionarios SET salario = ? WHERE id = ?', (novo_salario, id_lista))
        self.conexao.commit()

    def pegar_maior_id(self):
        self.cursor.execute('SELECT MAX(id) FROM funcionarios')
        resultado = self.cursor.fetchone()
        return resultado[0] if resultado[0] is not None else 0

    def deletar(self, id_para_deletar):
        self.cursor.execute('DELETE FROM funcionarios WHERE id = ?',(id_para_deletar,))
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.commit() 
        self.conexao.close()
        print("Conexão com o banco de dados encerrada.")

    def __del__(self):
        try:
            self.conexao.close()
        except:
            pass

# --------- ESTRUTURA DO MENU ---------

class Menu:

    def __init__(self):
        self.db = BancoDados()
        self.opcoes = {
            '1': self.listar,
            '2': self.adicionar,
            '3': self.atualizar,
            '4': self.excluir,
            '0': self.sair_sistema
        }

    def iniciar_menu(self):
        while  True:
            print('-='*16)
            print('[1] - Listar funcionários')
            print('[2] - Adicionar funcionário')
            print('[3] - Atualizar tabela')
            print('[4] - Deletar funcionário')
            print('[0] - Sair')
            print('-=' * 16)

            while True:
                escolha = input('> ').strip()

                if escolha in self.opcoes:
                    self.opcoes[escolha]()
                    break
                else:
                    print('Opção inválida, tente novamente!')

    def listar(self):
        maximo = self.db.pegar_maior_id()
        if maximo == 0:
            print('Lista vazia')
        else:    
            lista = self.db.ler()
            for item in lista:
                print(f'ID: {item[0]} | Nome: {item[1]} | Salario: {item[2]}')

    def adicionar(self):
        print('Que nome deseja salvar?')
        nome = input('> ')
        print('Qual o salario?')
        while True:
            try:
                salario = float(input('> '))
                break
            except ValueError:
                print('Valor invalido')
        self.db.salvar(nome, salario)
        print(f'Funcionario {nome} salvo com sucesso!')

    def atualizar(self):
        maior_id = self.db.pegar_maior_id()
        if maior_id == 0:
            print('Lista Vazia!')
        else:
            while True:
                print('Que funcionario deseja atualizar? (ID)')
                while True:
                    try:
                        fid = int(input('> '))
                        if fid > maior_id or fid <= 0:
                            print('ID invalido')
                        else:
                            break
                    except ValueError:
                        print('ID invalido')
                funcionario = self.db.buscar_id(fid)
                if not funcionario:
                    print('Funcionário não encontrado!')
                else:
                    print(f'ID: {funcionario[0]} | Nome: {funcionario[1]} | Salario: R$ {funcionario[2]}\n')
                    print('Oque deseja atualizar?')
                    print('[1] - Nome')
                    print('[2] - Salario')
                    print('[3] - Outra pessoa')
                    print('[0] - sair')     
                    escolha = input('> ')

                    if escolha == '1':
                        print('Qual o novo nome?')
                        nome = input('> ')
                        self.db.atualizar_nome(fid, nome)
                        return     
                    elif escolha == '2':
                        print('Qual o novo salario?')
                        while True:
                            try:
                                salario = float(input('> '))
                            except ValueError:
                                print('Valor invalido.')
                            else:
                                self.db.atualizar_salario(fid, salario)
                                return                           
                    elif escolha == '3':
                        continue
                    elif escolha == '0':
                        print('Acão cancelada.')
                        return
                    
    def excluir(self):
        id_maximo = self.db.pegar_maior_id()
        if id_maximo == 0:
            print('Lista vazia')
        else:
            while True:
                print('Que funcionario deseja excluir? (ID)')
                try:
                    eid = int(input('> '))
                    break
                except ValueError:
                    print('Valor invalido')
            if eid > id_maximo or eid <= 0:
                print('Valor invalido')
            else:
                funcionario = self.db.buscar_id(eid)
                if not funcionario:
                    print('Funcionário não encontrado!')
                else:
                    print(f'ID: {funcionario[0]} | Nome: {funcionario[1]} | Salario: R$ {funcionario[2]}\n')
                    print('Tem certeza que deseja excluir? (S/N)')
                    while True:
                        escolha = input('> ').title().strip()
                        if escolha == 'S':
                            print('Funcionario excluido!')
                            self.db.deletar(eid)
                            return
                        elif escolha == 'N':
                            print('Ação cancelada.')
                            return
                        else:
                            print('Valor invalido')

    def sair_sistema(self):
        print("Saindo e fechando banco...")
        self.db.fechar_conexao()
        exit()

if __name__ == "__main__":
    app = Menu()
    app.iniciar_menu()
