from datetime import date

class Barracuda:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
    