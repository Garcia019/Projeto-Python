"""
Extrair o nono e o quarto campos do arquivo CSV sobre
Região de influência das Cidades do IBGE, que pode ser baixado em:
http://www.geoservicos.ibge.gov.br/geoserver/wms?service=WFS&version=1.0.0&request=GetFeature&typeName=CGEO:RedeUrbanaSintese_Regic2007&
outputFormat=CSV. ignorando a primeira linha que é o cabeçalho:

O arquivo se encontra em ISO-8859-1 (aka latin1), será necessário usar
o parâmetro encoding da função open.
Por segurança temos uma cópia deste arquivo no nosso servidor,
que pode ser baixado em
http://files.cod3r.com.br/curso-python/desafio-ibge.csv.
Isso é importante em vários casos como indisponibilidade
ou até reestruturação do site do IBGE.
"""

import csv
from urllib import request

"""
Utilizei um parâmetro da função open, o encoding para ler o arquivo
na codificação correta nesse caso latin-1
"""


def read(url):
    with request.urlopen(url) as entrada:
        print("Baixando o CSV...")
        dados = entrada.read().decode("latin1")
        print("Download Completo!")
        for cidade in csv.reader(dados.splitlines()[1:20]):
            # Removi a primeira linha e limitei em 20 para não ficar extenso
            print(f"Nome origem: {cidade[3]}, Nome Destino: {cidade[8]}")


if __name__ == "__main__":
    read(r"http://files.cod3r.com.br/curso-python/desafio-ibge.csv")
    # utiliza-se o "r" para garantir que nenhum elemento da url seja executado
