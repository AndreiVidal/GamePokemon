import random


class Pokemon:

    def __init__(self, especie=None, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return f'{self.nome}({self.level})'

    def atacar(self, inimigo):
        print(f'{self} atacou {inimigo}')


class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, inimigo):
        print(f'{self} lançou um choque do trovão em {inimigo}')


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, inimigo):
        print(f'{self} lançou uma bola de fogo em {inimigo}')


class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, inimigo):
        print(f"{self} lançou um jato d'gua em {inimigo}")
