linha = '-' * 63
lista_informacoes = ['Nome: Lucas',
                     'Idade: 32',
                     'Altura: 1.75',
                     'Cidade: Campinas',
                     'Estado: SP',
                     'Pais: Brasil']

print (lista_informacoes)
print (lista_informacoes[5])
#-------------------------------------------------------------------------------------------
print(linha + '\n')
mensagem_indice = 'O indice do produto é:'
mensagen_iten ='e o iten da lista é o:'
mensagem_quantidade = 'e quantidade do produto é:'

#lista de produtos e seus estoques

produtos = ['Caixa de som','Celular','Monitor','Mouse','Teclado']
estoque = [100, 200, 300, 400, 1000]

#encontrando o indice do produto teclado
indice_teclado = produtos.index('Teclado')

#exibindo as informaçoes do produto
print(f'\n{mensagem_indice}{indice_teclado}, {mensagen_iten} {produtos[indice_teclado]}, {mensagem_quantidade} {estoque[indice_teclado]}')
print(linha + '\n')
#-------------------------------------------------------------------------------------------

produto = input('Insira o nome de um equipamento eletrônico')
produtos = ['Caixa de som','Celular','Monitor','Mouse','Teclado']
estoque = [100, 200, 300, 400, 1000]

#verificando se o produto esta na lista

if produto in produtos:
    indice = produtos.index(produto)
    qtd_estoque = estoque[indice]
    print(f'A quantidade dp produto "{produto}"em estoque é de: {qtd_estoque} unidades.')
else:
    print(f'O produto informado "{produto}" não existe no estoque.')
    print(linha + '\n')
#-------------------------------------------------------------------------------------------
    