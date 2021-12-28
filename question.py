import re


num_format = re.compile(r'^-?[0-9][0-9]*$')


class Questions:
    def __init__(self):
        # qsize is how many choices you have for your question
        self.qsize = 0
        self.p_location = 'Home'

    def checking_answer(self, user_input) -> bool:
        """This function is to check to make sure that the user
        inputs a number and checks to make sure that it is in
        range of how many choices you have. if it is an invalid
        input it returns false so the question can be asked again.
        if its true it will continue back to the main game to be
        processed."""
        it_is = re.match(num_format, user_input)
        if user_input == "":
            print('Missing input. Please try again.\n')
        elif it_is:
            if 0 < int(user_input) <= self.qsize:
                return True
            else:
                print('Out of range. Please try again.\n')
        else:
            print('Invalid input. Please try again.\n')
        return False

    def main_menu(self) -> str:
        """This is the main menu."""
        self.qsize = 4
        while True:
            print('(1) New Game')
            print('(2) Load Game')
            print('(3) Options')
            print('(4) Exit Game')
            user_input = input('Input: ')
            print('\n')
            if self.checking_answer(user_input):
                break
        return user_input

    def option_menu(self) -> str:
        """This is the option menu."""
        self.qsize = 2
        while True:
            print('(1) Difficultly selection')
            print('(2) Credits')
            user_input = input('Input: ')
            print('\n')
            if self.checking_answer(user_input):
                break
        return user_input

    def difficulty_s(self) -> int:
        self.qsize = 4
        while True:
            print("What difficulty will you chose?")
            print("(1) Easy")
            print("(2) Medium")
            print("(3) Hard")
            print("(4) Insane")
            user_input = input('Input: ')
            if self.checking_answer(user_input):
                break
        return int(user_input)

    def location(self) -> str:
        areas = ['Mountain', 'Forest', 'Dungeon', 'Plains']
        while True:
            print('Your Current location is ', self.p_location)
            print('Where would you like to travel to next: ')
            for each in areas:
                if self.p_location != each:
                    print(each)
            user_input = input("?: ")
            if user_input.lower() not in ['f', 'forest', 'm', 'mountain',
                                          'd', 'dungeon', 'p', 'plains', 'exit']:
                print('Incorrect Answer. Please try again')
                print('\n\n')
            else:
                if user_input.lower() in ['f', 'forest']:
                    dest = 'Forest'
                elif user_input.lower() in ['d', 'dungeon']:
                    dest = 'Dungeon'
                elif user_input.lower() in ['m', 'mountain']:
                    dest = 'Mountain'
                elif user_input.lower() in ['p', 'plains']:
                    dest = 'Plains'
                else:
                    return '0'
        print(f'You have decided to leave {self.p_location} and travel to {dest}')
        return user_input.lower()