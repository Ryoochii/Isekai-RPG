import re


num_format = re.compile(r'^-?[0-9][0-9]*$')


class Questions:
    def __init__(self):
        self.qsize = 0

    def checking_answer(self, user_input) -> bool:
        it_is = re.match(num_format, user_input)
        if user_input == "":
            print('Missing input. Please try again.\n')
        elif it_is:
            if 0 < int(user_input) < self.qsize:
                return True
            else:
                print('Out of range. Please try again.\n')
        else:
            print('Invalid input. Please try again.\n')
        return False

    def main_menu(self) -> str:
        self.qsize = 5
        while True:
            print('(1) New Game')
            print('(2) Load Game')
            print('(3) Options')
            print('(4) Exit Game')
            user_input = input('?: ')
            if self.checking_answer(user_input):
                break
        return user_input

    def option_menu(self) -> str:
        # make sure you make qsize one number bigger then the amount
        # of questions you are asking
        self.qsize = 3
        while True:
            print('(1) Difficultly selection')
            print('(2) Credits')
            user_input = input('?: ')
            if self.checking_answer(user_input):
                break
        return user_input
