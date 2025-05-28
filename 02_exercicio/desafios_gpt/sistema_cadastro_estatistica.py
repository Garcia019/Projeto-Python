"""
Desafio: Sistema de Gestão de Pessoas (SGP)

Objetivo:
Construir um programa interativo via terminal que simule o sistema de cadastro
de uma academia.
O sistema deve registrar informações básicas dos usuários e fornecer
estatísticas sobre os dados coletados.

Regras do sistema:

1. O sistema deve exibir um menu com opções numeradas de 1 a 10.
2. A opção 1 deve permitir o cadastro de uma nova pessoa, pedindo:
   - Nome
   - Idade
   - Peso (kg)
   - Altura (m)
   - Gênero (M/F)
   - Está matriculado no plano de musculação? (S/N)
3. Os dados de cada pessoa devem ser armazenados em um dicionário.
   Todos os cadastros devem ser salvos em uma lista chamada 'cadastros'.

4. As demais opções do menu devem:
   2 → Mostrar o número total de pessoas cadastradas.
   3 → Mostrar a quantidade de pessoas do gênero masculino e feminino.
   4 → Mostrar quantas pessoas estão matriculadas no plano de musculação.
   5 → Calcular e exibir a média de idade dos cadastrados.
   6 → Calcular e exibir a média de IMC (peso / altura²) dos cadastrados.
   7 → Exibir o nome e IMC da pessoa com o maior IMC.
   8 → Exibir o nome e IMC da pessoa com o menor IMC.
   9 → Permitir buscar um cadastro pelo nome e exibir os dados encontrados.
  10 → Encerrar o programa.

Regras adicionais:
- Deve haver validação para evitar divisões por zero (ex: lista vazia).
- A exibição de valores como IMC deve ser formatada com 2 casas decimais.
- O sistema deve aceitar nomes repetidos, mas mostrar todos os registros
correspondentes ao buscar.
- O sistema deve continuar rodando até que o usuário selecione a opção 10.

Conteúdo coberto: input, listas, dicionários, funções básicas, condicionais,
laços, lógica e exibição.
"""

cadastros = []
while (True):
    print("SGP - Sistema de Gestão de Pessoas")
    print(
        """
        1. Cadastrar Pessoa.
        2. Número total de pessoas cadastradas.
        3. Quantas pessoas são do gênero masculino e feminino.
        4. Quantos estão matriculados no plano de musculação.
        5. A média de idade dos cadastrados.
        6. A média de IMC dos cadastrados (IMC = peso / altura²).
        7. Nome da pessoa com maior IMC.
        8. Nome da pessoa com menor IMC.
        9. Buscar Cadastro.
        10. Encerrar SGP.
        """
    )
    menu = int(input("Selecione a opção do sistema:"))
    if menu == 1:
        pessoa = {}
        pessoa["nome"] = input("Digite o nome da Pessoa:").lower()
        pessoa["idade"] = int(input(f"Digite a idade da {pessoa['nome']}:"))
        pessoa["peso"] = float(input(f"Digite o peso da {pessoa['nome']}:"))
        pessoa["altura"] = float(input(
            f"Digite a altura da {pessoa['nome']}:"))
        pessoa["genero"] = input(
            f"Digite o gênero da {pessoa['nome']} M ou F: ").upper()
        if input(f"""A {pessoa['nome']}
                 está matriculada no plano de musculação S OU N:""") == "S":
            pessoa["plano"] = True
        else:
            pessoa["plano"] = False
        cadastros.append(pessoa)

    elif menu == 2:
        print(f"O total de pessoas cadastradas é de {len(cadastros)}")
    elif menu == 3:
        contagem_homens = 0
        contagem_mulheres = 0
        for individuo in cadastros:
            if individuo["genero"] == "M":
                contagem_homens += 1
            else:
                contagem_mulheres += 1
        print(f"""Cadastros nesse software possuem {contagem_homens}
              Homem(ns) e {contagem_mulheres} Mulher(ss).""")
    elif menu == 4:
        numero_pessoas_matriculadas = 0
        for individuo in cadastros:
            if individuo["plano"]:
                numero_pessoas_matriculadas += 1
        print(f"""Atualmente há {numero_pessoas_matriculadas}
              pessoas matriculadas no plano de musculação.""")
    elif menu == 5:
        if len(cadastros) == 0:
            print("Lista de Cadastro Vazia")
        else:
            somatorio_idades = 0
            for individuo in cadastros:
                somatorio_idades += individuo["idade"]
            print(f"""A média de idade das pessoas
                  cadastradas é de {somatorio_idades/len(cadastros)}.""")
    elif menu == 6:
        if len(cadastros) == 0:
            print("Lista de Cadastro Vazia")
        else:
            imc_total = 0
            for individuo in cadastros:
                imc_total += individuo["peso"] / individuo["altura"] ** 2
            print(f"""A média de IMC das pessoas
                  cadastradas é de {imc_total/len(cadastros)}.""")
    elif menu == 7:
        if len(cadastros) == 0:
            print("Lista de Cadastro Vazia")
        else:
            maior_imc = 0
            pessoa_maior_imc = ""
            for individuo in cadastros:
                if (individuo["peso"] / individuo["altura"] ** 2) > maior_imc:
                    maior_imc = individuo["peso"] / individuo["altura"] ** 2
                    pessoa_maior_imc = individuo["nome"]
            print(f"""A maior IMC do cadastro pertence ao
                  {pessoa_maior_imc} com o {maior_imc} de IMC!""")
    elif menu == 8:
        if len(cadastros) == 0:
            print("Lista de Cadastro Vazia")
        else:
            menor_imc = 200
            pessoa_menor_imc = ""
            for individuo in cadastros:
                if (individuo["peso"] / individuo["altura"] ** 2) < menor_imc:
                    menor_imc = individuo["peso"] / individuo["altura"] ** 2
                    pessoa_menor_imc = individuo["nome"]
            print(f"""O menor IMC do cadastro pertence ao
                  {pessoa_menor_imc} com o {menor_imc} de IMC!""")
    elif menu == 9:
        nome = input("""Digite o nome do usuário que deseja
                     buscar no banco de dados do cadastro:""").lower()
        print("Segue informações do cadastrado:")
        for individuo in cadastros:
            if individuo["nome"] == nome:
                for informacoes, dados in individuo.items():
                    print(informacoes.upper(), dados)
    elif menu == 10:
        break
