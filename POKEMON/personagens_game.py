from pokemon_game import *
import random

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
        if self.pokemons:
            print(f'Pokedex de {self}')
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} não possui nenhum Pokemon')


class Player(Personagens):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}')


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


