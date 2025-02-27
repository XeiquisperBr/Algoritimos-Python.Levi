linha = '-' * 63
print(linha)
ano = int(input("Digite o ano para saber se ele é ou não bissexto."))
print(linha)

if ano %4 == 0:
    print(f"O ano de {ano} é bissexto.")
    print(linha)
    
else:
    print(f"O ano de {ano} não é bissexto.")
    print(linha)