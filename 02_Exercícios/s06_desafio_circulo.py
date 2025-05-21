# VERSÃO ÁREA DA CIRCUNFERÊNCIA V14.0
# Utilizar o prefixo python antes de executar pelo navegador
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = "\033[091m"
    NORMAL = "\033[0m"


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {sys.argv[0][2:]} <raio>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO +
              "O raio informado deve ser no formato numérico" +
              TerminalColor.NORMAL)
        # NESSE PRINT É NECESSÁRIO ALTERAR A COR E RETORNAR
        sys.exit(errno.EINVAL)
    raio = sys.argv[1]
    area = circulo(raio)
    print(f"Á área da circunferência é de {area:.2f}")
