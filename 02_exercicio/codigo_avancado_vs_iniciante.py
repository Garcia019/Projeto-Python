""""
Diferença entre dois mesmo códigos que fazer a mesma coisa
porem com níveis diferentes de detalhes e otimização
"""

import unicodedata

def remover_acentos_iniciante(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''
    for letra in texto:
        if unicodedata.category(letra) != 'Mn':
            texto_sem_acentos += letra
    return texto_sem_acentos



def remover_acentos_avancado(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join([c for c in texto_normalizado if not unicodedata.combining(c)])
    return texto_sem_acentos


texto_com_acentos = "Olá, mundo! Você está bem?"
texto_sem_acentos_iniciante = remover_acentos_iniciante(texto_com_acentos)
texto_sem_acentos_avancado = remover_acentos_avancado(texto_com_acentos)
print(texto_sem_acentos_iniciante)  # Saída: Ola, mundo! Voce esta bem?
print(texto_sem_acentos_avancado)
