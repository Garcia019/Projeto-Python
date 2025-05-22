# Desafio de Fundamento em Python - Lista Final
# 1 Analisador de Texto
# Descrição: Peça um Frase ao usuário. Conte:
# Quantas Palavras
# Quantas Vogais
# Quantas Consoantes
# E qual a palavra mais longa.
# Fundamentos: string, loops, listas, funções
import unicodedata


def remover_acentos(frase):
    frase_normalizado = unicodedata.normalize("NFD", frase)
    frase_sem_acentos = ''.join([caractere for caractere in frase_normalizado
                                 if not unicodedata.combining(caractere)])
    return frase_sem_acentos


def contar_palavras(frase):
    palavras = frase.split(" ")
    return len(palavras)


def contar_vogais(frase):
    vogais = "aeiou"
    quantidade_vogais = 0
    vogais_encontradas = ""
    for letra in frase:
        if remover_acentos(letra.lower()) in vogais:
            quantidade_vogais += 1
            vogais_encontradas = vogais_encontradas + f"{letra}, "
    return quantidade_vogais, vogais_encontradas


def contar_consoantes(frase):
    consoantes = "bcdfghjklmnpqrstvxwyz"
    quantidade_consoantes = 0
    consoantes_encontradas = ""
    for letra in frase:
        if letra.lower() in consoantes:
            quantidade_consoantes += 1
            consoantes_encontradas = consoantes_encontradas + f"{letra}, "
    return quantidade_consoantes, consoantes_encontradas


def palavra_mais_longa(frase):
    palavras, maior_palavra = frase.split(" "), ""
    for palavra in palavras:
        caractere_proibido = ".,!?:*-+_`~!@#$%^<>º&(){}[]|/;'"
        for caractere in caractere_proibido:
            palavra = palavra.replace(caractere, "")
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    return (maior_palavra, len(maior_palavra))


if __name__ == "__main__":
    frase = input("Digite a frase escolhida:")
    print("Bem-vindo ao Analisador de Texto!")
    print(f"Na sua frase há {contar_palavras(frase)} palavra(s)!")
    print(f"Na sua frase há {contar_vogais(frase)[1]} que são {contar_vogais(frase)[0]} vogais!")
    print(f"Na sua frase há {contar_consoantes(frase)[1]} que são {contar_consoantes(frase)[0]} consoantes!")
    print(f""" palavra mais longa da sua frase é {palavra_mais_longa(frase)[0]}
          com {palavra_mais_longa(frase)[1]} letras!""")
