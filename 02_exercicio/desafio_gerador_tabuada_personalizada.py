"""
Gerador de Tabuada Personalizada
Descrição: Peça um número e gere sua tabuada
(de 1 a N, onde N também é informado pelo usuário).
Desafio Extra: Permita que o usuário escolha se quer a tabuada de soma,
 subtração, multiplicação ou divisão.

Fundamentos: loops (for ou while), operadores, input, condicionais.
"""


def gerar_tabela(operacao, limite_final):
    if operacao == "1":
        for numero in range(1, (int(limite_final) + 1)):
            print(f"Tabela de Adição - Número {numero}")
            for posicao in range(1, 11):
                print(f"{numero} + {posicao} = {numero + posicao}")
    elif operacao == "2":
        for numero in range(1, (int(limite_final) + 1)):
            print(f"Tabela de Subtração - Número {numero}")
            for posicao in range(1, 11):
                print(f"{numero} - {posicao} = {numero - posicao}")
    elif operacao == "3":
        for numero in range(1, (int(limite_final) + 1)):
            print(f"Tabela de Divisão - Número {numero}")
            for posicao in range(1, 11):
                print(f"{numero} / {posicao} = {numero / posicao}")
    elif operacao == "4":
        for numero in range(1, (int(limite_final) + 1)):
            print(f"Tabela de Multiplicação - Número {numero}")
            for posicao in range(1, 11):
                print(f"{numero} * {posicao} = {numero * posicao}")
    else:
        print("Operação inválida!")


if __name__ == "__main__":
    print("Gerador de Tabuáda!")
    limite_final = input("Digite o último número da tabuada:")
    operacao = input("""Digite a Operação da tabuada desejada:
                    1 - Adição
                    2 - Subtração
                    3 - Divisão
                    4 - Multiplicação
                     """)
    gerar_tabela(operacao, limite_final)
