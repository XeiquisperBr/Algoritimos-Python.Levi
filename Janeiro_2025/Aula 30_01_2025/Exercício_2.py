#Tratamento de Erros com os métodos Try e except
try:
    #Tenta abrir o 'arquivo.txt'
    arquivo = open('arquivo.txt')
except FileNotFoundError as erro:
    #Se o arquivo não for encontrado, exibe uma mensagem de erro amigável
    print(f"O arquivo .TXT não foi encontrado no diretório de projetos. \n{erro}")

else:
    with open("arquivo.txt", "r") as file_object:
        texto = file_object.read()
        print(texto)