from random import choices

moeda = ['cara','coroa']

while True:
    try:
        print('Cara ou Coroa?')
        resposta = input('').lower().strip()

        if resposta not in moeda:
            raise ValueError("Digita certo ai namoral")
    
        resultado = choices(moeda)[0]    

    except ValueError as errado:
        print(errado)
    
    else: 
        print(f'Sua resposta foi {resultado}')
        print('*Jogando a moeda para cima*')
        
        if resposta == resultado:
            print(f"A moeda deu {resultado}, ganho, meus parabens viu")

        else:
            print("perdeu, mt ruim slc")
    finally:
        print("Fim da rodada")


    options = ['s','n']

    while True:
        try:
            jogar_novamente = (input('jogar novamente? (s/n)')).lower().strip()

            if jogar_novamente not in options:
                raise ValueError("Digita certo ai namoral")
            break
        except ValueError as errado:
            print(errado)

    if jogar_novamente == 'n':
        break
