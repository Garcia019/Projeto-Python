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

for participantes in nomes_participantes:
    votos_processados[participantes] = 0

for votos in votos_participantes:
    voto = votos.split(" ")
    voto = [voto[0], voto[-1]]
    if voto[0] != voto[-1] and votos_validos.count([voto[0], voto[-1]]) == 0:
        votos_validos.append(voto)
        votos_processados[(voto[-1])] -= 1
    else:
        votos_invalidos.append(voto)

menor_voto = 0
mais_votado = {}

for voto in votos_processados.keys():
    if votos_processados[voto] < menor_voto:
        mais_votado.clear()
        mais_votado[voto] = votos_processados[voto]

print(mais_votado)
print(votos_validos)
print(votos_processados)
