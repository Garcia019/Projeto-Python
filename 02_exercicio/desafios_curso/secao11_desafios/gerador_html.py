# Gerador HTML - version-v4.0

# Ao utilizar parâmetros especiais de empacotamento ou desempacotamento
# Devemos nomear todos os parâmetros da função para o uso correto da mesma
# Nesse caso não podemos passar nenhum parâmetros posicionais
# todos os parâmetros devem ser parâmetros nomeados
# se passarmos 2 ou mais parâmetros pois
# a posição do *args é no segundo parâmetro
def tag_bloco(conteudo, *args, classe="success", inline=False):
    # Adicionando um novo parâmetro opcional a função
    tag = "span" if inline else "div"
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f"<{tag} class='{classe}'>{html}</{tag}>"


# No caso essa função utiliza do empacotamento de todas as variáveis passadas
# cria uma tupla com essa variáveis
def tag_lista(*itens):
    lista = "".join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"


if __name__ == "__main__":
    print(tag_bloco("bloco"))
    print(tag_bloco("inline e classe", classe="info", inline=True))
    # Utilizando Parâmetros de forma Posicional
    print(tag_bloco("inline", inline=True))
    # Nesse caso utilizando o parâmetro Nomeado
    print(tag_bloco(inline=True, conteudo="inline"))
    # Nesse caso utilizando o parâmetro Nomeado
    print(tag_bloco("falhou", classe="erro"))
    print(tag_bloco(tag_lista("item1", "item2"), classe="info"))
    # Ao utilizar parâmetros especiais de empacotamento ou desempacotamento
    # Devemos nomear todos os parâmetros da função para o uso correto da mesma
    # Nesse caso não podemos passar nenhum parâmetros posicionais
    # todos os parâmetros devem ser parâmetros nomeados
    print(tag_bloco(tag_lista, "Sábado", "Domingo",
                    classe="info", inline=True))
