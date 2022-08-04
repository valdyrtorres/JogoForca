import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS

def gerar_palavra_secreta():
    """
    Função para randomicamente selecionar uma palavra do arquivo texto
    :return: uma palavra aleatória
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as f_obj:
        palavra = f_obj.read().splitlines()

    return random.choice(palavra)


def verificar_letra_informada(palavra_secreta, suas_tentativas, tentativa):
    """
    Verifica se a letra dada está correta
    :param palavra_secreta: Gerada com base no arquivo texto de palavras secretas
    :param suas_tentativas: Lista com todas as tentativas
    :param tentativa: letra inserida nesta jogada
    :return: retorna um status
    """
    status = '' # O status precisa ser zerado toda vez que a função for chamada
    acertos = 0 # Também precisa ser zerado para essa jogada/tentativa

    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra
        else:
            status += '*'

        if letra.lower() == tentativa.lower():
            acertos += 1

    print(f"\n - Acertos {acertos} letras(s) '{tentativa}")

    return status

def total_tentativas(palavra_secreta):
    """
    Define a quantidade de tentativas de acordo com a palavra secreta
    :param palavra_secreta: gerada aleatoriamente
    :return: Quantidade de tentativas
    """
    chances = len(palavra_secreta)
    return chances + TENTATIVAS_ADICIONAIS
