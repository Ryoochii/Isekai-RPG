# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:04:35 2021

@author: nalaa019
"""


from player import Players
from gamedata import GameData
from creatures import Creatures
from question import Questions

# from sys import exit

player1 = Players()
gamedata = GameData()
creatures = Creatures()
questions = Questions()
story = 1
difficulty = 1


def new_game() -> None:
    player1.p_name = str(input("Welcome, what might your name be: "))
    print(f"Welcome {player1.p_name}. I, the god of life, have decided to give you a second chance. \n"
          "I am going to send you to a world of swords and magic.\n"
          "Your goal is to reach level 100 and beat the demon lord. Good luck.")
    print()
    print("The god sent you on your way. When you wake up, you realise you are an infant, \n"
          "unable to do anything. You then remember that the god told you to say status.")
    print("(You pronounce the word status. A screen appears in front of you)")
    player1.display_info()
    
    return


def game(continu=0) -> None:
    if continu == 1:
        print(f"Welcome back {player1.p_name}. Here are your stats!")
        player1.display_info()
    print("\nIt is at that moment that you realised that this is the start of your adventure.")
    game_play = True
    while game_play:
        creatures.num_c()
        monster = creatures.num_cs
        questions.p_location = player1.location
        s_location = questions.location()
        if s_location == 0:
            return
        if s_location == 1:
            player1.location = 'Mountain'
            print("You have set out on your adventure.")
            print("You arrive at a beginner mountain known for it's weak monsters.")
            print(f"While traveling, you get ambushed by a group of {monster} kobolds.")
        elif s_location == 2:
            player1.location = 'Forest'
            print("You have set out on your adventure.")
            print("You arrive at a dense forest known for it's weak monsters.")
            print("In the forrest, you see a goblin encampment.")
            print(f"After watching for a moment, you manage to see a total of {monster} goblins.")
        elif s_location == 3:
            player1.location = 'Dungeon'
            print("You have set out on your adventure.")
            print("You arrive at a dungeon where many beginners meet up to start a new adventure.")
            print(f"While walking around in the dungeon, you find a small group of {monster} zombies.")
        elif s_location == 4:
            player1.location = 'Plains'
            print("You have set out on your adventure.")
            print("You arrive at a wide plain where you can easily perceive monsters.")
            print(f"You perceive {monster} slimes and decide to engage in a combat.")
        elif s_location == 5:
            player1.location = 'Home'


        c_party = creatures.fight_party(player1.lvl)
        for k, v in c_party.items():
            print(f"Name: {v['name']}")
        game_play = True
        print('\n\n\n')
        gamedata.save_game(player1, creatures)
    return


def game_menu() -> None:
    while True:
        user_input = questions.main_menu()
        if user_input == '1':
            new_game()
            game()
        elif user_input == '2':
            if gamedata.load_game(player1, creatures):
                # Game data loaded successfully continuing with game
                game(1)
            else:
                # if saved data isnt present, a new game is started
                new_game()
                game()
        elif user_input == '3':
            options_menu()
        elif user_input == '4':
            break
    return


def options_menu() -> None:
    while True:
        user_input = questions.option_menu()
        if user_input == '1':
            difficulty_selection()
        elif user_input == '2':
            print('\n'
                  'Thank you for playing our game!''\n\n'
                  'Developers: \n'
                  'Navid Lahidji Hosseiny''\n'
                  'Adam Smith'
                  '\n\n\n')
        elif user_input == '0':
            break
    return


def difficulty_selection() -> None:
    player1.difficulty = questions.difficulty_s()
    return


if __name__ == '__main__':
    game_menu()
