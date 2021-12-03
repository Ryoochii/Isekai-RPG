import json
import random


class Players:
    """This class holds all of the player information."""

    def __init__(self):
        # Current level so far lvl 100 is the highest obtainable
        self.lvl = 1
        # Player Experience. When the player hits the thresh hold
        # they will level up.
        self.XP = 0
        self.maxXP = 10
        # Job title of the player.
        # Magician, Warrior, Archer
        self.job = ""
        # classes
        self.classes = random.randint(1, 3)
        # Health power
        self.HPh = 0
        self.maxHP = 0
        self.MPh = 0
        self.maxMP = 0
        self.ENh = 0
        self.maxEN = 0
        # Stats
        self.Energy = 0
        self.Strength = 0
        self.Intellect = 0
        self.Agility = 0
        self.Stamina = 0
        self.Luck = 0
        self.usp = 10
        self.skills = {}

    def display_info(self) -> None:
        print(f"Level: {self.lvl}   XP: {self.XP}/{self.maxXP}")
        print(f"Job: {self.job}")
        print(f"HP: {self.HPh}/{self.maxHP}")
        if self.classes == 1:
            print(f"MP: {self.MPh}/{self.maxMP}")
        elif self.classes in [2, 3]:
            print(f"Energy: {self.ENh}/{self.maxEN}")
        print(f"Strength: {self.Strength}")
        print(f"Intellect: {self.Intellect}")
        print(f"Agility: {self.Agility}")
        print(f"Stamina: {self.Stamina}")
        print(f"Luck: {self.Luck}")
        print(f"Skills: {self.skills}")
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
        if self.XP > self.maxXP:
            self.XP -= self.maxXP
            self.maxXP *= self.next_level()
            self.lvl += 1

        return

    def next_level(self) -> float:
        if 0 < self.lvl <= 10:
            return 1.15
        elif 10 < self.lvl <= 20:
            return 1.2
        elif 20 < self.lvl:
            return 1.5

        return 1.15


p = Players()
p.display_info()
p.unassigned_points()
