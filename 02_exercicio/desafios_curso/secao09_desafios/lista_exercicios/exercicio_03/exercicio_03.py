"""
Compactador de Arquivo

Leia um arquivo .txt linha por linha e
escreva outro arquivo com as palavras compactadas:

Exemplo: "banana" → "b2a2n2", "abacate" → "a2b1c1t1e1".

Use dict comprehension para contar letras + manipulação de arquivos.
"""


def contar_letras(arquivo):
    with open(arquivo, "r", newline='', encoding='utf-8') as palavras:
        with open("saida.txt", "w", newline='', encoding='utf-8') as saida:
            palavras = [palavra.strip() for palavra in palavras]
            for palavra in palavras:
                palavra_compacta = ""
                for caractere in palavra:
                    if caractere not in palavra_compacta:
                        palavra_compacta = palavra_compacta + \
                                            f"{caractere} \
                                            {palavra.count(caractere)}"
                print(palavra_compacta, file=saida)


if __name__ == "__main__":
    contar_letras("entrada.txt")
