import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS


def gerar_palavra_secreta():
    """
    Função para randomicamente selecionar uma palavra do arquivo texto
    :return: string
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as f_obj:
        palavras = f_obj.read().splitlines()

    return random.choice(palavras)


def verificar_letra_informada(palavra_secreta, suas_tentativas, tentativa):
    """
    Verifica se a letra dada está correta
    :param palavra_secreta: Gerada com base no arquivo texto de palavras secretas
    :param suas_tentativas: Lista com todas as tentativas
    :param tentativa: letra inserida nesta jogada
    :return: retorna um status
    """
    status = ''  # O status precisa ser zerado toda vez que a função for chamada
    acertos = 0  # Também precisa ser zerado para essa jogada/tentativa

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


def jogo(palavra_secreta):
    """
    Função principal do jogo
    :param palavra_secreta: palavra secreta gerada a partir do arquivo texto
    :return:
    """
    chute = 0
    adivinhado = False
    suas_tentativas = []
    chances = total_tentativas(palavra_secreta)
    total_chances = chances

    print(f" - Total de chances: {chances}")
    while chute < total_chances:
        letra_tentativa = input("\nEntre com sua letra: ")

        # Diminuindo as chances de 1 a 1
        chances -= 1

        # Se a letra já foi informada ou adivinhada
        if letra_tentativa in suas_tentativas:
            print(f"*** ATENÇÃO *** Você já tentou essa letra.")
        elif len(letra_tentativa) == 1:  # Precisa ser 1 letra somente de tentativa
            # Adicionando as letras no local correto da palavra
            suas_tentativas.append(letra_tentativa)
            resultado = verificar_letra_informada(palavra_secreta, suas_tentativas, letra_tentativa)
            if resultado == palavra_secreta:
                adivinhado = True
                print(f"\n=== Parabéns, você venceu! - Palavra é '{palavra_secreta}'.===")
                break
            else:
                print(f" - {' '.join(resultado)}")
        else:
            print(f"Entrada incorreta, informe somente 1 letra.")

        # Mostra quantas tentativas ainda restam
        print(f" - Tentativas restantes: {chances}")
        chute += 1
    if chute == total_chances:
        print(f"\n *** Suas tentativas acabaram. A palavra secreta é '{palavra_secreta}'. ***")
