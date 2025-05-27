"""
Conversor de Temperaturas
Descrição: O usuário escolhe converter:

De Celsius para Fahrenheit

De Fahrenheit para Celsius

De Celsius para Kelvin

De Kelvin para Celsius

Fundamentos: input, if/elif/else, operadores, funções.
"""


def converter_celsius_fahrenheit(temperatura):
    return temperatura * 9/5 + 32


def converter_fahrenheit_celsius(temperatura):
    return (temperatura - 32) * 5/9


def converter_celsius_kelvin(temperatura):
    return (temperatura + 273.15)


def converter_kelvin_celsius(temperatura):
    return (temperatura - 273.15)


if __name__ == "__main__":
    while True:
        print("Bem vindo ao Conversor de Temperatura,")
        opcao = (input("""
1 - Conversor De Celsius Para Fahrenheit.
2 - Conversor De Fahrenheit para Celsius.
3 - Conversor De Celsius para Kelvin.
4 - Conversor De Kelvin para Celsius.
5 - Sair do Menu Opções.\n
Digite a opção desejada: """))
        if not opcao.isnumeric():
            print("Digite apenas números nas opções do menu.")
            continue
        temperatura = input("Digite o valor Temperatura que deseja converter:")
        if not temperatura.isnumeric():
            print("Digite apenas números na temperatura desejada.")
            continue
        else:
            temperatura = float(temperatura)
        match int(opcao):
            case 1:
                print(f"""
{temperatura}º Celsius são o equivalente a
{converter_celsius_fahrenheit(temperatura)} Fahrenheit!
""")
            case 2:
                print(f"""
{temperatura}º Fahrenheit são o equivalente a
{converter_fahrenheit_celsius(temperatura)} Celsius!
""")
            case 3:
                print(f"""
{temperatura}º Celsius são o equivalente a
{converter_celsius_kelvin(temperatura)} Kelvin!
""")
            case 4:
                print(f"""
{temperatura}º Kelvin são o equivalente a
{converter_kelvin_celsius(temperatura)} Celsius!
""")
            case 5:
                print("\nSaindo do menu opções!")
                break
            case _:
                print("\nOpção inválida!")
