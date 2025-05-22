# 1. Desafio Matriz Rotacionada
"""
Dada uma matriz quadrada (lista de listas) de inteiros, escreva uma função
que rotacione a matriz 90° no sentido horário sem usar bibliotecas externas.
"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz_90 = []

for indice, linha in enumerate(matriz[::-1]):
    lista_linha = []
    for linha in matriz[::-1]:
        lista_linha.append(linha[indice])
    matriz_90.append(lista_linha)

for indice, linha in enumerate(matriz_90):
    print(matriz[indice], "--->", linha)
