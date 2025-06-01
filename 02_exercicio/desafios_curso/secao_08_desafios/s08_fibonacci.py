# Sequência de Fibonacci

# 0, 1, 1, 2, 3, 5, 8, 13, 21
# (próximo número é a soma dos dois últimos números)
def fibonacci(quantidade_numeros=20):
    resultado = [0, 1]
    for _ in range(quantidade_numeros-2):
        # _ é comumente utilizado na comunidade de python '
        # como varável não utilizada durante a utilização do for
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == "__main__":
    for fib in fibonacci():
        print(fib, end=", ")
