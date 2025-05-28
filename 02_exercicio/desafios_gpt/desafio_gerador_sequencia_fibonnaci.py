"""
Gerador de Sequência de Fibonacci
Descrição: Peça um número n e gere os n primeiros
termos da sequência de Fibonacci.

Desafio Extra: Faça com for e depois com while como prática.

Fundamentos: laços, operadores, listas, lógica.

"""


def fibonacci_recursiva(resultado=(0, 1), quantidade_numeros=20):
    return resultado if len(resultado) == quantidade_numeros else \
        fibonacci_recursiva(
            (resultado + (sum(resultado[-2:]),)), quantidade_numeros)


def fibonacci(quantidade_numeros=20):
    resultado = [0, 1]
    for _ in range(quantidade_numeros-2):
        # _ é comumente utilizado na comunidade de python '
        # como varável não utilizada durante a utilização do for
        resultado.append(sum(resultado[-2:]))
    return resultado


def fibonacci_while(quantidade_numeros=20):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade_numeros:
            return resultado


if __name__ == "__main__":
    for fib in fibonacci(25):
        print(fib, end=", ")
    print("")
    for fib in fibonacci_recursiva(quantidade_numeros=25):
        print(fib, end="* ")
    print("")
    for fib in fibonacci_while(25):
        print(fib, end="& ")
    print("")
