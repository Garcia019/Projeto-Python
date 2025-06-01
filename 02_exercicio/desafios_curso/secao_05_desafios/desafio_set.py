# Desafio Utilizando SET

PALAVRAS_PROIBIDAS = {"futebol", "religião", "política"}
frases = [
    "João gosta de futebol e política",
    "A praia foi divertida",
]

for indice, frase in enumerate(frases):
    frase_natural = frase.lower().split()
    conjunto_palavras = set(frase_natural)
    if len(PALAVRAS_PROIBIDAS.intersection(conjunto_palavras)) != 0:
        print(f"""Texto número {indice + 1} possui palavra probida:
{PALAVRAS_PROIBIDAS.intersection(conjunto_palavras)}""")
    else:
        print(f"Texto número {indice + 1} autorizado: {frase}!")
