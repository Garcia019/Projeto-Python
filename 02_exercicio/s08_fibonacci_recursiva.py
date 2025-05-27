# Sequência de Fibonacci Recursiva - v2.0

# 0, 1, 1, 2, 3, 5, 8, 13, 21
# (próximo número é a soma dos dois últimos números)


def fibonacci(resultado=(0, 1), quantidade_numeros=20):
    return resultado if len(resultado) == quantidade_numeros else \
        fibonacci((resultado + (sum(resultado[-2:]), )), quantidade_numeros)


if __name__ == "__main__":
    for fib in fibonacci():
        print(fib, end=", ")
