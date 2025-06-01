# Definir a faixa etária do individuo com base na idade

def faixa_etaria(idade):
    if 0 <= idade < 18:
        return "Menor de idade"
    elif idade in range(18, 65):
        return "Adulto"
    elif idade in range(65, 100):
        return "Idoso"
    elif idade >= 100:
        return "Centenária"
    else:
        return "Idade inválida"


if __name__ == "__main__":
    for idade in (17, 35, 87, 113, -2, 64):
        print(f"{idade}: {faixa_etaria(idade)}!")
