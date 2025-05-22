# Desafio de Fundamento em Python - Lista Final
# 1 Analisador de Texto
# Descrição: Peça um Frase ao usuário. Conte:
# Quantas Palavras
# Quantas Vogais
# Quantas Consoantes
# E qual a palavra mais longa.
# Fundamentos: string, loops, listas, funções

def contar_palavras(frase):
    palavras = frase.split(" ")
    return len(palavras)


def contar_vogais(frase):
    quantidade_vogais = 0
    for letra in frase.lower():
        if letra == "a":
            quantidade_vogais += 1
        elif letra == "e":
            quantidade_vogais += 1
        elif letra == "i":
            quantidade_vogais += 1
        elif letra == "o" or letra == "u":
            quantidade_vogais += 1
    return quantidade_vogais


def contar_consoantes(frase):
    quantidade_consoantes = len(frase) - contar_vogais(frase)
    return quantidade_consoantes


def palavra_mais_longa(frase):
    palavras, maior_palavra, numero_letras = frase.split(" "), "", 0
    for palavra in palavras:
        if len(palavra) > numero_letras:
            maior_palavra = palavra
            numero_letras = len(palavra)
    return (maior_palavra, numero_letras)


if __name__ == "__main__":
    frase = input("Digite a frase escolhida:")
    print("Bem-vindo ao Analisador de Texto!")
    print(f"Na sua frase há {contar_palavras(frase)} palavra(s)!")
    print(f"Na sua frase há {contar_vogais(frase)} vogais!")
    print(f"Na sua frase há {contar_consoantes(frase)} consoantes!")
    print(f""" palavra mais longa da sua frase é {palavra_mais_longa(frase)[0]}
          com {palavra_mais_longa(frase)[1]} letras!""")
