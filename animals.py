# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Donkey:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Horse:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Cow:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
    
class Pig:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()


class KingSnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Cobra:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class RattleSnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
    
class Python:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
    
class Anadonda:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class GoldFish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Barracuda:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
    
class ElectricEel:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
    
class Piranha:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
    
class SwordFish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()



miss_fuzz = Llama("Miss Fuzz", "domestic llama")
mr_snake = KingSnake("Mr. Snake", "king snake")
zappy = ElectricEel("Zappy", "electric eel")

print(miss_fuzz.name)
print(mr_snake.name)
print(zappy.species)