'''Desafio com pesquisas: '''

'''1º Crie uma lista contendo os números com os seguintes valores: [5, 2, 9, 1, 5, 6].
Ordene a lista em ordem crescente e imprima o resultado.'''
linha = '-' * 63

lista = [5, 2, 9, 1, 5, 6]
lista.sort()
print(lista)
print(linha)

#https://www.dio.me/articles/explorando-funcoes-em-python-sort

'''2º Com a lista de notas = [7, 8, 9, 7, 6, 8], conte quantas vezesa nota 7 aparece na lista 
e imprima o resultado'''

lista_de_notas = [7, 8, 9, 7, 6, 8]
quantidade = lista_de_notas.count(7)
print(f'R: O numéro 7 aparece {quantidade} vezes na lista.')
print(linha)

#https://awari.com.br/count-python-aprenda-a-utilizar-a-funcao-count-em-python/#:~:text=Utilizando%20a%20fun%C3%A7%C3%A3o%20count%20em%20Python,-Para%20utilizar%20a&text=Podemos%20fazer%20isso%20da%20seguinte,aparece%203%20vezes%20na%20lista%E2%80%9D.

'''3º Com a lista de materiais = ['papel', 'caneta', 'caderno', 'borracha'], verifique se 'lapiseira' está
presente na lista e imprima uma mensagem informandoo resultado.'''
lista_de_materiais = ['papel', 'caneta', 'caderno', 'borracha']
print('lapiseira' in lista_de_materiais)
print(linha)
    
'''4º Ao receber a lista de dias faça um Slicing, lista dias = ['domingo', 'segunda', 'terça', 'quarta',
'quinta', 'sexta', 'sabádo'], crie uma nova lista que contenha apenasos dias da semana de segunda a sexta. 
Imprima a nova lista'''
