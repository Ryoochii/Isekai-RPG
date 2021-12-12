import random


def num_c() -> int:
    return random.randint(3, 6)


class Creatures:
    """This class is for all the creatures. """
    def __init__(self):
        self.num_cs = num_c()
        self.fight_creatures = self.fight_party()
        self.c_names = {}

    def fight_party(self) -> dict:
        temp_n = {}
        self.creature_name()
        for i in range(self.num_cs):
            temp_n[i] = self.c_names['goblin']['name']
        return temp_n

    def creature_name(self) -> None:
        self.c_names = {'goblin': {'name': 'goblin', 'hp': 20, 'attackpower': 1},
                        'hobgoblin': {'name': 'hobgoblin', 'hp': 50, 'attackpower': 1},
                        'slime': {'name': 'slime', 'hp': 10, 'attackpower': 1},
                        'zombie': {'name': 'zombie', 'hp': 40, 'attackpower': 1},
                        'kobolds': {'name': 'kobolds', 'hp': 75, 'attackpower': 1},
                        'ghost': {'name': 'ghost', 'hp': 75, 'attackpower': 1},
                        'goblinking': {'name': 'goblinking', 'hp': 200, 'attackpower': 1},
                        'spider': {'name': 'spider', 'hp': 100, 'attackpower': 1},
                        'wolf': {'name': 'wolf', 'hp': 150, 'attackpower': 1},
                        'skeletonsoldier': {'name': 'skeletonsoldier', 'hp': 50, 'attackpower': 1},
                        'skeletonknight': {'name': 'skeletonknight', 'hp': 250, 'attacakpower': 1},
                        'ghoul': {'name': 'ghoul', 'hp': 250, 'attackpower': 1},
                        'spiderqueen': {'name': 'spiderqueen', 'hp': 500, 'attackpower': 1},
                        'orc': {'name': 'orc', 'hp': 400, 'attackpower': 1},
                        'beastmen': {'name': 'beatman', 'hp': 500, 'attackpower': 1},
                        'basilisk': {'name': 'baskilisk', 'hp': 500, 'attackpower': 1},
                        'centipede': {'name': 'centipede', 'hp': 600, 'attackpower': 1},
                        'centaur': {'name': 'centaur', 'hp': 650, 'attackpower': 1},
                        'satyr': {'name': 'satyr', 'hp': 800, 'attackpower': 1},
                        'earthelemental': {'name': 'earthelemental', 'hp': 750, 'attackpower': 1},
                        'fireelemental': {'name': 'fireelemental', 'hp': 750, 'attackpower': 1},
                        'waterelemental': {'name': 'waterelemental', 'hp': 750, 'attackpower': 1},
                        'windelemental': {'name': 'windelemental', 'hp': 750, 'attackpower': 1},
                        'fusedelemental': {'name': 'fusedelemental', 'hp': 1250, 'attackpower': 1},
                        'fairy': {'name': 'fairy', 'hp': 1000, 'attackpower': 1},
                        'elf': {'name': 'elf', 'hp': 1500, 'attackpower': 1},
                        'dwarf': {'name': 'dwarf', 'hp': 1750, 'attackpower': 1},
                        'darkknight': {'name': 'darkknight', 'hp': 2000, 'attackpower': 1},
                        'darkmage': {'name': 'darkmage', 'hp': 2500, 'attackpower': 1},
                        'skeletondragon': {'name': 'skeletondragon', 'hp': 3000, 'attackpower': 1},
                        'golem': {'name': 'golem', 'hp': 10000, 'attackpower': 1},
                        'minotaur': {'name': 'minotaur', 'hp': 10000, 'attackpower': 1},
                        'demonlackey': {'name': 'demonlackey', 'hp': 12500, 'attackpower': 1},
                        'werewolf': {'name': 'werewolf', 'hp': 12500, 'attackpower': 1},
                        'succubi': {'name': 'succubi', 'hp': 15000, 'attackpower': 1},
                        'kraken': {'name': 'kraken', 'hp': 15000, 'attackpower': 1},
                        'manticore': {'name': 'manticore', 'hp': 16000, 'attackpower': 1},
                        'darkelf': {'name': 'darkelf', 'hp': 15000, 'attackpower': 1},
                        'wyvern': {'name': 'wyvern', 'hp': 16000, 'attackpower': 1},
                        'troll': {'name': 'troll', 'hp': 15500, 'attackpower': 1},
                        'phoenix': {'name': 'phoenix', 'hp': 19000, 'attackpower': 1},
                        'lich': {'name': 'lich', 'hp': 17500, 'attackpower': 1},
                        'vampire': {'name': 'vampire', 'hp': 20000, 'attackpower': 1},
                        'giant': {'name': 'gaint', 'hp': 25000, 'attackpower': 1},
                        'chimera': {'name': 'chimera', 'hp': 30000, 'attackpower': 1},
                        'dragon': {'name': 'dragon', 'hp': 50000, 'attackpower': 1},
                        'demonlord': {'name': 'demonlord', 'hp': 100000, 'attackpower': 1}}
        return
