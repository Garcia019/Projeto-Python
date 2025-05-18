nomes_participantes = ["Matheus", "Taiane", "Roberta", "Joao", "Maria", "Roberto"]
votos_participantes = ["Maria votou em Joao",
    "Joao votou em Taiane",
    "Taiane votou em Joao",
    "Matheus votou em Maria",
    "Roberta votou em Maria",
    "Roberto votou em Matheus",
    "Maria votou em Joao",
    "Joao votou em Joao",
    "Matheus votou em Maria",
    "Roberto votou em Maria",
    "Roberta votou em Joao"]

votos_validos = []
votos_invalidos = []
votos_processados = {}
mais_negativo = 0
eliminados = []
menor_posicao_voto = 100
participantes_recompensados = []
minimo_voto = -10

for participantes in nomes_participantes:
    votos_processados[participantes] = [0, "NAO FOI VOTADO"]

for indice, votos in enumerate(votos_participantes):
    voto = votos.split(" ")
    voto = [voto[0], voto[-1]]
    if voto[0] != voto[-1] and votos_validos.count([voto[0], voto[-1]]) == 0:
        votos_validos.append(voto)
        votos_processados[(voto[-1])][0] -= 1
        votos_processados[(voto[-1])][1] = indice
    else:
        votos_invalidos.append(voto)

for voto in votos_processados.keys():
    if votos_processados[voto][0] < mais_negativo:
        mais_negativo = votos_processados[voto][0]

for nome, votos in votos_processados.items():
    if votos[0] == mais_negativo:
        eliminados.append([f"{nome}", votos])
    if votos[0] > minimo_voto:
        minimo_voto = votos[0]

print("Tabela de votos por participante:\n")
for participante, voto in votos_processados.items():
    print(f"Participante {participante} teve {-voto[0]} voto(s)!")
    if voto[0] == minimo_voto:
        participantes_recompensados.append(participante)

print("\nO(s) participante(s) que foi/foram recompensado(s) por ter/terem menos votos no programa foi/foram:\n")
for participante in participantes_recompensados:
    print(participante)

if len(eliminados) == 1:
    print(f"O participante eliminado foi o(a) {eliminados[0][0]} com {-eliminados[0][1][0]} votos!")
else:
    print("\nVamos para o empate entre...\n")
    for eliminado in eliminados:
        print(eliminado[0], f"{-eliminado[1][0]} voto(s)!")
    print("\nApós contabilizar as votações o participante eliminado foi... \n")
    for eliminado in eliminados:
        if eliminado[1][1] < menor_posicao_voto:
            menor_posicao_voto = eliminado[1][1]
    for eliminado in eliminados:
        if eliminado[1][1] == menor_posicao_voto:
            print(f"{eliminado[0]} com {-eliminado[1][0]} votos e com o ultimo voto na {eliminado[1][1]} posicao!")
