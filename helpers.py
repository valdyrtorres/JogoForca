import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS

def gerar_palavra_secreta():
    """
    Função para randomicamente selecionar uma palavra do arquivo texto
    :return:
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as f_obj:
        palavra = f_obj.read().splitlines()

    return random.choice(palavra)
