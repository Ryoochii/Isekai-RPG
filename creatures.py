import random

class Creatures():
    """This class is for all the creatures. """
    def __init__(self):
        self.name = ""
        self.num_cs = self.num_c()
        self.fight_creatures = self.creature_name()

    def num_c(self) -> int:
        return random.randint(3, 6)

    def fight(self) -> list:
        temp_n = []
        for i in range(self.num_cs):
            temp_n.append('1')
        return temp_n

    def creature_name(self) -> dict:
        temp_n = {}
        c_names = {'name': 'goblin', 'hp': 20, 'attackpower': 1}
        for i in range(self.num_cs):
            temp_n[i] = c_names
        return temp_n

"""                   
                    ('hobgoblin', 50),
                    ('slime', 10),
                    ('zombie', 40),
        ]
"""

"""        
HPkobolds = 75
HPghost = 75

HPgoblinking = 200

HPspider = 100
HPwolf = 150
HPskeletonsoldier = 50
HPskeletonknight = 250
HPghoul = 250

HPspiderqueen = 500

HPorc = 400
HPbeastmen = 500
HPbasilisk = 500
HPcentipede = 600
HPcentaur = 650

Satyr = 800

HPearthelemental = 750
HPfireelemental = 750
HPwaterelemental = 750
HPwindelemental = 750

HPfusedelemental = 1250

HPfairy = 1000
HPelf = 1500
HPdwarf = 1750
HPdarkknight = 2000

HPdarkmage = 2500

# HP
HPskeletondragon = 3000

HPgolem = 10000
HPminotaur = 10000
HPdemonlackey = 12500
HPwerewolf = 12500

HPsuccubi = 15000

HPkraken = 15000
HPmanticore = 16000
HPdarkelf = 15000
HPwyvern = 16000
HPtroll = 15500

HPphoenix = 19000

HPlich = 17500
HPvampire = 20000
HPgiant = 25000
HPchimera = 30000
HPdragon = 50000

HPDemonlord = 100000
"""