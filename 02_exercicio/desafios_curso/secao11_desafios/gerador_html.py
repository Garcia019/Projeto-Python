# Gerador HTML - version-v5.0
bloco_atributos = ("bloco_accesskey", "bloco_id")
ul_atributos = ("ul_id", "ul_style")


def filtrar_atributos(informados, suportados):
    return "".join(f" {chave.split('_')[-1]}='{valor}'"
                   for chave, valor in informados.items()
                   if chave in suportados)


def tag_bloco(conteudo, *args, classe="success",
              inline=False, **novos_atributos):
    tag = "span" if inline else "div"
    html = conteudo if not callable(conteudo)\
        else conteudo(*args, **novos_atributos)
    atributos = filtrar_atributos(novos_atributos, bloco_atributos)
    return f"<{tag}{atributos} class='{classe}'>{html}</{tag}>"


def tag_lista(*itens, **novos_atributos):
    lista = "".join(f"<li>{item}</li>" for item in itens)
    return f"<ul{filtrar_atributos(novos_atributos,ul_atributos)}>{lista}</ul>"


if __name__ == "__main__":
    print(tag_bloco("bloco"))
    print(tag_bloco("inline e classe", classe="info", inline=True))
    print(tag_bloco("inline", inline=True))
    print(tag_bloco(inline=True, conteudo="inline"))
    print(tag_bloco("falhou", classe="erro"))
    print(tag_bloco(tag_lista("item1", "item2"), classe="info"))
    print(tag_bloco(tag_lista, "Sábado", "Domingo",
                    classe="info", inline=True))
    print(tag_bloco(tag_lista, "Item1", "Item2", classe="info",
                    bloco_accesskey="m", bloco_id="conteudo", ul_id="lista"))
