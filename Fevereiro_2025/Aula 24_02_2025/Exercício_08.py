def gerar_relatorio_financeiro(transacoes):
    total = sum([transacao["valor"] for transacao in transacoes])
    return total
# Exemplo de uso
transacoes = [
    {"data": "2025-02-01", "valor": 1000},
    {"data": "2025-02-10", "valor": 500},
    {"data": "2025-02-15", "valor": 200}
]
total_vendas = gerar_relatorio_financeiro(transacoes)
print(f"Total de vendas: R${total_vendas:.2f}") # Total de vendas: R$1700.00