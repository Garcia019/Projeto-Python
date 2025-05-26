"""
Jogo da Adivinhação Inteligente
Descrição: O computador escolhe um número aleatório entre 1 e 100.
O usuário tenta adivinhar.

Após cada tentativa, o programa diz se o número é maior ou menor.

Ao final, mostra quantas tentativas foram necessárias.

Fundamentos: while, if, import random, laços.
"""
from random import randint


def adivinhar_numero():
    numero_aleatorio = randint(1, 100)
    quantidade_tentativas = 0
    print("Bem-vindo ao Desafio - Acerte o número sorteado!\n")
    print("Sorteando número...\n")
    while True:
        tentativa = input("Digite sua tentativa entre 1 e 100: ")
        quantidade_tentativas += 1
        if not tentativa.isnumeric():
            print("\nDigite um número inteiro válido!\n")
            continue
        if int(tentativa) < numero_aleatorio:
            print(f"""
Sua tentativa {tentativa} é menor que o número sorteado!
""")
        elif int(tentativa) > numero_aleatorio:
            print(f"""
Sua tentativa {tentativa} é maior que o número sorteado!
""")
        elif int(tentativa) == numero_aleatorio:
            print(f"\nParabéns!! Você acertou o número sorteado {tentativa}")
            print(f"\nForam necessárias {quantidade_tentativas} tentativas!\n")
            break


if __name__ == "__main__":
    adivinhar_numero()
