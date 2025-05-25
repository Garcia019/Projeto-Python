"""
Caixa Eletrônico
Descrição: Simule um caixa eletrônico que:

Recebe um valor de saque.

Informa quantas cédulas de cada valor devem ser entregues
(R$100, R$50, R$20, R$10, R$5, R$2, R$1).

Desafio: Resolver com o menor número de cédulas.

Fundamentos: while, operadores matemáticos, divisão inteira, dicionário/lista.
"""


def saque_caixa_eletronico(valor):
    notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    for nota in notas.keys():
        while valor >= nota:
            valor -= nota
            notas[nota] += 1
        if valor == 0:
            break
    return notas


if __name__ == "__main__":
    valor_saque = int(input("Digite um valor inteiro para o saque:"))
    for nota, numero_notas in saque_caixa_eletronico(valor_saque).items():
        if numero_notas == 0:
            continue
        print(f"Notas de {nota} : {numero_notas}")
