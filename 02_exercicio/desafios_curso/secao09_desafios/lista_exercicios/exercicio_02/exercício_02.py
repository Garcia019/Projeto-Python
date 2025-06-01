"""
Validador de Arquivo CSV com Expressões Condicionais

Escreva um código que leia um arquivo
CSV e identifique linhas com dados inválidos.

Critérios: colunas vazias, preço negativo, nomes com caracteres inválidos.

Utilize dict comprehension para mapear erros por coluna.
"""

import csv


def dados_invalidos(arquivo="produtos.csv"):
    with open(arquivo, "r", newline='', encoding='utf-8') as dados:
        produtos = csv.reader(dados)
        erros_produtos = []
        erros_quantidade = []
        erros_valor = []
        next(produtos)
        for indice,  dado_produto in enumerate(produtos, start=1):
            if not dado_produto[0].strip():
                erros_produtos.append(indice)
            # utilizar sempre que possível o try except para tratar problemas
            # como identificar números, inteiros, float, entre outros
            try:
                quantidade = int(dado_produto[1])
                if quantidade <= 0:
                    erros_quantidade.append(indice)
            except ValueError:
                erros_quantidade.append(indice)
            try:
                valor = float(dado_produto[2])
                if valor <= 0:
                    erros_valor.append(indice)
            except ValueError:
                erros_valor.append(indice)
    erros = {
        "produto": erros_produtos,
        "quantidade": erros_quantidade,
        "valor": erros_valor
    }
    erros_filtrados = {coluna: linhas for coluna,
                       linhas in erros.items() if linhas}
    return erros_filtrados


if __name__ == "__main__":
    print(dados_invalidos("produtos_exercicio_02.csv"))
