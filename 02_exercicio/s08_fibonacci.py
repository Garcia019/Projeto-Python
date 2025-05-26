# Sequência de Fibonacci

# 0, 1, 1, 2, 3, 5, 8, 13, 21
# (próximo número é a soma dos dois últimos números)
def fibonacci(quantidade_numeros=20):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if quantidade_numeros == len(resultado):
            break
    return resultado


if __name__ == "__main__":
    for fib in fibonacci():
        print(fib, end=", ")
