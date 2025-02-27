#Adicioanando item a lista

# Lista de Celulares
adiciona_mobile = ['SAMSUNG S20', 'SAMSUNG A10', 'LG K10 PRO']
print('Modelos atuais da lista:', adiciona_mobile, '\n')

# Remove um modelo da lista
adiciona_mobile.remove('LG K10 PRO')

# Exibe a confirmação da adição
print('O celular', adiciona_mobile[-1], 'foi adicionado ao estoque com sucesso.')

'''Utilizado -1 para adicionar após o ultimo item da lista, porem poderia utilizar [3]'''

# Mostra a lista atualizada
print('A lista de produtos atualizada é:', adiciona_mobile)




modelo_removido = remove_mobile.pop(2)