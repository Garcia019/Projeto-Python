"""
Calculadora de IMC com Classificação
Descrição: Peça peso e altura, calcule o IMC e informe:

A classificação (baixo peso, normal, sobrepeso, obesidade, etc.).

Fundamentos: operadores matemáticos, if/elif/else.
"""


def lendo_dados_usuario():
    while True:
        nome = input("Digite seu nome: ")
        peso = input("Digite o seu peso para armazenar: ")
        altura = input("Digite sua altura para armazenar: ")
        try:
            float(peso)
        except ValueError:
            print("""
Digite um peso válido (inteiro ou decimal, positivo).
                  """)
            continue
        try:
            float(altura)
        except ValueError:
            print("""
Digite uma altura válida (inteiro ou decimal, positivo).
                  """)
            continue
        else:
            return {"nome": nome,
                    "peso": float(peso),
                    "altura": float(altura),
                    "imc": float(peso)/float(altura)**2}


def classificacao_imc(pessoa):
    if pessoa["imc"] >= 40:
        return pessoa["nome"], pessoa["imc"], "Obesidade Grau III"
    elif 35 <= pessoa["imc"] <= 39.9:
        return pessoa["nome"], pessoa["imc"], "Obesidade Grau II"
    elif 30 <= pessoa["imc"] <= 34.9:
        return pessoa["nome"], pessoa["imc"], "Obesidade Grau I"
    elif 25 <= pessoa["imc"] <= 29.9:
        return pessoa["nome"], pessoa["imc"], "Sobre Peso"
    elif 18.5 <= pessoa["imc"] <= 24.9:
        return pessoa["nome"], pessoa["imc"], "Peso Normal"
    elif pessoa["imc"] < 18.5:
        return pessoa["nome"], pessoa["imc"], "Baixo Peso"


if __name__ == "__main__":
    while True:
        print("Bem vindo ao Classificadora e Calculadora IMC,\n")
        pessoa = lendo_dados_usuario()
        print("""
Olá {} seu IMC é {} e você foi classificado no grupo {}!
""".format(*classificacao_imc(pessoa)))
