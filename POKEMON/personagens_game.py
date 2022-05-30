from pokemon_game import *
import random
from time import sleep

NOMES_INIMIGOS = [
    'Equipe Rocket', 'Jessie', 'James', 'Cassidy', 'Proton',
    'Petrel', 'Ariana', 'Archer', 'Butch', 'Tríade das Sombras',
    'Equipe Galáctica', 'Equipe Magma', 'Sr Giovanni', 'Gary',
]

NOMES_ALEATORIO = [
    'Ash Ketchum', 'Misty', 'Brock', 'Serena',
    'Chris', 'Cilan',
]

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Charmilion'),
    PokemonFogo('Arcanaine'),
    PokemonAgua('Psyduck'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Totodile'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Dracozolt'),
    PokemonEletrico('Electabuzz')
]


class Personagens:

    def __init__(self, nome=None, pokemons=None):
        if pokemons is None:
            pokemons = []
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES_ALEATORIO)
        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemon(self):
        sleep(1)
        if self.pokemons:
            print(f'Pokedex de {self}')
            for index, pokemon in enumerate(self.pokemons):
                print(f'[{index}] - {pokemon}')
        else:
            print(f'{self} não possui nenhum Pokemon')

    def escolher_pokemon(self):
        sleep(1)
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'Pokemon escolhido por {self} foi {pokemon_escolhido}.')
            return pokemon_escolhido
        else:
            print('Esse jogador não possui pokemon para ser escolhido.')

    def batalhar(self, pessoa):
        sleep(1)
        print(f'{self} iniciou uma batalha com {pessoa}')
        pessoa.mostrar_pokemon()
        pokemon_adversario = pessoa.escolher_pokemon()
        pokemon = self.pokemon_batalha()

        if pokemon and pokemon_adversario:

            while True:

                vitoria = pokemon.atacar(pokemon_adversario)
                if vitoria:
                    sleep(1)
                    print(f'{self} Ganhou !!')
                    break
                derrota = pokemon_adversario.atacar(pokemon)
                if derrota:
                    sleep(1)
                    print(f'{pessoa} Venceu !!')
                    break


class Player(Personagens):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        sleep(1)
        print(f'{self} capturou {pokemon}')

    def pokemon_batalha(self):
        self.mostrar_pokemon()

        if self.pokemons:
            while True:
                sleep(1)
                escolha = input('Escolha um pokemon para batalhar: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    sleep(1)
                    print(f'{pokemon_escolhido} eu escolho voçê!!!')
                    return pokemon_escolhido
                except:
                    print('Escolha inválida: ')
        else:
            print('Voçê não possui Pokemon para batalhar.')


class Inimigo(Personagens):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if pokemons is None:
            pokemons = []

        super().__init__(nome=nome, pokemons=pokemons)
        if not nome:
            self.nome = random.choice(NOMES_INIMIGOS)
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))
