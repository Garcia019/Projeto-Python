""""
Validador de Senha Forte
Descrição: O usuário deve digitar uma senha. Valide se ela possui:

Pelo menos 8 caracteres.

Pelo menos 1 letra maiúscula.

Pelo menos 1 número.

Pelo menos 1 caractere especial (!, @, #, $, etc.).

Fundamentos: string, if/elif/else, operadores, funções.
"""


def possui_letra_maiuscula(senha):
    for caractere in senha:
        if caractere.isupper():
            return True
    return False


def possui_numero(senha):
    for caractere in senha:
        if caractere.isnumeric():
            return True
    return False


def possui_caractere_especial(senha):
    caractere_especiais = set("!@#$%^&*()-_=+[]{}|<>?/~.")
    for caractere in senha:
        if caractere in caractere_especiais:
            return True
    return False


if __name__ == "__main__":
    while True:
        senha = input("Digite sua senha:")
        if (len(senha) >= 8 and possui_letra_maiuscula(senha) and
           possui_numero(senha) and possui_caractere_especial(senha)):
            print(f"Sua senha '{senha}' é válida!")
        else:
            print(f"""Sua senha '{senha}' é inválida!
                  \nAtenda aos requisitos abaixo:""")
            print("- Pelo menos 8 caracteres")
            print("- Pelo menos 1 letra MAIÚSCULA")
            print("- Pelo menos 1 NÚMERO")
            print("- Pelo menos 1 CARACTERE ESPECIAL (!@#$...)")
