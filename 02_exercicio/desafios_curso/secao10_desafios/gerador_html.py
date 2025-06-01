# Gerador HTML - version-v2.0

def tag_bloco(texto, classe="success", inline=False):
    # Adicionando um novo parâmetro opcional a função
    tag = "span" if inline else "div"
    return f"<{tag} class='{classe}'>{texto}</{tag}>"


if __name__ == "__main__":
    print(tag_bloco("bloco"))
    print(tag_bloco("inline e classe", "info", True))
    # Utilizando Parâmetros de forma Posicional
    print(tag_bloco("inline", inline=True))
    # Nesse caso utilizando o parâmetro Nomeado
    print(tag_bloco(inline=True, texto="inline"))
    # Nesse caso utilizando o parâmetro Nomeado
    print(tag_bloco("falhou", classe="erro"))
