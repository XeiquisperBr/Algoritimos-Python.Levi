contatos = (
    ('Levi', '9999-9999'),
    ('Davi', '8888-8888'),
    ('Lucielma', '7777-7777')
)

# Acessando uma informação da tupla
for nome, telefone in contatos:
    if nome == 'Levi':
        print(f'Telefone Levi: {telefone}')