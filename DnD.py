import random as rnd
from player import Players
from gamedata import GameData
from creatures import Creatures
from sys import exit

player1 = Players()
gamedata = GameData()
creatures = Creatures()
story = 1
difficulty=1

"""
def g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp):
    if lvl == 1 and XP >= maxXP:
        XP -= maxXP
        lvl += 1
        maxXP = 25
        s += 1
        intel += 1
        a += 1
        st += 1
        l += 1
        maxHP = 20
        HPh = maxHP
        maxMP = 20
        MPh = maxMP
        print("Level up")
        player1.dispaly_info()
        gamedata.save_game(player1)
    if lvl == 2 and XP >= maxXP:
        XP -= maxXP
        lvl = 3
        maxXP = 50
        s += 1
        intel += 1
        a += 1
        st += 1
        l += 1
        maxHP += 10
        HPh = maxHP
        maxMP += 10
        MPh = maxMP
        print("Level up")
        player1.dispaly_info()
        gamedata.save_game(player1)
    if lvl == 3 and XP >= maxXP:
        XP -= maxXP
        lvl = 4
        maxXP = 75
        s += 1
        intel += 1
        a += 1
        st += 1
        l += 1
        maxHP += 10
        HPh = maxHP
        maxMP += 10
        MPh = maxMP
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        save()
    while (3 < lvl < 10) and XP >= maxXP:
        XP -= maxXP
        lvl += 1
        maxXP = 100
        s += 1
        intel += 1
        a += 1
        st += 1
        l += 1
        maxHP += 10
        HPh = maxHP
        maxMP += 10
        MPh = maxMP
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        save()
    if lvl == 9 and XP >= maxXP:
        XP -= maxXP
        lvl += 1
        maxXP = 1000
        s += 10
        intel += 10
        a += 10
        st += 10
        l += 10
        maxHP += 100
        HPh = maxHP
        maxMP += 100
        MPh = maxMP
        usp += 10
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        print("You have received the skill: Watershot (5 mana, 3*intelligence on 1 creature)")
        Skills.append()
        print(f"Unassigned Stat Points: {usp}")
        h(s, usp, intel, a, st, l);
        save();
    if lvl == 10 and XP >= maxXP:
        XP -= maxXP
        lvl += 1
        maxXP = 100
        s += 2
        intel += 2
        a += 2
        st += 2
        l += 2
        maxHP += 100
        HPh = maxHP
        maxMP += 100
        MPh = maxMP
        usp += 3
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        print("You have received the skill: Watershot (5 mana, 3*intelligence on 1 creature)")
        Skills.append(", Watershot (5 mana, 3*intelligence on 1 creature)")
        print(f"Unassigned Stat Points: {usp}")
        h(s, usp, intel, a, st, l);
        save();
    return (lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)



if story == 1:
    if lvl == 1:
    while lvl < 10:
        if HPh <= 0:
            break
        save()
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 'Forest':
            d = 0
            c = 0
            b = 0
            gob = rnd.randint(3, 6)
            if gob >= 3:
                gob1 = HPg
                gob2 = HPg
                gob3 = HPg
            if gob >= 6:
                gob6 = HPg
                d = 1
            if gob >= 5:
                gob5 = HPg
                c = 1
            if gob == 4:
                gob4 = HPg
                b = 1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to a forest.")
            print("You arrive at a dense forrest known for it's weak monsters.")
            print("In the forrest, you see a goblin encampment.")
            print(f"After watching for a moment, you manage to see a total of {gob} goblins.")
            while gob > 0:
                if classes == 1:
                    attack = str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                    if attack == 'Fireball' and MPh >= 2:
                        MPh -= 2
                        if l < 10:
                            gob1 = gob1 - 2 * intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                gob1 = gob1 - 4 * intel
                                print(
                                    "You stumbled and shot a bit lower, the goblin tried avoiding your spell but the fireball hit the goblin in his face and did double the damage!")
                            else:
                                gob1 = gob1 - 2 * intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                gob1 = gob1 - 4 * intel
                                print(
                                    "You stumbled and shot a bit lower, the goblin tried avoiding your spell but the fireball hit the goblin in his face and did double the damage!")
                            else:
                                gob1 = gob1 - 2 * intel
                        if gob1 <= 0:
                            print("Congratulations, you have killed a goblin. You received 7XP")
                            XP += 7
                            gob -= 1
                            if gob == 5:
                                d -= 1
                                gob1 = gob6
                            if gob == 4:
                                c -= 1
                                gob1 = gob5
                            if gob == 3:
                                b -= 1
                                gob1 = gob4
                            if gob == 2:
                                gob1 = gob3
                            if gob == 1:
                                gob1 = gob2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif gob1 > 0:
                            print(f"The goblin has {gob1} remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = gob * 10
                        elif 0 < ac < 10:
                            at = gob * 1
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
                    elif attack == 'Heal' and MPh >= 3:
                        HPh += 50
                        MPh -= 3
                        if HPh > maxHP:
                            HPh = maxHP
                        else:
                            HPh = HPh
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = gob * 10
                        elif 0 < ac < 10:
                            at = gob * 1
                        HPh -= at
                        print(f'HP: {HPh}')
                    elif attack == 'Electrocute' and MPh >= 3:
                        MPh -= 3
                        if d == 1:
                            if l < 10:
                                gob6 = gob6 - intel
                                gob5 = gob5 - intel
                                gob4 = gob4 - intel
                                gob3 = gob3 - intel
                                gob2 = gob2 - intel
                                gob1 = gob1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    gob6 = gob6 - 2 * intel
                                    gob5 = gob5 - 2 * intel
                                    gob4 = gob4 - 2 * intel
                                    gob3 = gob3 - 2 * intel
                                    gob2 = gob2 - 2 * intel
                                    gob1 = gob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob6 = gob6 - intel
                                    gob5 = gob5 - intel
                                    gob4 = gob4 - intel
                                    gob3 = gob3 - intel
                                    gob2 = gob2 - intel
                                    gob1 = gob1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    gob6 = gob6 - 2 * intel
                                    gob5 = gob5 - 2 * intel
                                    gob4 = gob4 - 2 * intel
                                    gob3 = gob3 - 2 * intel
                                    gob2 = gob2 - 2 * intel
                                    gob1 = gob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob6 = gob6 - intel
                                    gob5 = gob5 - intel
                                    gob4 = gob4 - intel
                                    gob3 = gob3 - intel
                                    gob2 = gob2 - intel
                                    gob1 = gob1 - intel
                            if gob6 <= 0:
                                print("Congratulations, you have killed 6 goblins. You received 42XP")
                                XP += 42
                                gob -= 6
                                gob1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif gob1 <= 0:
                                print("Congratulations, you have killed a goblin. You received 7XP")
                                XP += 7
                                gob -= 1
                                if gob == 5:
                                    d -= 1
                                    gob1 = gob6
                                if gob == 4:
                                    c -= 1
                                    gob1 = gob5
                                if gob == 3:
                                    b -= 1
                                    gob1 = gob4
                                if gob == 2:
                                    gob1 = gob3
                                if gob == 1:
                                    gob1 = gob2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif c == 1:
                            if l < 10:
                                gob5 = gob5 - intel
                                gob4 = gob4 - intel
                                gob3 = gob3 - intel
                                gob2 = gob2 - intel
                                gob1 = gob1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    gob5 = gob5 - 2 * intel
                                    gob4 = gob4 - 2 * intel
                                    gob3 = gob3 - 2 * intel
                                    gob2 = gob2 - 2 * intel
                                    gob1 = gob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob5 = gob5 - intel
                                    gob4 = gob4 - intel
                                    gob3 = gob3 - intel
                                    gob2 = gob2 - intel
                                    gob1 = gob1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    gob5 = gob5 - 2 * intel
                                    gob4 = gob4 - 2 * intel
                                    gob3 = gob3 - 2 * intel
                                    gob2 = gob2 - 2 * intel
                                    gob1 = gob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob5 = gob5 - intel
                                    gob4 = gob4 - intel
                                    gob3 = gob3 - intel
                                    gob2 = gob2 - intel
                                    gob1 = gob1 - intel
                            if gob5 <= 0:
                                print("Congratulations, you have killed 5 goblins. You received 35XP")
                                XP += 35
                                gob -= 5
                                gob1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif gob1 <= 0:
                                print("Congratulations, you have killed a goblin. You received 7XP")
                                XP += 7
                                gob -= 1
                                if gob == 5:
                                    d -= 1
                                    gob1 = gob6
                                if gob == 4:
                                    c -= 1
                                    gob1 = gob5
                                if gob == 3:
                                    b -= 1
                                    gob1 = gob4
                                if gob == 2:
                                    gob1 = gob3
                                if gob == 1:
                                    gob1 = gob2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 1:
                            if l < 10:
                                gob4 = gob4 - intel
                                gob3 = gob3 - intel
                                gob2 = gob2 - intel
                                gob1 = gob1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    gob4 = gob4 - 2 * intel
                                    gob3 = gob3 - 2 * intel
                                    gob2 = gob2 - 2 * intel
                                    gob1 = gob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob4 = gob4 - intel
                                    gob3 = gob3 - intel
                                    gob2 = gob2 - intel
                                    gob1 = gob1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    gob4 = gob4 - 2 * intel
                                    gob3 = gob3 - 2 * intel
                                    gob2 = gob2 - 2 * intel
                                    gob1 = gob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob4 = gob4 - intel
                                    gob3 = gob3 - intel
                                    gob2 = gob2 - intel
                                    gob1 = gob1 - intel
                            if gob4 <= 0:
                                print("Congratulations, you have killed 4 goblins. You received 28XP")
                                XP += 28
                                gob -= 4
                                gob1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif gob1 <= 0:
                                print("Congratulations, you have killed a goblin. You received 7XP")
                                XP += 7
                                gob -= 1
                                if gob == 5:
                                    d -= 1
                                    gob1 = gob6
                                if gob == 4:
                                    c -= 1
                                    gob1 = gob5
                                if gob == 3:
                                    b -= 1
                                    gob1 = gob4
                                if gob == 2:
                                    gob1 = gob3
                                if gob == 1:
                                    gob1 = gob2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 0 and c == 0 and d == 0:
                            if gob == 3:
                                if l < 10:
                                    gob3 = gob3 - intel
                                    gob2 = gob2 - intel
                                    gob1 = gob1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        gob3 = gob3 - 2 * intel
                                        gob2 = gob2 - 2 * intel
                                        gob1 = gob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob3 = gob3 - intel
                                        gob2 = gob2 - intel
                                        gob1 = gob1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        gob3 = gob3 - 2 * intel
                                        gob2 = gob2 - 2 * intel
                                        gob1 = gob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob3 = gob3 - intel
                                        gob2 = gob2 - intel
                                        gob1 = gob1 - intel
                                if gob1 <= 0:
                                    print("Congratulations, you have killed 3 goblins. You received 21XP")
                                    XP += 21
                                    gob -= 3
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif gob1 <= 0:
                                    print("Congratulations, you have killed a goblin. You received 7XP")
                                    XP += 7
                                    gob -= 1
                                    if gob == 5:
                                        d -= 1
                                        gob1 = gob6
                                    if gob == 4:
                                        c -= 1
                                        gob1 = gob5
                                    if gob == 3:
                                        b -= 1
                                        gob1 = gob4
                                    if gob == 2:
                                        gob1 = gob3
                                    if gob == 1:
                                        gob1 = gob2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            if gob == 2:
                                if l < 10:
                                    gob1 -= intel
                                    gob2 = gob2 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        gob1 = gob1 - 2 * intel
                                        gob2 = gob2 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1 -= intel
                                        gob2 = gob2 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        gob1 = gob1 - 2 * intel
                                        gob2 = gob2 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1 -= intel
                                        gob2 = gob2 - intel
                                if gob2 <= 0:
                                    print("Congratulations, you have killed 2 goblins. You received 14XP")
                                    XP += 14
                                    gob -= 2
                                    gob2 = gob1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif gob1 <= 0:
                                    print("Congratulations, you have killed a goblin. You received 7XP")
                                    XP += 7
                                    gob -= 1
                                    if gob == 5:
                                        d -= 1
                                        gob1 = gob6
                                    if gob == 4:
                                        c -= 1
                                        gob1 = gob5
                                    if gob == 3:
                                        b -= 1
                                        gob1 = gob4
                                    if gob == 2:
                                        gob1 = gob3
                                    if gob == 1:
                                        gob1 = gob2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            if gob == 1:
                                if l < 10:
                                    gob1 = gob1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        gob1 = gob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1 = gob1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        gob1 = gob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1 -= intel
                                if gob1 <= 0:
                                    print("Congratulations, you have killed a goblin. You received 7XP")
                                    XP += 7
                                    gob -= 1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                        if gob1 > 0:
                            print(f"The goblin has {gob1}HP remaining")
                            if gob > 1:
                                print(f"The other goblins have {gob2}HP remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = gob * 10
                        elif 0 < ac < 10:
                            at = gob * 1
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
                    elif attack == 'Hit':
                        if l < 10:
                            gob1 = gob1 - s
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                gob1 = gob1 - 2 * s
                                print("You hit the goblin in the eye! It did double the damage!!")
                            else:
                                gob1 = gob1 - s
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                gob1 = gob1 - 2 * s
                                print("You hit the goblin in the eye! It did double the damage!")
                            else:
                                gob1 = gob1 - s
                        if gob1 <= 0:
                            print("Congratulations, you have killed a goblin. You received 7XP")
                            XP += 7
                            gob -= 1
                            if gob == 5:
                                d -= 1
                                gob1 = gob6
                            if gob == 4:
                                c -= 1
                                gob1 = gob5
                            if gob == 3:
                                b -= 1
                                gob1 = gob4
                            if gob == 2:
                                gob1 = gob3
                            if gob == 1:
                                gob1 = gob2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif gob1 > 0:
                            print(f"The goblin has {gob1} remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = gob * 10
                        elif 0 < ac < 10:
                            at = gob * 1
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
        elif story_2 == 'Mountain':
            kob = rnd.randint(3, 6)
            d = 0
            c = 0
            b = 0
            if kob >= 3:
                kob1 = HPkobolds
                kob2 = HPkobolds
                kob3 = HPkobolds
            if kob >= 6:
                kob6 = HPkobolds
                kob5 = HPkobolds
                kob4 = HPkobolds
                d = 1
            if kob >= 5:
                kob5 = HPkobolds
                kob4 = HPkobolds
                c = 1
            if kob == 4:
                kob4 = HPkobolds
                b = 1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to the mountains.")
            print("You arrive at a beginner mountain known for it's weak monsters.")
            print(f"While traveling, you get ambushed by a group of {kob} kobolts.")
            while kob > 0:
                if classes == 1:
                    attack = str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                    if attack == 'Fireball' and MPh >= 2:
                        MPh -= 2
                        if l < 10:
                            kob1 = kob1 - 2 * intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                kob1 = kob1 - 4 * intel
                                print(
                                    "The kobold tried to avoid your spell but ran into a wall, you having missed by little you spell, the fireball hit directly the kobold in his face and did double the damage!")
                            else:
                                kob1 = kob1 - 2 * intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                kob1 = kob1 - 4 * intel
                                print(
                                    "The kobold tried to avoid your spell but ran into a wall, you having missed by little you spell, the fireball hit directly the kobold in his face and did double the damage!")
                            else:
                                kob1 = kob1 - 2 * intel
                        if kob1 <= 0:
                            print("Congratulations, you have killed a Kobold. You received 15XP")
                            XP += 15
                            kob -= 1
                            if kob == 5:
                                d -= 1
                                kob1 = kob6
                            if kob == 4:
                                c -= 1
                                kob1 = kob5
                            if kob == 3:
                                b -= 1
                                kob1 = kob4
                            if kob == 2:
                                kob1 = kob3
                            if kob == 1:
                                kob1 = kob2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif kob1 > 0:
                            print(f"The kobold has {kob1} remaining")
                        ac = rnd.randint(1, 20)
                        if ac == 20:
                            at = kob * 15
                        elif 0 < ac < 20:
                            at = kob * 3
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
                    elif attack == 'Heal' and MPh >= 3:
                        HPh += 50
                        MPh -= 3
                        if HPh > maxHP:
                            HPh = maxHP
                        else:
                            HPh = HPh
                        ac = rnd.randint(1, 20)
                        if ac == 20:
                            at = kob * 15
                        elif 0 < ac < 20:
                            at = kob * 3
                        HPh -= at
                        print(f'HP: {HPh}')
                    elif attack == 'Electrocute' and MPh >= 3:
                        MPh -= 3
                        if d == 1:
                            if l < 10:
                                kob6 = kob6 - intel
                                kob5 = kob5 - intel
                                kob4 = kob4 - intel
                                kob3 = kob3 - intel
                                kob2 = kob2 - intel
                                kob1 = kob1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    kob6 = kob6 - 2 * intel
                                    kob5 = kob5 - 2 * intel
                                    kob4 = kob4 - 2 * intel
                                    kob3 = kob3 - 2 * intel
                                    kob2 = kob2 - 2 * intel
                                    kob1 = kob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob6 = kob6 - intel
                                    kob5 = kob5 - intel
                                    kob4 = kob4 - intel
                                    kob3 = kob3 - intel
                                    kob2 = kob2 - intel
                                    kob1 = kob1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    kob6 = kob6 - 2 * intel
                                    kob5 = kob5 - 2 * intel
                                    kob4 = kob4 - 2 * intel
                                    kob3 = kob3 - 2 * intel
                                    kob2 = kob2 - 2 * intel
                                    kob1 = kob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob6 = kob6 - intel
                                    kob5 = kob5 - intel
                                    kob4 = kob4 - intel
                                    kob3 = kob3 - intel
                                    kob2 = kob2 - intel
                                    kob1 = kob1 - intel
                            if kob6 <= 0:
                                print("Congratulations, you have killed 6 kobolds. You received 90XP")
                                XP += 90
                                kob -= 6
                                kob1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif kob1 <= 0:
                                print("Congratulations, you have killed a Kobold. You received 15XP")
                                XP += 15
                                kob -= 1
                                if kob == 5:
                                    d -= 1
                                    kob1 = kob6
                                if kob == 4:
                                    c -= 1
                                    kob1 = kob5
                                if kob == 3:
                                    b -= 1
                                    kob1 = kob4
                                if kob == 2:
                                    kob1 = kob3
                                if kob == 1:
                                    kob1 = kob2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif c == 1:
                            if l < 10:
                                kob5 = kob5 - intel
                                kob4 = kob4 - intel
                                kob3 = kob3 - intel
                                kob2 = kob2 - intel
                                kob1 = kob1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    kob5 = kob5 - 2 * intel
                                    kob4 = kob4 - 2 * intel
                                    kob3 = kob3 - 2 * intel
                                    kob2 = kob2 - 2 * intel
                                    kob1 = kob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob5 = kob5 - intel
                                    kob4 = kob4 - intel
                                    kob3 = kob3 - intel
                                    kob2 = kob2 - intel
                                    kob1 = kob1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    kob5 = kob5 - 2 * intel
                                    kob4 = kob4 - 2 * intel
                                    kob3 = kob3 - 2 * intel
                                    kob2 = kob2 - 2 * intel
                                    kob1 = kob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob5 = kob5 - intel
                                    kob4 = kob4 - intel
                                    kob3 = kob3 - intel
                                    kob2 = kob2 - intel
                                    kob1 = kob1 - intel
                            if kob5 <= 0:
                                print("Congratulations, you have killed 5 kobolds. You received 75XP")
                                XP += 75
                                kob -= 5
                                kob1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif kob1 <= 0:
                                print("Congratulations, you have killed a Kobold. You received 15XP")
                                XP += 15
                                kob -= 1
                                if kob == 5:
                                    d -= 1
                                    kob1 = kob6
                                if kob == 4:
                                    c -= 1
                                    kob1 = kob5
                                if kob == 3:
                                    b -= 1
                                    kob1 = kob4
                                if kob == 2:
                                    kob1 = kob3
                                if kob == 1:
                                    kob1 = kob2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 1:
                            if l < 10:
                                kob4 = kob4 - intel
                                kob3 = kob3 - intel
                                kob2 = kob2 - intel
                                kob1 = kob1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    kob4 = kob4 - 2 * intel
                                    kob3 = kob3 - 2 * intel
                                    kob2 = kob2 - 2 * intel
                                    kob1 = kob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob4 = kob4 - intel
                                    kob3 = kob3 - intel
                                    kob2 = kob2 - intel
                                    kob1 = kob1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    kob4 = kob4 - 2 * intel
                                    kob3 = kob3 - 2 * intel
                                    kob2 = kob2 - 2 * intel
                                    kob1 = kob1 - 2 * intel
                                    print(
                                        "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob4 = kob4 - intel
                                    kob3 = kob3 - intel
                                    kob2 = kob2 - intel
                                    kob1 = kob1 - intel
                            if kob4 <= 0:
                                print("Congratulations, you have killed 4 kobolds. You received 60XP")
                                XP += 60
                                kob -= 4
                                kob1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif kob1 <= 0:
                                print("Congratulations, you have killed a Kobold. You received 15XP")
                                XP += 15
                                kob -= 1
                                if kob == 5:
                                    d -= 1
                                    kob1 = kob6
                                if kob == 4:
                                    c -= 1
                                    kob1 = kob5
                                if kob == 3:
                                    b -= 1
                                    kob1 = kob4
                                if kob == 2:
                                    kob1 = kob3
                                if kob == 1:
                                    kob1 = kob2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 0 and c == 0 and d == 0:
                            if kob == 3:
                                if l < 10:
                                    kob3 = kob3 - intel
                                    kob2 = kob2 - intel
                                    kob1 = kob1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        kob3 = kob3 - 2 * intel
                                        kob2 = kob2 - 2 * intel
                                        kob1 = kob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob3 = kob3 - intel
                                        kob2 = kob2 - intel
                                        kob1 = kob1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        kob3 = kob3 - 2 * intel
                                        kob2 = kob2 - 2 * intel
                                        kob1 = kob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob3 = kob3 - intel
                                        kob2 = kob2 - intel
                                        kob1 = kob1 - intel
                                if kob3 <= 0:
                                    print("Congratulations, you have killed 3 kobolds. You received 45XP")
                                    XP += 45
                                    kob -= 3
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif kob1 <= 0:
                                    print("Congratulations, you have killed a Kobold. You received 15XP")
                                    XP += 15
                                    kob -= 1
                                    if kob == 5:
                                        d -= 1
                                        kob1 = kob6
                                    if kob == 4:
                                        c -= 1
                                        kob1 = kob5
                                    if kob == 3:
                                        b -= 1
                                        kob1 = kob4
                                    if kob == 2:
                                        kob1 = kob3
                                    if kob == 1:
                                        kob1 = kob2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            elif kob == 2:
                                if l < 10:
                                    kob1 = kob1 - intel
                                    kob2 = kob2 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        kob1 = kob1 - 2 * intel
                                        kob2 = kob2 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1 = kob1 - intel
                                        kob2 = kob2 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        kob1 = kob1 - 2 * intel
                                        kob2 = kob2 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1 = kob1 - intel
                                        kob2 = kob2 - intel
                                if kob2 <= 0:
                                    print("Congratulations, you have killed 2 kobolds. You received 30XP")
                                    XP += 30
                                    kob -= 2
                                    kob2 -= intel
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif kob1 <= 0:
                                    print("Congratulations, you have killed a Kobold. You received 15XP")
                                    XP += 15
                                    kob -= 1
                                    kob1 = kob2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            elif kob == 1:
                                if l < 10:
                                    kob1 = kob1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        kob1 = kob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1 = kob1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        kob1 = kob1 - 2 * intel
                                        print(
                                            "You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1 = kob1 - intel
                                if kob1 <= 0:
                                    print("Congratulations, you have killed a kobold. You received 15XP")
                                    XP += 15
                                    kob -= 1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                        if kob1 > 0:
                            print(f"The kobold has {kob1}HP remaining")
                            if kob > 1:
                                print(f"The other kobolds have {kob2}HP remaining")
                        ac = rnd.randint(1, 20)
                        if ac == 20:
                            at = kob * 15
                        elif 0 < ac < 20:
                            at = kob * 3
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
                    elif attack == 'Hit':
                        if l < 10:
                            kob1 = kob1 - s
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                kob1 = kob1 - 2 * s
                                print("You hit the kobold in the muzzle! It did double the damage!!")
                            else:
                                kob1 = kob1 - s
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                kob1 = kob1 - 2 * s
                                print("You hit the goblin in the muzzle! It did double the damage!")
                            else:
                                kob1 = kob1 - s
                        if kob1 <= 0:
                            print("Congratulations, you have killed a Kobold. You received 15XP")
                            XP += 15
                            kob -= 1
                            if kob == 5:
                                d -= 1
                                kob1 = kob6
                            if kob == 4:
                                c -= 1
                                kob1 = kob5
                            if kob == 3:
                                b -= 1
                                kob1 = kob4
                            if kob == 2:
                                kob1 = kob3
                            if kob == 1:
                                kob1 = kob2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif kob1 > 0:
                            print(f"The kobold has {kob1} remaining")
                        ac = rnd.randint(1, 20)
                        if ac == 20:
                            at = kob * 15
                        elif 0 < ac < 20:
                            at = kob * 3
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
        elif story_2 == 'Dungeon':
            zomb = rnd.randint(3, 6)
            d = 0
            c = 0
            b = 0
            if zomb >= 3:
                zomb1 = HPzombie
                zomb2 = HPzombie
                zomb3 = HPzombie
            if zomb >= 6:
                zomb6 = HPzombie
                zomb5 = HPzombie
                zomb4 = HPzombie
                d = 1
            elif zomb >= 5:
                zomb5 = HPzombie
                zomb4 = HPzombie
                c = 1
            elif zomb == 4:
                zomb4 = HPzombie
                b = 1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to a beginner dungeon.")
            print("You arrive at a dungeon where many beginners meet up to start a new adventure.")
            print(f"While walking around in the dungeon, you find a small group of {zomb} zombies.")
            while zomb > 0:
                if classes == 1:
                    attack = str(input(f"What attack will you use first? {Skills}: "))
                    if attack == 'Fireball' and MPh >= 2:
                        MPh -= 2
                        if l < 10:
                            zomb1 = zomb1 - 2 * intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                zomb1 = zomb1 - 4 * intel
                                print(
                                    "The zombie tried to run away and hide behind a corner. Unfortunately for it, by running away, it ran exactly in the trajectory of your fireball and it hit for twice the damage!")
                            else:
                                zomb1 = zomb1 - 2 * intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                zomb1 = zomb1 - 4 * intel
                                print(
                                    "The zombie tried to run away and hide behind a corner. Unfortunately for it, by running away, it ran exactly in the trajectory of your fireball and it hit for twice the damage!")
                            else:
                                zomb1 = zomb1 - 2 * intel
                        if zomb1 <= 0:
                            print("Congratulations, you have killed a zombie. You received 10XP")
                            XP += 10
                            zomb -= 1
                            if zomb <= 5:
                                d -= 1
                                zomb1 = zomb6
                            if zomb <= 4:
                                c -= 1
                                zomb1 = zomb5
                            if zomb <= 3:
                                b -= 1
                                zomb1 = zomb4
                            if zomb == 2:
                                zomb1 = zomb3
                            if zomb == 1:
                                zomb1 = zomb2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif gob1 > 0:
                            print(f"The zombie has {zomb1} remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = zomb * 12
                        elif 0 < ac < 10:
                            at = zomb * 2
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
                    elif attack == 'Heal' and MPh >= 3:
                        HPh += 50
                        MPh -= 3
                        if HPh > maxHP:
                            HPh = maxHP
                        else:
                            HPh = HPh
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = zomb * 12
                        elif 0 < ac < 10:
                            at = zomb * 2
                        HPh -= at
                        print(f'HP: {HPh}')
                    elif attack == 'Electrocute' and MPh >= 3:
                        MPh -= 3
                        if d == 1:
                            if l < 10:
                                zomb6 = zomb6 - intel
                                zomb5 = zomb5 - intel
                                zomb4 = zomb4 - intel
                                zomb3 = zomb3 - intel
                                zomb2 = zomb2 - intel
                                zomb1 = zomb1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    zomb6 = zomb6 - 2 * intel
                                    zomb5 = zomb5 - 2 * intel
                                    zomb4 = zomb4 - 2 * intel
                                    zomb3 = zomb3 - 2 * intel
                                    zomb2 = zomb2 - 2 * intel
                                    zomb1 = zomb1 - 2 * intel
                                    print(
                                        "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                else:
                                    zomb6 = zomb6 - intel
                                    zomb5 = zomb5 - intel
                                    zomb4 = zomb4 - intel
                                    zomb3 = zomb3 - intel
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    zomb6 = zomb6 - 2 * intel
                                    zomb5 = zomb5 - 2 * intel
                                    zomb4 = zomb4 - 2 * intel
                                    zomb3 = zomb3 - 2 * intel
                                    zomb2 = zomb2 - 2 * intel
                                    zomb1 = zomb1 - 2 * intel
                                    print(
                                        "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                else:
                                    zomb6 = zomb6 - intel
                                    zomb5 = zomb5 - intel
                                    zomb4 = zomb4 - intel
                                    zomb3 = zomb3 - intel
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                            if zomb6 <= 0:
                                print("Congratulations, you have killed 6 zombies. You received 60XP")
                                XP += 60
                                zomb -= 6
                                zomb1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif c == 1:
                            if l < 10:
                                zomb5 = zomb5 - intel
                                zomb4 = zomb4 - intel
                                zomb3 = zomb3 - intel
                                zomb2 = zomb2 - intel
                                zomb1 = zomb1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    zomb5 = zomb5 - 2 * intel
                                    zomb4 = zomb4 - 2 * intel
                                    zomb3 = zomb3 - 2 * intel
                                    zomb2 = zomb2 - 2 * intel
                                    zomb1 = zomb1 - 2 * intel
                                    print(
                                        "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                else:
                                    zomb5 = zomb5 - intel
                                    zomb4 = zomb4 - intel
                                    zomb3 = zomb3 - intel
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    zomb5 = zomb5 - 2 * intel
                                    zomb4 = zomb4 - 2 * intel
                                    zomb3 = zomb3 - 2 * intel
                                    zomb2 = zomb2 - 2 * intel
                                    zomb1 = zomb1 - 2 * intel
                                    print(
                                        "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                else:
                                    zomb5 = zomb5 - intel
                                    zomb4 = zomb4 - intel
                                    zomb3 = zomb3 - intel
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                            if zomb5 <= 0:
                                print("Congratulations, you have killed 5 zombies. You received 50XP")
                                XP += 50
                                zomb -= 5
                                zomb1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 1:
                            if l < 10:
                                zomb4 = zomb4 - intel
                                zomb3 = zomb3 - intel
                                zomb2 = zomb2 - intel
                                zomb1 = zomb1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    zomb4 = zomb4 - 2 * intel
                                    zomb3 = zomb3 - 2 * intel
                                    zomb2 = zomb2 - 2 * intel
                                    zomb1 = zomb1 - 2 * intel
                                    print(
                                        "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                else:
                                    zomb4 = zomb4 - intel
                                    zomb3 = zomb3 - intel
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    zomb4 = zomb4 - 2 * intel
                                    zomb3 = zomb3 - 2 * intel
                                    zomb2 = zomb2 - 2 * intel
                                    zomb1 = zomb1 - 2 * intel
                                    print(
                                        "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                else:
                                    zomb4 = zomb4 - intel
                                    zomb3 = zomb3 - intel
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                            if zomb4 <= 0:
                                print("Congratulations, you have killed 4 zombies. You received 40XP")
                                XP += 40
                                zomb -= 4
                                zomb1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 0 and c == 0 and d == 0:
                            if zomb == 3:
                                if l < 10:
                                    zomb3 = zomb3 - intel
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        zomb3 = zomb3 - 2 * intel
                                        zomb2 = zomb2 - 2 * intel
                                        zomb1 = zomb1 - 2 * intel
                                        print(
                                            "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                    else:
                                        zomb3 = zomb3 - intel
                                        zomb2 = zomb2 - intel
                                        zomb1 = zomb1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        zomb3 = zomb3 - 2 * intel
                                        zomb2 = zomb2 - 2 * intel
                                        zomb1 = zomb1 - 2 * intel
                                        print(
                                            "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                    else:
                                        zomb3 = zomb3 - intel
                                        zomb2 = zomb2 - intel
                                        zomb1 = zomb1 - intel
                                if zomb3 <= 0:
                                    print("Congratulations, you have killed 3 zombies. You received 30XP")
                                    XP += 30
                                    zomb -= 3
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            if zomb == 2:
                                if l < 10:
                                    zomb2 = zomb2 - intel
                                    zomb1 = zomb1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        zomb2 = zomb2 - 2 * intel
                                        zomb1 = zomb1 - 2 * intel
                                        print(
                                            "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                    else:
                                        zomb2 = zomb2 - intel
                                        zomb1 = zomb1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        zomb2 = zomb2 - 2 * intel
                                        zomb1 = zomb1 - 2 * intel
                                        print(
                                            "The zombies getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                    else:
                                        zomb2 = zomb2 - intel
                                        zomb1 = zomb1 - intel
                                if zomb1 <= 0:
                                    print("Congratulations, you have killed 2 zombies. You received 20XP")
                                    XP += 20
                                    zomb -= 2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            if zomb == 1:
                                if l < 10:
                                    zomb1 = zomb1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        zomb1 = zomb1 - 2 * intel
                                        print(
                                            "The zombie getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                    else:
                                        zomb1 = zomb1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        zomb1 = zomb1 - 2 * intel
                                        print(
                                            "The zombie getting scared by the electric feeling, tried to run away but fell in a puddle! It did twice the damage!")
                                    else:
                                        zomb1 = zomb1 - intel
                                if zomb1 <= 0:
                                    print("Congratulations, you have killed a zombie. You received 10XP")
                                    XP += 10
                                    zomb -= 1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                        if zomb1 > 0:
                            print(f"The zombie has {zomb1}HP remaining")
                            if zomb > 1:
                                print(f"The other zombies have {zomb2}HP remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = zomb * 12
                        elif 0 < ac < 10:
                            at = zomb * 2
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
                    if attack == 'Hit':
                        if l < 10:
                            zomb1 = zomb1 - s
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                zomb1 = zomb1 - 2 * s
                                print("You hit the zombie right through his flesh dealing double the damage!")
                            else:
                                zomb1 = zomb1 - s
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                zomb1 = zomb1 - 2 * s
                                print("You hit the zombie right through his flesh dealing double the damage!")
                            else:
                                zomb1 = zomb1 - s
                        if zomb1 <= 0:
                            print("Congratulations, you have killed a zombie. You received 10XP")
                            XP += 10
                            zomb -= 1
                            if zomb <= 5:
                                d -= 1
                                zomb1 = zomb6
                            if zomb <= 4:
                                c -= 1
                                zomb1 = zomb5
                            if zomb <= 3:
                                b -= 1
                                zomb1 = zomb4
                            if zomb == 2:
                                zomb1 = zomb3
                            if zomb == 1:
                                zomb1 = zomb2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif zomb1 > 0:
                            print(f"The zombie has {zomb1} remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = zomb * 12
                        elif 0 < ac < 10:
                            at = zomb * 2
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
        elif story_2 == 'Plains':
            slime = rnd.randint(6, 9)
            d = 0
            c = 0
            b = 0
            if slime >= 6:
                slime1 = HPslime
                slime2 = HPslime
                slime3 = HPslime
                slime4 = HPslime
                slime5 = HPslime
                slime6 = HPslime
            if slime >= 9:
                slime9 = HPslime
                slime8 = HPslime
                slime7 = HPslime
                d = 1
            elif slime >= 8:
                slime8 = HPslime
                slime7 = HPslime
                c = 1
            elif slime == 7:
                slime7 = HPslime
                b = 1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to a plain.")
            print("You arrive at a wide plain where you can easily perceive monsters.")
            print(f"You perceive {slime} slimes. You engage in a combat.")
            while slime > 0:
                if classes == 1:
                    attack = str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                    if attack == 'Fireball' and MPh >= 2:
                        slime1 -= 2 * intel
                        MPh -= 2
                        if slime1 <= 0:
                            print("Congratulations, you have killed a slime. You received 2XP")
                            XP += 2
                            slime -= 1
                            if slime == 8:
                                d -= 1
                                slime1 = slime9
                            if slime == 7:
                                c -= 1
                                slime1 = slime8
                            if slime == 6:
                                b -= 1
                                slime1 = slime7
                            if slime == 5:
                                slime1 = slime6
                            if slime == 4:
                                slime1 = slime5
                            if slime == 3:
                                slime1 = slime4
                            if slime == 2:
                                slime1 = slime3
                            if slime1 == 1:
                                slime1 = slime2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif slime1 > 0:
                            print(f"The slime has {slime1}HP remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = slime * 5
                        elif 0 < ac < 10:
                            if slime == 2 or slime == 4 or slime == 6 or slime == 8:
                                at = slime * 0.5
                            else:
                                at = (slime * 0.5) + 0.5
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
                    elif attack == 'Heal' and MPh >= 3:
                        HPh += 50
                        MPh -= 3
                        if HPh > maxHP:
                            HPh = maxHP
                        else:
                            HPh = HPh
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = slime * 5
                        elif 0 < ac < 10:
                            if slime == 2 or slime == 4 or slime == 6 or slime == 8:
                                at = slime * 0.5
                            else:
                                at = (slime * 0.5) + 0.5
                        HPh -= at
                        print(f'HP: {HPh}')
                    elif attack == 'Electrocute' and MPh >= 3:
                        MPh -= 3
                        if d == 1:
                            if l < 10:
                                slime9 = slime9 - intel
                                slime8 = slime8 - intel
                                slime7 = slime7 - intel
                                slime6 = slime6 - intel
                                slime5 = slime5 - intel
                                slime4 = slime4 - intel
                                slime3 = slime3 - intel
                                slime2 = slime2 - intel
                                slime1 = slime1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    slime9 = slime9 - 2 * intel
                                    slime8 = slime8 - 2 * intel
                                    slime7 = slime7 - 2 * intel
                                    slime6 = slime6 - 2 * intel
                                    slime5 = slime5 - 2 * intel
                                    slime4 = slime4 - 2 * intel
                                    slime3 = slime3 - 2 * intel
                                    slime2 = slime2 - 2 * intel
                                    slime1 = slime1 - 2 * intel
                                    print(
                                        "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                else:
                                    slime9 = slime9 - intel
                                    slime8 = slime8 - intel
                                    slime7 = slime7 - intel
                                    slime6 = slime6 - intel
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    slime9 = slime9 - 2 * intel
                                    slime8 = slime8 - 2 * intel
                                    slime7 = slime7 - 2 * intel
                                    slime6 = slime6 - 2 * intel
                                    slime5 = slime5 - 2 * intel
                                    slime4 = slime4 - 2 * intel
                                    slime3 = slime3 - 2 * intel
                                    slime2 = slime2 - 2 * intel
                                    slime1 = slime1 - 2 * intel
                                    print(
                                        "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                else:
                                    slime9 = slime9 - intel
                                    slime8 = slime8 - intel
                                    slime7 = slime7 - intel
                                    slime6 = slime6 - intel
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                            if slime9 <= 0:
                                print("Congratulations, you have killed 9 slimes. You received 18XP")
                                XP += 18
                                slime -= 9
                                slime1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif slime1 <= 0:
                                print("Congratulations, you have killed a slime. You received 2XP")
                                XP += 2
                                slime -= 1
                                if slime == 8:
                                    d -= 1
                                    slime1 = slime9
                                if slime == 7:
                                    c -= 1
                                    slime1 = slime8
                                if slime == 6:
                                    b -= 1
                                    slime1 = slime7
                                if slime == 5:
                                    slime1 = slime6
                                if slime == 4:
                                    slime1 = slime5
                                if slime == 3:
                                    slime1 = slime4
                                if slime == 2:
                                    slime1 = slime3
                                if slime1 == 1:
                                    slime1 = slime2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif c == 1:
                            if l < 10:
                                slime8 = slime8 - intel
                                slime7 = slime7 - intel
                                slime6 = slime6 - intel
                                slime5 = slime5 - intel
                                slime4 = slime4 - intel
                                slime3 = slime3 - intel
                                slime2 = slime2 - intel
                                slime1 = slime1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    slime8 = slime8 - 2 * intel
                                    slime7 = slime7 - 2 * intel
                                    slime6 = slime6 - 2 * intel
                                    slime5 = slime5 - 2 * intel
                                    slime4 = slime4 - 2 * intel
                                    slime3 = slime3 - 2 * intel
                                    slime2 = slime2 - 2 * intel
                                    slime1 = slime1 - 2 * intel
                                    print(
                                        "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                else:
                                    slime8 = slime8 - intel
                                    slime7 = slime7 - intel
                                    slime6 = slime6 - intel
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    slime8 = slime8 - 2 * intel
                                    slime7 = slime7 - 2 * intel
                                    slime6 = slime6 - 2 * intel
                                    slime5 = slime5 - 2 * intel
                                    slime4 = slime4 - 2 * intel
                                    slime3 = slime3 - 2 * intel
                                    slime2 = slime2 - 2 * intel
                                    slime1 = slime1 - 2 * intel
                                    print(
                                        "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                else:
                                    slime8 = slime8 - intel
                                    slime7 = slime7 - intel
                                    slime6 = slime6 - intel
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                            if slime8 <= 0:
                                print("Congratulations, you have killed 8 slimes. You received 16XP")
                                XP += 16
                                slime -= 8
                                slime1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif slime1 <= 0:
                                print("Congratulations, you have killed a slime. You received 2XP")
                                XP += 2
                                slime -= 1
                                if slime == 8:
                                    d -= 1
                                    slime1 = slime9
                                if slime == 7:
                                    c -= 1
                                    slime1 = slime8
                                if slime == 6:
                                    b -= 1
                                    slime1 = slime7
                                if slime == 5:
                                    slime1 = slime6
                                if slime == 4:
                                    slime1 = slime5
                                if slime == 3:
                                    slime1 = slime4
                                if slime == 2:
                                    slime1 = slime3
                                if slime1 == 1:
                                    slime1 = slime2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 1:
                            if l < 10:
                                slime7 = slime7 - intel
                                slime6 = slime6 - intel
                                slime5 = slime5 - intel
                                slime4 = slime4 - intel
                                slime3 = slime3 - intel
                                slime2 = slime2 - intel
                                slime1 = slime1 - intel
                            elif 9 < l < 20:
                                crit = rnd.randint(1, 10)
                                if crit == 10:
                                    slime7 = slime7 - 2 * intel
                                    slime6 = slime6 - 2 * intel
                                    slime5 = slime5 - 2 * intel
                                    slime4 = slime4 - 2 * intel
                                    slime3 = slime3 - 2 * intel
                                    slime2 = slime2 - 2 * intel
                                    slime1 = slime1 - 2 * intel
                                    print(
                                        "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                else:
                                    slime7 = slime7 - intel
                                    slime6 = slime6 - intel
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                            elif 19 < l < 30:
                                crit = rnd.randint(1, 10)
                                if crit >= 7:
                                    slime7 = slime7 - 2 * intel
                                    slime6 = slime6 - 2 * intel
                                    slime5 = slime5 - 2 * intel
                                    slime4 = slime4 - 2 * intel
                                    slime3 = slime3 - 2 * intel
                                    slime2 = slime2 - 2 * intel
                                    slime1 = slime1 - 2 * intel
                                    print(
                                        "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                else:
                                    slime7 = slime7 - intel
                                    slime6 = slime6 - intel
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                            if slime7 <= 0:
                                print("Congratulations, you have killed 7 slimes. You received 14XP")
                                XP += 14
                                slime -= 7
                                slime1 = 0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                            elif slime1 <= 0:
                                print("Congratulations, you have killed a slime. You received 2XP")
                                XP += 2
                                slime -= 1
                                if slime == 8:
                                    d -= 1
                                    slime1 = slime9
                                if slime == 7:
                                    c -= 1
                                    slime1 = slime8
                                if slime == 6:
                                    b -= 1
                                    slime1 = slime7
                                if slime == 5:
                                    slime1 = slime6
                                if slime == 4:
                                    slime1 = slime5
                                if slime == 3:
                                    slime1 = slime4
                                if slime == 2:
                                    slime1 = slime3
                                if slime1 == 1:
                                    slime1 = slime2
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                    maxHP, MPh, maxMP,
                                                                                                    s, intel, a, st, l,
                                                                                                    usp)
                        elif b == 0 and c == 0 and d == 0:
                            if slime == 6:
                                if l < 10:
                                    slime6 = slime6 - intel
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        slime6 = slime6 - 2 * intel
                                        slime5 = slime5 - 2 * intel
                                        slime4 = slime4 - 2 * intel
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime6 = slime6 - intel
                                        slime5 = slime5 - intel
                                        slime4 = slime4 - intel
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        slime6 = slime6 - 2 * intel
                                        slime5 = slime5 - 2 * intel
                                        slime4 = slime4 - 2 * intel
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime6 = slime6 - intel
                                        slime5 = slime5 - intel
                                        slime4 = slime4 - intel
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                if slime6 <= 0:
                                    print("Congratulations, you have killed 6 slimes. You received 12XP")
                                    XP += 12
                                    slime -= 6
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif slime1 <= 0:
                                    print("Congratulations, you have killed a slime. You received 2XP")
                                    XP += 2
                                    slime -= 1
                                    if slime == 8:
                                        d -= 1
                                        slime1 = slime9
                                    if slime == 7:
                                        c -= 1
                                        slime1 = slime8
                                    if slime == 6:
                                        b -= 1
                                        slime1 = slime7
                                    if slime == 5:
                                        slime1 = slime6
                                    if slime == 4:
                                        slime1 = slime5
                                    if slime == 3:
                                        slime1 = slime4
                                    if slime == 2:
                                        slime1 = slime3
                                    if slime1 == 1:
                                        slime1 = slime2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            if slime == 5:
                                if l < 10:
                                    slime5 = slime5 - intel
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        slime5 = slime5 - 2 * intel
                                        slime4 = slime4 - 2 * intel
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime5 = slime5 - intel
                                        slime4 = slime4 - intel
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        slime5 = slime5 - 2 * intel
                                        slime4 = slime4 - 2 * intel
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime5 = slime5 - intel
                                        slime4 = slime4 - intel
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                if slime5 <= 0:
                                    print("Congratulations, you have killed 5 slimes. You received 10XP")
                                    XP += 10
                                    slime -= 5
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif slime1 <= 0:
                                    print("Congratulations, you have killed a slime. You received 2XP")
                                    XP += 2
                                    slime -= 1
                                    if slime == 8:
                                        d -= 1
                                        slime1 = slime9
                                    if slime == 7:
                                        c -= 1
                                        slime1 = slime8
                                    if slime == 6:
                                        b -= 1
                                        slime1 = slime7
                                    if slime == 5:
                                        slime1 = slime6
                                    if slime == 4:
                                        slime1 = slime5
                                    if slime == 3:
                                        slime1 = slime4
                                    if slime == 2:
                                        slime1 = slime3
                                    if slime1 == 1:
                                        slime1 = slime2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            if slime == 4:
                                if l < 10:
                                    slime4 = slime4 - intel
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        slime4 = slime4 - 2 * intel
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime4 = slime4 - intel
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        slime4 = slime4 - 2 * intel
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime4 = slime4 - intel
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                if slime4 <= 0:
                                    print("Congratulations, you have killed 4 slimes. You received 8XP")
                                    XP += 8
                                    slime -= 4
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif slime1 <= 0:
                                    print("Congratulations, you have killed a slime. You received 2XP")
                                    XP += 2
                                    slime -= 1
                                    if slime == 8:
                                        d -= 1
                                        slime1 = slime9
                                    if slime == 7:
                                        c -= 1
                                        slime1 = slime8
                                    if slime == 6:
                                        b -= 1
                                        slime1 = slime7
                                    if slime == 5:
                                        slime1 = slime6
                                    if slime == 4:
                                        slime1 = slime5
                                    if slime == 3:
                                        slime1 = slime4
                                    if slime == 2:
                                        slime1 = slime3
                                    if slime1 == 1:
                                        slime1 = slime2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            if slime == 3:
                                if l < 10:
                                    slime3 = slime3 - intel
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        slime3 = slime3 - 2 * intel
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime3 = slime3 - intel
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                if slime3 <= 0:
                                    print("Congratulations, you have killed 3 slimes. You received 6XP")
                                    XP += 6
                                    slime -= 3
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif slime1 <= 0:
                                    print("Congratulations, you have killed a slime. You received 2XP")
                                    XP += 2
                                    slime -= 1
                                    if slime == 8:
                                        d -= 1
                                        slime1 = slime9
                                    if slime == 7:
                                        c -= 1
                                        slime1 = slime8
                                    if slime == 6:
                                        b -= 1
                                        slime1 = slime7
                                    if slime == 5:
                                        slime1 = slime6
                                    if slime == 4:
                                        slime1 = slime5
                                    if slime == 3:
                                        slime1 = slime4
                                    if slime == 2:
                                        slime1 = slime3
                                    if slime1 == 1:
                                        slime1 = slime2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            elif slime == 2:
                                if l < 10:
                                    slime2 = slime2 - intel
                                    slime1 = slime1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        slime2 = slime2 - 2 * intel
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slimes couldn't see you so they jumped up. Unfortunately for them, they landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime2 = slime2 - intel
                                        slime1 = slime1 - intel
                                if slime2 <= 0:
                                    print("Congratulations, you have killed 2 slimes. You received 4XP")
                                    XP += 4
                                    slime -= 2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                                elif slime1 <= 0:
                                    print("Congratulations, you have killed a slime. You received 2XP")
                                    XP += 2
                                    slime -= 1
                                    slime1 = slime2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                            elif slime == 1:
                                if l < 10:
                                    slime1 = slime1 - intel
                                elif 9 < l < 20:
                                    crit = rnd.randint(1, 10)
                                    if crit == 10:
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slime couldn't see you so it jumped up. Unfortunately for it, it landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime1 = slime1 - intel
                                elif 19 < l < 30:
                                    crit = rnd.randint(1, 10)
                                    if crit >= 7:
                                        slime1 = slime1 - 2 * intel
                                        print(
                                            "The slime couldn't see you so it jumped up. Unfortunately for it, it landed in the middle of your spell, dealing twice as much damage!")
                                    else:
                                        slime1 = slime1 - intel
                                if slime1 <= 0:
                                    print("Congratulations, you have killed a slime. You received 2XP")
                                    XP += 2
                                    slime -= 1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP,
                                                                                                        HPh, maxHP, MPh,
                                                                                                        maxMP, s, intel,
                                                                                                        a, st, l, usp)
                        if slime1 > 0:
                            print(f"The slime has {slime1}HP remaining")
                            if slime > 1:
                                print(f"The other slimes have {slime2}HP remaining")
                        ac = rnd.randint(1, 10)
                        if ac == 10:
                            at = slime * 5
                        elif 0 < ac < 10:
                            if slime == 2 or slime == 4 or slime == 6 or slime == 8:
                                at = slime * 0.5
                            else:
                                at = (slime * 0.5) + 0.5
                        HPh -= at
                        print(f'HP: {HPh}')
                        if HPh <= 0:
                            print("Game Over")
                            break
    if lvl == 10:
        print("You have met your first boss, a Goblin King!")
        gobk = 1
        mgob = 3
        mgob1 = 50
        mgob2 = mgob1
        mgob3 = mgob1
        print("There are 3 mage goblins with him")
        while gobk > 0 or mgob > 0:
            if classes == 1:
                attack = str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                if attack == 'Fireball' and MPh >= 2:
                    MPh -= 2
                    if mgob > 0:
                        if l < 10:
                            mgob1 = mgob1 - 2 * intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                mgob1 = mgob1 - 4 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblin thought you were launching a water spell and threw a plant type spell. Unfortunately, it caught fire and delt twice as much damage!")
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your fireball, it delt twice the damage!")
                            else:
                                mgob1 = mgob1 - 2 * intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                mgob1 = mgob1 - 4 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblin thought you were launching a water spell and threw a plant type spell. Unfortunately, it caught fire and delt twice as much damage!")
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your fireball, it delt twice the damage!")
                            else:
                                mgob1 = mgob1 - 2 * intel
                        if mgob1 <= 0:
                            print("Congratulations, you have killed a goblin. You received 7XP")
                            XP += 7
                            mgob -= 1
                            if mgob == 2:
                                mgob1 = mgob3
                            if mgob == 1:
                                mgob1 = mgob2
                            elif mgob == 0:
                                mgob1 = HPgoblinking
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif mgob1 > 0:
                            print(f"The goblin has {gob1}HP remaining")
                    elif mgob == 0:
                        if l < 10:
                            HPgoblinking = HPgoblinking - 2 * intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                HPgoblinking = HPgoblinking - 4 * intel
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your fireball, it delt twice the damage!")
                            else:
                                HPgoblinking = HPgoblinking - 2 * intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                HPgoblinking = HPgoblinking - 4 * intel
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your fireball, it delt twice the damage!")
                            else:
                                HPgoblinking = HPgoblinking - 2 * intel
                        if HPgoblinking <= 0:
                            print("Congratulations, you have killed the goblin king. You received 100XP")
                            XP += 1000
                            gobk -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                    if HPgoblinking > 0:
                        print(f"The goblin king has {HPgoblinking} HP remaining.")
                    acc = rnd.randint(1, 20)
                    if acc == 20:
                        at = mgob * 10 + gobk * 10
                    elif 0 < acc < 20:
                        at = mgob * 2 + gobk * 7
                    HPh -= at
                    print(f'HP: {HPh}')
                    if HPh <= 0:
                        print("Game Over")
                        break
                elif attack == 'Heal' and MPh >= 3:
                    HPh += 50
                    MPh -= 3
                    if HPh > maxHP:
                        HPh = maxHP
                    else:
                        HPh = HPh
                    acc = rnd.randint(1, 20)
                    if acc == 20:
                        at = mgob * 10 + gobk * 10
                    elif 0 < acc < 20:
                        at = mgob * 2
                    HPh -= at
                    print(f'HP: {HPh}')
                elif attack == 'Electrocute' and MPh >= 3:
                    MPh -= 3
                    if mgob == 3:
                        if l < 10:
                            mgob3 = mgob3 - intel
                            mgob2 = mgob2 - intel
                            mgob1 = mgob1 - intel
                            HPgoblinking -= intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                mgob3 = mgob3 - 2 * intel
                                mgob2 = mgob2 - 2 * intel
                                mgob1 = mgob1 - 2 * intel
                                HPgoblinking -= 2 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblins thought you were firing a fire type spell and protected themselves with water. As you expect, it did twice the amount of damge!")
                                print(
                                    "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                mgob3 = mgob3 - intel
                                mgob2 = mgob2 - intel
                                mgob1 = mgob1 - intel
                                HPgoblinking -= intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                mgob3 = mgob3 - 2 * intel
                                mgob2 = mgob2 - 2 * intel
                                mgob1 = mgob1 - 2 * intel
                                HPgoblinking -= 2 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblins thought you were firing a fire type spell and protected themselves with water. As you expect, it did twice the amount of damge!")
                                print(
                                    "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                mgob3 = mgob3 - intel
                                mgob2 = mgob2 - intel
                                mgob1 = mgob1 - intel
                                HPgoblinking -= intel
                        if mgob3 <= 0:
                            print("Congratulations, you have killed 3 mage goblins. You received 60XP")
                            XP += 60
                            mgob -= 3
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        if HPgoblinking <= 0:
                            print("Congratulations, you have killed the goblin king. You received 100XP")
                            XP += 1000
                            gobk -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                    elif mgob == 2:
                        if l < 10:
                            mgob2 = mgob2 - intel
                            mgob1 = mgob1 - intel
                            HPgoblinking -= intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                mgob2 = mgob2 - 2 * intel
                                mgob1 = mgob1 - 2 * intel
                                HPgoblinking -= 2 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblins thought you were firing a fire type spell and protected themselves with water. As you expect, it did twice the amount of damge!")
                                else:
                                    print(
                                        "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                mgob2 = mgob2 - intel
                                mgob1 = mgob1 - intel
                                HPgoblinking -= intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                mgob2 = mgob2 - 2 * intel
                                mgob1 = mgob1 - 2 * intel
                                HPgoblinking -= 2 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblins thought you were firing a fire type spell and protected themselves with water. As you expect, it did twice the amount of damge!")
                                mgob2 = mgob2 - intel
                                mgob1 = mgob1 - intel
                                HPgoblinking -= intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                gob2 = gob2 - 2 * intel
                                gob1 = gob1 - 2 * intel
                                HPgoblinking -= 2 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblins thought you were firing a fire type spell and protected themselves with water. As you expect, it did twice the amount of damge!")
                                else:
                                    print(
                                        "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                mgob2 = mgob2 - intel
                                mgob1 = mgob1 - intel
                                HPgoblinking -= intel
                        if mgob2 <= 0:
                            print("Congratulations, you have killed 2 mage goblins. You received 40XP")
                            XP += 40
                            mgob -= 2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        if HPgoblinking <= 0:
                            print("Congratulations, you have killed the goblin king. You received 100XP")
                            XP += 1000
                            gobk -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                    elif mgob == 1:
                        if l < 10:
                            mgob1 = mgob1 - intel
                            HPgoblinking -= intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                mgob1 = mgob1 - 2 * intel
                                HPgoblinking -= 2 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblin thought you were firing a fire type spell and protected himself with water. As you expect, it did twice the amount of damge!")
                                print(
                                    "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                mgob1 = mgob1 - intel
                                HPgoblinking -= intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                gob1 = gob1 - 2 * intel
                                HPgoblinking -= 2 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblin thought you were firing a fire type spell and protected himself with water. As you expect, it did twice the amount of damge!")
                                print(
                                    "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                mgob1 = mgob1 - intel
                                HPgoblinking -= intel
                        if mgob1 <= 0:
                            print("Congratulations, you have killed a mage goblin. You received 20XP")
                            XP += 20
                            mgob -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        if HPgoblinking <= 0:
                            print("Congratulations, you have killed the goblin king. You received 100XP")
                            XP += 1000
                            gobk -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                    elif mgob == 0:
                        if l < 10:
                            HPgoblinking -= intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                HPgoblinking -= 2 * intel
                                print(
                                    "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                HPgoblinking -= intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                HPgoblinking -= 2 * intel
                                print(
                                    "The goblin king tried to avoid your attack but ran right into it dealing double the damage!")
                            else:
                                HPgoblinking -= intel
                        if HPgoblinking <= 0:
                            print("Congratulations, you have killed the goblin king. You received 100XP")
                            XP += 1000
                            gobk -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                    if mgob1 > 0:
                        print(f"The goblin has {mgob1}HP remaining")
                        if mgob > 1:
                            print(f"The other goblins have {mgob2}HP remaining")
                    if HPgoblinking > 0:
                        print(f"The goblin king has {HPgoblinking}HP remaining.")
                    acc = rnd.randint(1, 20)
                    if acc == 20:
                        at = mgob * 10 + gobk * 10
                    elif 0 < acc < 20:
                        at = mgob * 2 + gobk * 10
                    HPh -= at
                    print(f'HP: {HPh}')
                    if HPh <= 0:
                        print("Game Over")
                        break
                elif attack == 'Hit':
                    if mgob > 0:
                        if l < 10:
                            mgob1 = mgob1 - s
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                mgob1 = mgob1 - 2 * s
                                if mgob > 0:
                                    print("You hit the mage goblin in the face! You dealt twice as much damage!")
                                print("You hit the goblin king's jewels! You dealt twice as much damage!")
                            else:
                                mgob1 = mgob1 - s
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                mgob1 = mgob1 - 2 * s
                                if mgob > 0:
                                    print("You hit the mage goblin in the face! You dealt twice as much damage!")
                                print("You hit the goblin king's jewels! You dealt twice as much damage!")
                            else:
                                mgob1 = mgob1 - s
                        if mgob1 <= 0:
                            print("Congratulations, you have killed a goblin. You received 7XP")
                            XP += 7
                            mgob -= 1
                            if mgob == 2:
                                mgob1 = mgob3
                            if mgob == 1:
                                mgob1 = mgob2
                            elif mgob == 0:
                                mgob1 = HPgoblinking
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif mgob1 > 0:
                            print(f"The goblin has {gob1}HP remaining")
                    elif mgob == 0:
                        if l < 10:
                            HPgoblinking = HPgoblinking - s
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                HPgoblinking = HPgoblinking - 2 * s
                                print("You hit the goblin king's jewels! You dealt twice as much damage!")
                            else:
                                HPgoblinking = HPgoblinking - s
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                HPgoblinking = HPgoblinking - 2 * s
                                print("You hit the goblin king's jewels! You dealt twice as much damage!")
                            else:
                                HPgoblinking = HPgoblinking - s
                        if HPgoblinking <= 0:
                            print("Congratulations, you have killed the goblin king. You received 100XP")
                            XP += 1000
                            gobk -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                    if HPgoblinking > 0:
                        print(f"The goblin king has {HPgoblinking}HP remaining.")
                    acc = rnd.randint(1, 20)
                    if acc == 20:
                        at = mgob * 10 + gobk * 10
                    elif 0 < acc < 20:
                        at = mgob * 2 + gobk * 7
                    HPh -= at
                    print(f'HP: {HPh}')
                    if HPh <= 0:
                        print("Game Over")
                        break
                elif attack == 'Watershot' and MPh >= 5:
                    MPh -= 2
                    if mgob > 0:
                        if l < 10:
                            mgob1 = mgob1 - 4 * intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                mgob1 = mgob1 - 8 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblins protected themselves with an electric cage, the watershot became an electric watershot and delt twice as much damage!")
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your watershot, it delt twice the damage!")
                            else:
                                mgob1 = mgob1 - 4 * intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                mgob1 = mgob1 - 8 * intel
                                if mgob > 0:
                                    print(
                                        "The mage goblins protected themselves with an electric cage, the watershot became an electric watershot and delt twice as much damage!")
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your watershot, it delt twice the damage!")
                            else:
                                mgob1 = mgob1 - 4 * intel
                        if mgob1 <= 0:
                            print("Congratulations, you have killed a goblin. You received 7XP")
                            XP += 7
                            mgob -= 1
                            if mgob == 2:
                                mgob1 = mgob3
                            if mgob == 1:
                                mgob1 = mgob2
                            elif mgob == 0:
                                mgob1 = HPgoblinking
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                        elif mgob1 > 0:
                            print(f"The goblin has {gob1}HP remaining")
                    elif mgob == 0:
                        if l < 10:
                            HPgoblinking = HPgoblinking - 2 * intel
                        elif 9 < l < 20:
                            crit = rnd.randint(1, 10)
                            if crit == 10:
                                HPgoblinking = HPgoblinking - 4 * intel
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your watershot, it delt twice the damage!")
                            else:
                                HPgoblinking = HPgoblinking - 2 * intel
                        elif 19 < l < 30:
                            crit = rnd.randint(1, 10)
                            if crit >= 7:
                                HPgoblinking = HPgoblinking - 4 * intel
                                print(
                                    "The goblin king forgot about you for a second and forgot to block your watershot, it delt twice the damage!")
                            else:
                                HPgoblinking = HPgoblinking - 2 * intel
                        if HPgoblinking <= 0:
                            print("Congratulations, you have killed the goblin king. You received 100XP")
                            XP += 1000
                            gobk -= 1
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp = g(lvl, XP, maxXP, HPh,
                                                                                                maxHP, MPh, maxMP, s,
                                                                                                intel, a, st, l, usp)
                    if HPgoblinking > 0:
                        print(f"The goblin king has {HPgoblinking}HP remaining.")
                    acc = rnd.randint(1, 20)
                    if acc == 20:
                        at = mgob * 10 + gobk * 10
                    elif 0 < acc < 20:
                        at = mgob * 2 + gobk * 7
                    HPh -= at
                    print(f'HP: {HPh}')
                    if HPh <= 0:
                        print("Game Over")
                        break
    while 10 < lvl < 20:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    if lvl == 20:
        print("You have met your second boss, a Spider Queen")
    while 20 < lvl < 30:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    while 30 < lvl < 40:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    while 40 < lvl < 50:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    while 50 < lvl < 60:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    while 60 < lvl < 70:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    while 70 < lvl < 80:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    while 80 < lvl < 90:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    while 90 < lvl < 100:
        story_2 = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2 == 1:
            print("You have set out on a new adventure.")
        if story_2 == 2:
            print("You have set out on a new adventure.")
        if story_2 == 3:
            print("You have set out on a new adventure.")
    if lvl == 100:
        print("You have arrived to the Demon king's palace.")
"""
def new_game() -> None:
    player1.p_name = str(input("Welcome Hero, what might your name be: "))
    print(f"Welcome {player1.p_name}. You have been summoned to this world called Aether. " \
          "Your goal is to reach level 100 and beat the demon lord. Good luck.")
    print("Say status. (You prounounce the word status. A screen appears in front of you)")
    player1.display_info()
    player1.unassigned_points()
    user_input = str(input("Please hit enter to continue"))
    print()
    print()
    return

def game() -> None:
    game_play = True
    while game_play:
        s_location = str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if s_location.lower() not in ['forest', 'f', 'mountain', 'm',
                                      'dungeon', 'd', 'plains', 'p']:
            print('Incorrect Answer. Please try again')
        elif s_location.lower() in ['mountain', 'm']:
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to the mountains.")
            print("You arrive at a beginner mountain known for it's weak monsters.")
            print(f"While traveling, you get ambushed by a group of {creatures.num_cs} kobolts.")
            print(creatures.fight_creatures)
            game_play = False
    return


def game_menu():
    while True:
        print('(1) New Game')
        print('(2) Load Game')
        print('(3) Options')
        print('(4) Exit Game')
        user_input = str(input('Insert: '))
        if user_input not in ['1', '2', '3', '4']:
            print('Incorrect selection. Pleas try again\n')
        elif user_input == '1':
            new_game()
            game()
        elif user_input == '2':
            if gamedata.file_exists:
                gamedata.load_data(player1)
                game()
            else:
                print('File doesnt exist. Creating a new file.')
                new_game()
                game()
        elif user_input == '3':
            options_menu(difficulty)
        elif user_input == '4':
            exit()


def options_menu(difficulty):
    diff=0
    print('needs to be added')
    while diff==0:
        print("What difficulty will you chose?")
        print("Easy (1)")
        print("Medium (2)")
        print("Hard (3)")
        print("Extreme (4)")
        difficulty=str(input('Insert: '))
        if difficulty not in ['1', '2', '3', '4']:
            print('Incorrect selection. Pleas try again\n')
        elif difficulty == '1':
            print("We need to do the game easy")
            diff=1
        elif difficulty == '2':
            print("We need to do the game a bit harder")
            diff=1
        elif difficulty == '3':
            print("We need to do the game hard")
            diff=1
        elif difficulty == '4':
            print("We need to do the game extreme")
            diff=1
        return difficulty

if __name__ == '__main__':
    game_menu()