import json
from os.path import exists as file_exists
import time
import sys
from player import Players

player1=Players()
def print_speed(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(player1.text)

class GameData:
    """ This class will offer loading and saving of game data"""
    def __init__(self):
        self.file = 'RPGsave.txt'
        self.file_exists = bool(file_exists(self.file))

    def load_game(self, player_data, creatures) -> bool:
        if self.file_exists:
            with open(self.file, 'r') as user_data_file:
                user_data = json.load(user_data_file)
                self.set_player_data(player_data, user_data)
                self.set_creature_data(creatures, user_data)
                print_speed('Saved data has been loaded successfully!\n')
                return True
        else:  # don't need to initialize values -- already initialized when class created
            print_speed('No saved data found...\n')
            print_speed('Starting a fresh game...\n')
            return False

    def save_game(self, player_data, creatures) -> None:
        if not self.file_exists:
            print_speed("No previous save! Creating a new save...\n")
        save_data = self.set_save_data(player_data, creatures)
        with open(self.file, 'w') as user_data_file:
            json.dump(save_data, user_data_file)
        return

    @staticmethod
    def set_player_data(p, data) -> None:
        p.p_name = data['p_name']
        p.lvl = data['lvl']
        p.XP = data['XP']
        p.maxXP = data['maxXP']
        p.job = data['job']
        p.p_class = data['p_class']
        p.HPh = data['HPh']
        p.maxHP = data['maxHP']
        p.MPh = data['MPh']
        p.maxMP = data['maxMP']
        p.ENh = data['ENh']
        p.maxEN = data['maxEN']
        p.Energy = data['Energy']
        p.Strength = data['Strength']
        p.Intellect = data['Intellect']
        p.Agility = data['Agility']
        p.Accuracy = data['Accuracy']
        p.Luck = data['Luck']
        p.usp = data['usp']
        p.skills = data['skills']
        p.difficulty = data['difficulty']
        p.main_location = data['main_location']
        p.s_location = data['location']
        return

    @staticmethod
    def set_creature_data(c, data) -> None:
        #c.nums_cs = data['nums_cs']
        c.c_names = data['c_names']
        return

    @staticmethod
    def set_save_data(p, c) -> dict:
        temp = {'p_name': p.p_name, 'lvl': p.lvl, 'XP': p.XP, 'maxXP': p.maxXP, 'job': p.job, 'p_class': p.p_class,
                'HPh': p.HPh, 'maxHP': p.maxHP, 'MPh': p.MPh, 'maxMP': p.maxMP, 'ENh': p.ENh, 'maxEN': p.maxEN,
                'Energy': p.Energy, 'Strength': p.Strength, 'Intellect': p.Intellect, 'Agility': p.Agility,
                'Accuracy': p.Accuracy, 'Luck': p.Luck, 'usp': p.usp, 'skills': p.skills, 'difficulty': p.difficulty,
                'main_location': p.main_location, 'location': p.location, 'c_names': c.c_names}


        return temp