"""
Analisador de Lista Numérica
Descrição: Peça ao usuário uma lista de números separados por vírgula e:

Mostre o maior e o menor valor.

Calcule a média.

Mostre quantos números são pares e quantos são ímpares.

Fundamentos: string, split, listas, for, if.
"""


def maior_valor_lista(lista):
    maior_valor = lista[0]
    for numero in lista:
        if numero > maior_valor:
            maior_valor = numero
    return maior_valor


def menor_valor_lista(lista):
    menor_valor = lista[0]
    for numero in lista:
        if numero < menor_valor:
            menor_valor = numero
    return menor_valor


def media_lista(lista):
    return sum(lista) / len(lista)


def somatorio_pares(lista):
    quantidade_par = 0
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            quantidade_par += 1
            pares.append(numero)
    return quantidade_par, pares


def somatorio_impares(lista):
    quantidade_impares = 0
    impares = []
    for numero in lista:
        if numero % 2 != 0:
            quantidade_impares += 1
            impares.append(numero)
    return quantidade_impares, impares


if __name__ == "__main__":
    while True:
        print("\nBem-Vindo ao Analisador de Lista Numérica!\n")
        lista_natural = input("Digite uma lista com números:").split(", ")
        lista_final = []
        for numero in lista_natural:
            if not numero.replace("-", "").isnumeric():
                print("Formato de lista ou Número Inválido!")
                break
            lista_final.append(int(numero))
        else:
            break
    while True:
        print(f"\nSua lista é {lista_final}")
        opcao = (input("""
1 - Mostrar Maior Valor.
2 - Mostrar Menor Valor.
3 - Mostrar Média.
4 - Mostrar Quantidade de Números Pares.
5 - Mostrar Quantidade de Números Ímpares.
6 - Sair do Menu Opções.\n
Digite a opção desejada: """))
        if not opcao.isnumeric():
            print("Digite apenas números nas opções do menu.")
            continue
        match int(opcao):
            case 1:
                print(f"""
O maior valor da lista é o número {maior_valor_lista(lista_final)}!
""")
            case 2:
                print(f"""
O menor valor da lista é o número {menor_valor_lista(lista_final)}!
""")
            case 3:
                print(f"""
A média dos números da lista é: {media_lista(lista_final)}!
""")
            case 4:
                print(f"""

A quantidade total de números pares é

{somatorio_pares(lista_final)[0]} !
Sendo eles {somatorio_pares(lista_final)[1]} !
""")
            case 5:
                print(f"""
A quantidade total de números ímpares é

{somatorio_impares(lista_final)[0]} !
Sendo eles {somatorio_impares(lista_final)[1]} !
""")
            case 6:
                print("\nSaindo do menu opções!")
                break
            case _:
                print("\nOpção inválida!")
