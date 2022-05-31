from pokemon_game import *
from personagens_game import *
from time import sleep
import pickle
from os import remove

def salvar_game(player):
    try:
        with open('databse.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
    except:
        print('Ocorreu algum erro ao salvar o Jogo!!')


def load_game():
    try:
        with open('databse.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            return player
    except:
        print('Nenhum Jogo Salvo!!')

    

def pokemon_inicial(player):
    print(f'Escolha seu primeiro Pokemon pra iniciar sua jornada! ')

    pikachu = PokemonEletrico('Pikachu', 1)
    charmander = PokemonFogo('Charmander', 1)
    squirtle = PokemonAgua('Squirtle', 1)

    print('''
Voçê tem 3 pokemons disponíveis para escolher:
    [1] - Pikachu
    [2] - Charmander
    [3] - Squirtle ''')

    while True:
        escolha = input('Escolha um deles pra iniciar sua jornada: ')

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


if __name__ == "__main__":
    print('############################')
    print('Bem vindo ao mundo Pokemon!!')
    print('############################')
    player = load_game()

    if not player:
        nome = input('Qual seu Nome: ').capitalize()
        player = Player(nome)

        print(f'''
    Olá {nome} esse é um mundo de fantasia repleto de aventuras, venha fazer parte dessas aventuras e se torne um mestre Pokemon!!
    ''')

        if player.pokemons:
            print('Voçê já possui alguns pokemons.')
            player.mostrar_pokemon()
        else:
            print('Voçê não possui nenhum pokemon, portando voçê precisa de um pokemon para se aventurar!!')
            pokemon_inicial(player)

        print(f'{nome} voçê encontrou um antigo adversário aproveite essa oportunidade pra testar seu mais novo Pokemon!!')

        gary = Inimigo(nome='Gary', pokemons=[PokemonFogo('Charmilion', 1)])
        while True:
            primeiraLuta = input(
                f'{player} voçê deseja batalhar com Gary ? [S]/[N] ')
            if primeiraLuta == 's':
                player.batalhar(gary)
                print(
                    f'Parabéns {player} pela sua primeira batalha, agora desfrute esse mundo!!')
                break
            elif primeiraLuta == 'n':
                print(f'{player} desistiu da luta..')
                break
            else:
                print('Opção inválida..')
                continue

        while True:
            salvar = input('Deseja salvar o jogo?: [S]/[N]: ')
            if salvar == 's':
                salvar_game(player)
                break
            elif salvar == 'n':
                print('Voçê não salvou o Jogo')
                break
            else:
                print('opção inválida')
                continue

    while True:
        print('______________________________')
        print('######___MENU INICIAL___######')
        print('______________________________')
        escolha = input('''
    [1] - Explorar mundo !
    [2] - Lutar com inimigo!
    [3] - Pokedex!
    [4] - Sair e excluir jogo salvo..
    [0] - Sair..
Digite a opção desejada: ''')

        if escolha == '0':
            print('Saindo do jogo...')
            break
        elif escolha == '1':
            player.explorar()
            salvar_game(player)
        elif escolha == '2':
            player.batalhar(Inimigo())
            salvar_game(player)
        elif escolha == '3':
            player.mostrar_pokemon()
        elif escolha == '4':
            try:
                remove('databse.db')
                print('jogo deletado com sucesso!!')
                break
            except:
                print('Nenhum arquivo encontrato!!')
                continue
        else:
            print('Escolha inválida!!')
