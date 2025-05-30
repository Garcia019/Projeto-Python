"""
Validador de Arquivo CSV com Expressões Condicionais

Escreva um código que leia um arquivo
CSV e identifique linhas com dados inválidos.

Critérios: colunas vazias, preço negativo, nomes com caracteres inválidos.

Utilize dict comprehension para mapear erros por coluna.
"""
"""
import csv


def dados_invalidos(arquivo="produtos.csv"):
    with open(arquivo, "r", newline='', encoding='utf-8') as dados:
        produtos = {}

"""
