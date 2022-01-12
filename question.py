import re


num_format = re.compile(r'^-?[0-9][0-9]*$')


class Questions:
    def __init__(self):
        # qsize is how many choices you have for your question
        self.qsize = 0
        self.p_location = 'Town'

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
            if -1 < int(user_input) <= self.qsize:
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
            print('(0) Main menu')
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

    def location(self) -> int:
        main_place=True
        while main_place==True:
            if self.p_location=='Campaign' or self.p_location=='Plains' or self.p_location=='Forest' or self.p_location=='Dungeon' or self.p_location=='Mountain':
                self.qsize = 5
                areas = ['Mountain', 'Forest', 'Dungeon', 'Plains', 'Town']
                main_location=1
                while True:
                    print('Your Current location is ', self.p_location)
                    print('Where would you like to travel to next:')
                    count = 0
                    for each in areas:
                        if self.p_location != each:
                            count += 1
                            print(f'({count}) {each}')
                        else:
                            count += 1
                            print(f'({count}) {each}*')
                    user_input = input("Input: ")
                    if self.checking_answer(user_input):
                        if user_input == 5:
                            main_location=2
                            main_place=True
                            self.p_location='Town'
                            break
                        if areas[int(user_input) - 1] == self.p_location:
                            print(f'Sorry you cannot choose {areas[int(user_input) - 1]} cause you are currently at that location')
                        else:
                            main_place=False
                            break
            elif self.p_location=='Town' or self.p_location=='Home' or self.p_location=='Shop' or self.p_location=='Guild' or self.p_location=='Arena':
                self.qsize = 5
                main_location=2
                areas = ['Home', 'Shop', 'Guild', 'Arena', 'Campaign']
                while True:
                    print('Your Current location is ', self.p_location)
                    print('Where would you like to travel to next:')
                    count = 0
                    for each in areas:
                        if self.p_location != each:
                            count += 1
                            print(f'({count}) {each}')
                        else:
                            count += 1
                            print(f'({count}) {each}*')
                    user_input = input("Input: ")
                    if self.checking_answer(user_input):
                        if int(user_input) == 5:
                            main_location=1
                            main_place=True
                            self.p_location='Campaign'
                            break
                        if areas[int(user_input) - 1] == self.p_location:
                            print(f'Sorry you cannot choose {areas[int(user_input) - 1]} cause you are currently at that location')
                        else:
                            main_place=False
                            break
        return int(user_input), main_location
