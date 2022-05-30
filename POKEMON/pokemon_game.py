import random
from time import sleep


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

        self.ataque = self.level * 8
        self.vida = self.level * 12

    def __str__(self):
        return f'{self.nome} [{self.level}]'

    def atacar(self, inimigo):
        sleep(1)
        inimigo.vida = inimigo.vida - self.ataque
        sleep(1)
        print(f'{inimigo} perdeu {self.ataque} de vida!!')

        if inimigo.vida <= 0:
            sleep(1)
            print(f'{inimigo} perdeu a batalha')
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, inimigo):
        sleep(1)
        print(f'{self} lançou um choque do trovão em {inimigo}')
        return super().atacar(inimigo)


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, inimigo):
        sleep(1)
        print(f'{self} lançou uma bola de fogo em {inimigo}')
        return super().atacar(inimigo)


class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, inimigo):
        sleep(1)
        print(f"{self} lançou um jato d'gua em {inimigo}")
        return super().atacar(inimigo)
