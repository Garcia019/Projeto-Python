# Conceitos Notas
# A         De 10.0 à 9.1
# A-        De 9,0 à 8.1
# B         De 8.0 à 7.1
# B-        De 7.0 à 6.1
# C         De 6.0 à 5.1
# C-        De 5.0 à 4.1
# D         De 4.0 à 3.1
# D-        De 3.0 à 2.1
# E         De 2.0 à 1.1
# E-        De 1.0 à 0.0

# Para notas maiores que 10 e menores que 0 será impresso "Nota Inválida"
import sys


def help():
    if len(sys.argv) < 2:
        print("É Necessário informar a nota!")
        print(f"Sintaxe: {sys.argv[0]} <nota>")
        sys.exit()
    try:
        float(sys.argv[1])
    except ValueError:
        print("A nota precisa ser passada em um valor numérico!")
        sys.exit()


def conceito_nota(nota):
    nota = float(nota)
    """
    Alterado a programação considerando que a função poderá
    ser importada e não convertido o valor externamente como
    necessário para fazer as comparações float()
    """
    if 9.1 <= nota <= 10.0:
        return "A"
    elif 8.1 <= nota < 9.1:
        return "A-"
    elif 7.1 <= nota < 8.1:
        return "B"
    elif 6.1 <= nota < 7.1:
        return "B-"
    elif 5.1 <= nota < 6.1:
        return "C"
    elif 4.1 <= nota < 5.1:
        return "C-"
    elif 3.1 <= nota < 4.1:
        return "D"
    elif 2.1 <= nota < 3.1:
        return "D-"
    elif 1.1 <= nota < 2.1:
        return "E"
    elif 0.0 <= nota < 1.1:
        return "E-"
    else:
        return "Nota Inválida!"


if __name__ == "__main__":
    help()
    print(f"Sua nota conceito é {conceito_nota(sys.argv[1])}!")
