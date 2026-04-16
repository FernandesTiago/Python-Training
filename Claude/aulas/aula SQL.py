#learning SQL

import sqlite3

conexao = sqlite3.connect('funcionarios.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        salario INTEGER
    )
''')
#cursor.execute('INSERT INTO funcionarios (nome, salario) VALUES (?, ?)', ('Tiago', 2500))
#cursor.execute('INSERT INTO funcionarios (nome, salario) VALUES (?,?)', ('Juliana', 3000))

#cursor.execute('UPDATE funcionarios SET salario = 5000 WHERE id = 1')

#cursor.execute('DELETE FROM funcionarios WHERE id = 1')

cursor.execute('SELECT * FROM funcionarios')
lista = cursor.fetchall()

for item in lista:
    print(f'ID: {item[0]} | Nome: {item[1]} | Salario: {item[2]}')


conexao.commit()
conexao.close()