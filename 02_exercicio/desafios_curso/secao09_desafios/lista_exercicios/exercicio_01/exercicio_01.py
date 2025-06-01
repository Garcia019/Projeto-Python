"""
Analisador de Vendas CSV com Generator

Crie um gerador que leia um arquivo .csv com colunas:
produto, quantidade, preço_unitário.

O gerador deve calcular e retornar o faturamento total
linha por linha, sem carregar tudo em memória).

Use o módulo csv + generator.
"""

import csv


def faturamento(arquivo="produtos.csv"):
    with open(arquivo, "r") as produtos:
        produtos_linha = (produto for produto in csv.reader(produtos))
        next(produtos_linha)
        for dados in produtos_linha:
            print(f"""
Faturamento da venda de {dados[0]}, foi de {float(dados[2]) * float(dados[1])}
    """)


if __name__ == "__main__":
    faturamento("produtos_exercicio_01.csv")
