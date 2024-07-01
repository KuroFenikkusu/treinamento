"""

Jogo da forca

"""
import random

nomes = {0 : 'julia', 1: 'valdinei', 2: 'donis', 3: 'beatriz', 4: 'larissa', 5: 'fernanda', 6: 'gabriel'}
animais = {0 : 'tartaruga', 1: 'coelho', 2: 'leopardo', 3: 'elefante', 4: 'baleia', 5: 'cachorro', 6: 'gato'}
jogos = {0 : 'league-of-legends', 1: 'sekiro', 2: 'dark souls', 3: 'cookie-clicker', 4: 'elden-ring', 5: 'minecraft', 6: 'xadrez'}
profissoes = {0 : 'programador', 1: 'contador', 2: 'enfermeiro', 3: 'designer', 4: 'veterinário', 5: 'motoboy', 6: 'professor'}


palavras = {
    "nome": nomes, 
    "animal": animais, 
    "jogo": jogos, 
    "profissao": profissoes}

def forca():
    cat = random.choice(list(palavras.keys()))
    word = random.choice(list(palavras[cat].values()))

    print(f"Olá jogador, bem vindo ao jogo da forca!")
    print(f"A dica da palavra sorteada é: {cat}.")

    progress = ['_'] *len(word)
    attempts = 6
    guessed = []

    while True:
        print(" ".join(progress))
        print(f'Tentativas: {attempts}')
        letter = input("Digite uma letra: ").lower().strip()
        if letter in guessed:
            print("Letras repetidas não são permitidas, favor digitar outra")
            continue

        if not letter.isalpha() or len(letter) != 1:
            print("Por favor, digitar somente letras do alfabeto")
            continue
        guessed.append(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    progress[i] = letter

        else:
            attempts = attempts - 1
            
        if "_" not in progress:
            print(f"Parabens, você descobriu a palavra {word}")
            break
        if attempts == 0:
            print(f"Fim de jogo, a palavra era {word}")
            break

while True:
    forca()
    restart = ['s','n']
    while True:
        try:
            jogar_novamente = (input('jogar novamente? (s/n)')).lower().strip()

            if jogar_novamente not in restart:
                    raise ValueError("Formato inválido")
            break
        except ValueError as errado:
            print(errado)

    if jogar_novamente == 'n':
        break

