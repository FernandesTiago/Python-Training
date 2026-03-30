# cadastro de pessoa sem menu ou input

cadastro = {'nome': 'tiago','email': 'castelantiago@gmail.com','idade': 23}
print(f"Nome: {cadastro['nome']} Email: {cadastro['email']} Idade: {cadastro['idade']}")

cadastro.update({'email': 'castelantiago2@gmail.com', 'idade': 24})
print(f"Nome: {cadastro['nome']} Email: {cadastro['email']} Idade: {cadastro['idade']}")

cadastro['telefone'] = '(11) 99938-0440'
if cadastro.get('telefone'):
    print(f"Nome: {cadastro['nome']} Email: {cadastro['email']} Idade: {cadastro['idade']} Telefone: {cadastro['telefone']}")

del cadastro['telefone']
print(f"Nome: {cadastro['nome']} Email: {cadastro['email']} Idade: {cadastro['idade']}", end=' ')
print(f"Telefone: {cadastro.get('telefone', 'N/A')}")
