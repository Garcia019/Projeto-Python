# IO - version_5.0

"""
Já podemos considerar que a função open()
tem dois parâmetros um deles é o nome do arquivo
que será aberto e o segundo parâmetro sera o
mode de execução do arquivo que você pode determinar
no exemplo abaixo vamos abrir o arquivo "pessoas.txt"
no modo de escrita utilizando o parâmetro "w"

Outro detalhe é sobre a utilização do parâmetro file
na função saída, que ao invés de fazer a impressão
no console faz diretamente na memoria saida, nesse
caso o arquivo pessoa.txt
"""
with open("pessoas.csv",) as arquivo:
    with open("pessoas.txt", "w") as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(",")
            print("Nome: {}, Idade: {}".format(*pessoa), file=saida)

if arquivo.closed:
    print("Arquivo já foi fechado por conta do bloco de execução with!")

if saida.closed:
    print("Arquivo de saída já foi fechado conta do bloco de execução with!")
