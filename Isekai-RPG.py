# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:04:35 2021

@author: nalaa019
"""


from player import Players
from gamedata import GameData
from creatures import Creatures
from question import Questions
import time
import sys
# from sys import exit

player1 = Players()
gamedata = GameData()
creatures = Creatures()
questions = Questions()
story = 1
difficulty = 1

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)

def print_speed(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(player1.text)
    sys.stdout.write('\n')

def new_game() -> None:
    player1.p_name = str(input("Welcome, what might your name be: "))
    print_speed(f"Welcome {player1.p_name}. I, the god of life, have decided to give you a second chance. \n"
          "I am going to send you to a world of swords and magic.\n"
          "Your goal is to reach level 100 and beat the demon lord. Good luck.")
    print()
    print_speed("The god sent you on your way. When you wake up, you realise you are an infant, \n"
          "unable to do anything. You then remember that the god told you to say status.")
    print_speed("(You pronounce the word status. A screen appears in front of you)")
    player1.display_info()
    player1.unassigned_points()
    return


def game(continu=0) -> None:
    guild_id="Unknown"
    if continu == 1:
        print_speed(f"Welcome back {player1.p_name}. Here are your stats!")
        player1.display_info()
        player1.unassigned_points()
        #We need to add guild id on the txt file
    print_speed("It is at that moment that you realised that this is the start of your adventure.")
    game_play = True
    while game_play:
        creatures.num_c()
        monster = creatures.num_cs
        questions.p_location = player1.location
        s_location, main_location = questions.location()
        if main_location==1:
            if s_location == 0:
                game_play=False
                return
            if s_location == 1:
                player1.location = 'Mountain'
                print_speed("You have set out on your adventure.")
                print_speed("You arrive at a beginner mountain known for it's weak monsters.")
                print_speed(f"While traveling, you get ambushed by a group of {monster} kobolds.")
            elif s_location == 2:
                player1.location = 'Forest'
                print_speed("You have set out on your adventure.")
                print_speed("You arrive at a dense forest known for it's weak monsters.")
                print_speed("In the forrest, you see a goblin encampment.")
                print_speed(f"After watching for a moment, you manage to see a total of {monster} goblins.")
            elif s_location == 3:
                player1.location = 'Dungeon'
                print_speed("You have set out on your adventure.")
                print_speed("You arrive at a dungeon where many beginners meet up to start a new adventure.")
                print_speed(f"While walking around in the dungeon, you find a small group of {monster} zombies.")
            elif s_location == 4:
                player1.location = 'Plains'
                print_speed("You have set out on your adventure.")
                print_speed("You arrive at a wide plain where you can easily perceive monsters.")
                print_speed(f"You perceive {monster} slimes and decide to engage in a combat.")
            elif s_location == 5:
                player1.location = 'Town'
            c_party = creatures.fight_party(player1.lvl)
            for k, v in c_party.items():
                print_speed(f"Name: {v['name']}")
            game_play = True
            print('\n\n\n')
        elif main_location==2:
            if s_location == 0:
                game_play=False
                return
            if s_location == 1:
                stay=1
                player1.location = 'Home'
                print_speed("You go home.")
                while stay==1:
                    action=str(input('Do you want to rest or do you want to rearrange your inventory and chest? '))
                    if action.lower() not in ['rest', 'r', 'inventory', 'i']:
                        print_speed('Incorrect answer. Please try again')
                    elif action.lower() in ['inventory', 'i']:
                        print_speed("Please rearrange your inventory.")
                        stay=0
                        #Need to have your inventory and chest where you can store things
                    else:
                        gamedata.set_save_data(player1, creatures)
                        print_speed("You arrive and your family has prepared a dinner for you.")
                        print_speed("You eat and head to your bed.")
                        player1.rest()
                        print_slow(".....")
                        print("Game saved!")
                        time.sleep(1)
                        print_speed("After a good meal and a good rest, you are back full of energy.")
                        stay=0
            elif s_location == 2:
                stay=1
                player1.location = 'Shop'
                print_speed("You go into a small shop.")
                print_speed("Welcome, what can I do for you?")
                while stay==1:
                    question=1
                    problem=1
                    while problem==1:
                        action=str(input("Would you like to sell or buy (Sell or Buy)? "))
                        if action.lower() not in ['sell', 's', 'buy', 'b']:
                            print_speed('Incorrect answer. Please try again')
                        elif action.lower() in ['sell', 's']:
                            print_speed("What do you want to sell?")
                            #Need to have your inventory with what you can sell and the prices
                            problem=0
                        else:
                            print_speed("What would you like to buy?")
                            problem=0
                            #Need to do a shop program or file that checks what items are left in stock and everything.
                    while question==1:
                        print_speed("Would you like to do something else?")
                        answer=str(input("Yes or No: "))
                        if answer.lower() not in ['yes', 'no', 'n', 'y']:
                            print_speed('Incorrect answer. Please try again')
                        elif answer.lower() in ['no', 'n']:
                            stay=0
                            question=0
                        else:
                            print_speed("What else can I do for you?")
                            question=0
                print_speed("Goodbye and be careful.")
            elif s_location == 3:
                player1.location = 'Guild'
                print_speed("You head into the guild")
                if guild_id=="Unknown":
                    print_speed("Welcome to the guild. Before registering, let me explain a little.")
                    print_speed("Guild id shows your rank. You get a new rank every ten levels: ")
                    print_speed("F=LVL1 to LVL10")
                    print_speed("E=LVL11 to LVL20")
                    print_speed("D=LVL21 to LVL30")
                    print_speed("C=LVL31 to LVL40")
                    print_speed("B=LVL41 to LVL50")
                    print_speed("A=LVL51 to LVL60")
                    print_speed("S=LVL61 to LVL70")
                    print_speed("SS=LVL71 to LVL MAX")
                    print_speed("The higher your rank, the more missions you can access."
                          "Lets assess your rank")
                    guild_id=player1.rank()
                    print_speed(f"Congratulations, you are officially a hunter of {guild_id} rank.")
                print_speed("Please choose a mission:")
                #Need to do a function in questions for all the missions
            elif s_location == 4:
                player1.location = 'Arena'
                print_speed("You go towards the arena.")
                read_rules=input("Welcome to the arena, would you like to read the rules? (Yes or No) ")
                if read_rules.lower() not in ['yes', 'no', 'n', 'y']:
                    print_speed('Incorrect answer. Please try again')
                elif read_rules.lower() in ['no', 'n']:
                    pass
                else:
                    print_speed("Welcome to the arena. The goal is to beat your opponent.")
                    print_speed("The opponents get stronger as it goes.")
                    print_speed("The further you make it in the matches, the better the rewards.")
                    #Gets gold for every opponent he beats and has a chance of obtaining an item or potion every 10 opponents
                print_speed("Good luck!")
            elif s_location == 5:
                player1.location = 'Adventure'
            
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
            speed_text()
        elif user_input == '3':
            print_speed('\n'
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

def speed_text() -> None:
    player1.text = questions.text_speed()
    return

if __name__ == '__main__':
    game_menu()
