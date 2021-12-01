import json
from os.path import exists as file_exists


class GameData:
    """ This class will offer loading and saving of game data"""
    def __init__(self):
        self.file = 'RPGsave.txt'
        self.file_exists = bool(file_exists(self.file))

    def load_game(self, player_data: dict):
        if self.file_exists:
            with open(self.file, 'r') as user_data_file:
                user_data = json.load(user_data_file)
                print('Saved data has been loaded successfully!\n')
                return user_data
        else:  # don't need to initialize values -- already initialized when class created
            print('No saved data found...\n')
            print('Starting a fresh game...\n')

    def save_game(self, player_data: dict) -> None:
        if not self.file_exists:
            print("No previous save! Creating a new save...\n")

        with open(self.file, 'w') as user_data_file:
            json.dump(player_data, user_data_file)
