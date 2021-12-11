import json
import random


class Players:
    """This class holds all of the player information."""

    def __init__(self):
        self.p_name = ""
        # Current level so far lvl 100 is the highest obtainable
        self.lvl = 1
        # Player Experience. When the player hits the thresh hold
        # they will level up. to get to level 100 is 329240xp with
        # the current progression levels
        self.XP = 0
        self.maxXP = 10
        # Job title of the player.
        # Magician, Warrior, Archer
        self.job = ['Magician', 'Warrior', 'Archer', '?']
        # classes
        self.p_class = random.randint(0, 0)
        # Health power
        self.HPh = 10
        self.maxHP = 10
        self.MPh = 10
        self.maxMP = 10
        self.ENh = 10
        self.maxEN = 10
        # Stats
        self.Energy = 0
        self.Strength = 0
        self.Intellect = 0
        self.Agility = 0
        self.Stamina = 0
        self.Luck = 0
        self.usp = 10
        self.skills = self.get_skills(self.p_class)
        self.set_attt()
        # difficulty
        self.difficulty = 0

    def display_info(self) -> None:
        print(f"Level: {self.lvl}   XP: {int(self.XP):,}/{int(self.maxXP):,}")
        print(f"Job: {self.job[self.p_class]} Class: {self.p_class}")
        print(f"HP: {self.HPh}/{self.maxHP}")
        if self.p_class == 1:
            print(f"MP: {self.MPh}/{self.maxMP}")
        elif self.p_class in [2, 3]:
            print(f"Energy: {self.ENh}/{self.maxEN}")
        print(f"Strength: {self.Strength}")
        print(f"Intellect: {self.Intellect}")
        print(f"Agility: {self.Agility}")
        print(f"Stamina: {self.Stamina}")
        print(f"Luck: {self.Luck}")
        print(f"Skills: ", self.skills)
        print(f"Unassigned Stat Points: {self.usp}")
        return

    def unassigned_points(self) -> None:
        while self.usp > 0:
            print(f'You have {self.usp} points to spend')
            user_input = str(input('Would you like to spend your points (Yes, No)?'))
            if user_input.lower() not in ['yes', 'no', 'n', 'y']:
                print('Incorrect answer. Please try again')
            elif user_input.lower() in ['no', 'n']:
                print('No Points Spent')
                break
            else:
                while self.usp > 0:
                    print(f'You have {self.usp} Points to use.')
                    print('Which category do you want to assign your points?')
                    print('(S)trength')
                    print('(I)ntellect')
                    print('(A)gility')
                    print('S(t)amina')
                    print('(L)uck')
                    user_input = str(input('? '))
                    if user_input.lower() not in ['s', 'i', 'a', 't', 'l']:
                        print('Incorrect answer. Please try again')
                    else:
                        while True:
                            a_input = int(input('How many points to assign? '))
                            if a_input > self.usp:
                                print('Sorry you can not spend more points than you currently have. Please try again.')
                            else:
                                break
                        if user_input.lower() == 's':
                            self.Strength += a_input
                        elif user_input.lower() == 'i':
                            self.Intellect += a_input
                        elif user_input.lower() == 'a':
                            self.Agility += a_input
                        elif user_input.lower() == 't':
                            self.Stamina += a_input
                        elif user_input.lower() == 'l':
                            self.Luck += a_input
                        self.usp -= a_input
        return

    def level_up(self) -> None:
        """This function is to level up the character"""
        while self.XP >= self.maxXP:
            # XP leveling section
            self.XP -= self.maxXP
            self.maxXP += self.level_progression()
            self.maxXP = self.maxXP
            self.lvl += 1
            # ?
            self.maxHP += 10
            self.maxMP += 10
        return

    def level_progression(self) -> float:
        if 0 < self.lvl <= 10:
            return 25
        elif 10 < self.lvl <= 20:
            return 50
        elif 20 < self.lvl < 50:
            return 75
        elif 50 < self.lvl < 75:
            return 100
        elif 75 < self.lvl < 100:
            return 125
        return 25

    def set_attt(self) -> None:
        if self.p_class == 0:
            self.Strength = random.randint(7, 11)
            self.Intellect = random.randint(12, 16)
            self.Agility = random.randint(8, 12)
            self.Stamina = random.randint(12, 16)
            self.Luck = random.randint(8, 12)
            self.usp = random.randint(1, 3)
        elif self.p_class == 1:
            self.Strength = random.randint(12, 16)
            self.Intellect = random.randint(7, 11)
            self.Agility = random.randint(8, 12)
            self.Stamina = random.randint(8, 12)
            self.Luck = random.randint(12, 16)
            self.usp = random.randint(1, 3)
        elif self.p_class == 2:
            self.Strength = random.randint(8, 12)
            self.Intellect = random.randint(8, 12)
            self.Agility = random.randint(12, 16)
            self.Stamina = random.randint(7, 11)
            self.Luck = random.randint(12, 16)
            self.usp = random.randint(1, 3)
        return

    def get_skills(self, c_num) -> str:
        if c_num == 0:
            return "Fireball (2 mana; 2*intellect on 1 enemy), " \
                   "Heal (3 mana; heal yourself for 50 HP), " \
                   "Electrocute (3 mana; 1*intellect to all creatures), " \
                   "Hit (0 mana; 1*strength on 1 enemmy)"
        elif c_num == 1:
            return "Pierce (2 energy; 2*strength on max 3 ennemies), " \
                   "Slice (3 energy; 4*strength on one enemmy), " \
                   "Strengthen (4 energy, augment your shield by 50 for 3 turns) " \
                   "Hit (0 energy; 1*strength on 1 enemmy)"
        elif c_num == 2:
            return "still need to add in skills"
        elif c_num == 3:
            return ", Watershot (5 mana, 3*intelligence on 1 creature)"
        else:
            return "?"


"""
p = Players()
p.display_info()
p.Xp = 25
p.level_up()
p.display_info()
"""
