"""
Sistema de Cadastro Simples
Descrição: Crie um sistema onde o usuário pode:

Cadastrar pessoas com nome, idade e gênero.

Ver a quantidade total de cadastros.

Ver a média de idade.

Listar quem tem mais de 18 anos.

Fundamentos: listas, dicionários, while, if/elif/else, for.
"""

cadastros = []


def cadastro_pessoa(cadastros):
    pessoa = {}
    while True:
        nome = input("Digite o nome da Pessoa: ")
        confirmar_nome = int(input(f"""\nDeseja confirma o nome {nome}:\n
1 - Sim;
2 - Não;\n
"""))
        if confirmar_nome == 1:
            pessoa["nome"] = nome.lower()
            break
        else:
            continue
    while True:
        idade = input("Digite a idade da pessoa: ")
        confirmar_idade = int(input(f"""Deseja confirma a idade {idade} anos:\n
1 - Sim;
2 - Não;\n
"""))
        if confirmar_idade != 1:
            continue
        elif idade.isnumeric() and int(idade) >= 0:
            pessoa["idade"] = int(idade)
            break
        else:
            print(f"Idade inválida: {idade}, digite uma idade válida!")
    while True:
        genero = input("""Para cadastrar o gênero,
Digite Masculino ou Feminino: """).lower()
        confirmar_genero = int(input(f"""Deseja confirma o gênero {genero}:\n
1 - Sim;
2 - Não;\n
"""))
        if confirmar_genero != 1:
            continue
        elif genero == "masculino" or genero == "feminino":
            pessoa["genero"] = genero
            break
        else:
            print(f"Gênero inválido: {genero}, digite um gênero válido!")
    cadastros.append(pessoa)


def quantidade_cadastro(cadastros):
    return len(cadastros)


def maiores_idade(cadastros):
    lista_maiores_idade = []
    for pessoa in cadastros:
        if pessoa["idade"] >= 18:
            lista_maiores_idade.append(pessoa)
    return lista_maiores_idade


def media_idade(cadastros):
    soma_idades = 0
    for pessoa in cadastros:
        soma_idades += pessoa["idade"]
    return (soma_idades/len(cadastros)) if soma_idades != 0 else 0


if __name__ == "__main__":
    while True:
        print("\nBem-Vindo ao Menu Cadastro Simples!")
        opcao = (input("""
1 - Realizar novo cadastro.
2 - Quantidade total de cadastros.
3 - Média de idade dos cadastros.
4 - Listagem dos maiores de 18 anos.
5 - Sair do programa.\n
Digite a opção desejada: """))
        if not opcao.isnumeric():
            print("Digite apenas números nas opções do menu.")
            continue
        match int(opcao):
            case 1:
                print("\nIniciado Cadastro de Pessoa.\n")
                cadastro_pessoa(cadastros)
            case 2:
                print(f"""O cadastro simples possui:\n
{quantidade_cadastro(cadastros)} cadastros.\n""")
            case 3:
                print(f"""A média de idades entre os cadastrados é:\n
{media_idade(cadastros)} anos.\n""")
            case 4:
                print("Lista Maiores de 18 Anos:\n")
                for pessoa in maiores_idade(cadastros):
                    print(f"""
Nome: {pessoa["nome"].upper()}, Idade: {pessoa["idade"]} anos.
""")
            case 5:
                print("Saindo do programa até logo.")
                break
            case _:
                print("\nOpção inválida!")
