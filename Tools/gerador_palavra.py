import random

def gerar_palavra(opcoes):
    tamanho = len(opcoes)
    posicao_sorteada = random.randint(0, tamanho)
    return opcoes[posicao_sorteada]
