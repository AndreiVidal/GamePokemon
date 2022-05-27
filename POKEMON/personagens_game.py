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
            for index, pokemon in enumerate(self.pokemons):
                print(f'[{index}] - {pokemon}')
        else:
            print(f'{self} não possui nenhum Pokemon')


    def pokemon_batalha(self):
        self.mostrar_pokemon()
        

        if self.pokemons:
            while True:
                escolha = input('Escolha um pokemon para batalhar: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f'{pokemon_escolhido} eu escolho voçê!!!')
                    return pokemon_escolhido
                    
                except:
                    print('Escolha inválida: ')
        else:
            print('Voçê não possui Pokemon para batalhar.')


    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')
        pessoa.mostrar_pokemon()
        self.pokemon_batalha()

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

