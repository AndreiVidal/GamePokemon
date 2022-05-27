from pokemon_game import *

from personagens_game import *

def primeiro_pokemon(player):
    print(f'Olá {player} ecolha seu primeiro Pokemon pra iniciar sua jornada! ')

    pikachu = PokemonEletrico('Pikachu', 1)
    charmander = PokemonFogo('Charmander', 1)
    squirtle = PokemonAgua('Squirtle', 1)
    
    print('''
    Voçê tem 3 pokemons disponíveis para escolher:
    [1] - Pikachu
    [2] - Charmander
    [3] - Squirtle   
''')

    while True:
        escolha = input('Digite a opção desejada: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')
