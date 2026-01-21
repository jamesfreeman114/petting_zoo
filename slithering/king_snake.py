from datetime import date

class KingSnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
    
    def __str__(self):
        return f"{self.name} is a {self.species}"