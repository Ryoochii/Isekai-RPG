
import random as rnd

monsters=1
classes=rnd.randint(1,1)
story=1
XP=0
maxXP=10

def save():
    with open('RPGsave.txt', 'w') as fil:
        fil.write(str(lvl)+'\t'+str(XP)+'\t'+str(maxXP)+'\t'+str(HPh)+'\t'+str(maxHP)+'\t'+str(MPh)+'\t'+str(maxMP)+'\t'+str(s)+'\t'+str(intel)+'\t'+str(a)+'\t'+str(st)+'\t'+str(l)+'\t'+str(usp))

def load(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp):
    try:
        with open('RPGsave.txt') as fil:
            ans=str(input("Do you want to continue where you stopped (Yes or No): "))
            if ans!='Yes' or ans!='yes' or ans!='No' or ans!='no':
                print("Learn how to write!")
                ans=str(input("Do you want to continue where you stopped (Yes or No): "))
            if ans=='Yes' or ans=='yes':
                for linje in fil:
                    lvl=(int(linje.split()[0]))
                    XP=(int(linje.split()[1]))
                    maxXP=(int(linje.split()[2]))
                    HPh=(int(linje.split()[3]))
                    maxHP=(int(linje.split()[4]))
                    MPh=(int(linje.split()[5]))
                    maxMP=(int(linje.split()[6]))
                    s=(int(linje.split()[7]))
                    intel=(int(linje.split()[8]))
                    a=(int(linje.split()[9]))
                    st=(int(linje.split()[10]))
                    l=(int(linje.split()[11]))
                    usp=(int(linje.split()[12]))
            if ans=='No' or ans=='no':
                pass
    except IOError:
        pass
    return(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)

def f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp):
    print(f"Level: {lvl}   XP: {XP}/{maxXP}")
    print(f"Job: {Job}")
    print(f"HP: {HPh}/{maxHP}")
    if classes==1:
        print(f"MP: {MPh}/{maxMP}")
    elif classes==2:
        print(f"Energy: {ENh}/{maxEN}")
    elif classes==3:
        print(f"Energy: {ENh}/{maxEN}")
    print(f"Strength: {s}")
    print(f"Intellect: {intel}")
    print(f"Agility: {a}")
    print(f"Stamina: {st}")
    print(f"Luck: {l}")
    print(f"Skills: {skills}")
    print(f"Unassigned Stat Points: {usp}")

def h(s, usp, intel, a, st, l):
    sp=str(input("Will you assign your points? Yes or No: "))
    if sp=='Yes':
        print("Assign your points")
        pa=str(input("Assign your stat points to a category (Strength, Intellect, Agility, Stamina or Luck): "))
        amount=int(input("How many points do you want to add?: "))
        while amount<0 or amount>usp:
            print("Impossible")
            amount=int(input("How many points do you want to add?: "))
        if pa=='Strength':
            s+=amount
            usp-=amount
        elif pa=='Intellect':
            intel+=amount
            usp-=amount
        elif pa=='Agility':
            a+=amount
            usp-=amount
        elif pa=='Stamina':
            st+=amount
            usp-=amount
        elif pa=='Luck':
            l+=amount
            usp-=amount
        else:
            print("Invalid point; try again")
    else:
        print("No points added.")
    return(s, usp, intel, a, st, l)

def g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp):
    if lvl==1 and XP>=maxXP:
        XP-=maxXP
        lvl+=1
        maxXP=25
        s+=1
        intel+=1
        a+=1
        st+=1
        l+=1
        maxHP=20
        HPh=maxHP
        maxMP=20
        MPh=maxMP
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        save()
    if lvl==2 and XP>=maxXP:
        XP-=maxXP
        lvl=3
        maxXP=50
        s+=1
        intel+=1
        a+=1
        st+=1
        l+=1
        maxHP+=10
        HPh=maxHP
        maxMP+=10
        MPh=maxMP 
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        save()
    if lvl==3 and XP>=maxXP:
        XP-=maxXP
        lvl=4
        maxXP=75
        s+=1
        intel+=1
        a+=1
        st+=1
        l+=1
        maxHP+=10
        HPh=maxHP
        maxMP+=10
        MPh=maxMP   
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        save()
    while lvl>=4 and lvl<10 and XP>=maxXP:
        XP-=maxXP
        lvl+=1
        maxXP=100
        s+=1
        intel+=1
        a+=1
        st+=1
        l+=1
        maxHP+=10
        HPh=maxHP
        maxMP+=10
        MPh=maxMP  
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        save()
    if lvl==9 and XP>=maxXP:
        XP-=maxXP
        lvl+=1
        maxXP=1000
        s+=10
        intel+=10
        a+=10
        st+=10
        l+=10
        maxHP+=100
        HPh=maxHP
        maxMP+=100
        MPh=maxMP
        usp+=10
        print("Level up")
        f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
        print("You have received the skill: Watershot (5 mana, 3*intelligence on 1 creature)")
        Skills.append(", Watershot (5 mana, 3*intelligence on 1 creature)")
        print(f"Unassigned Stat Points: {usp}")
        h();
        save();
    return(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)

if monsters==1:
    HPgoblin=20
    HPhobgoblin=50
    HPslime=10
    HPzombie=40
    HPkobolds=75
    HPghost=75
    
    HPgoblinking=200
    
    HPspider=100
    HPwolf=150
    HPskeletonsoldier=50
    HPskeletonknight=250
    HPghoul=250
    
    HPspiderqueen=500

    HPorc=400
    HPbeastmen=500
    HPbasilisk=500
    HPcentipede=600
    HPcentaur=650
    
    Satyr=800
    
    HPearthelemental=750
    HPfireelemental=750
    HPwaterelemental=750
    HPwindelemental=750
    
    HPfusedelemental=1250
    
    HPfairy=1000
    HPelf=1500
    HPdwarf=1750
    HPdarkknight=2000
    
    HPdarkmage=2500
    
    #HP
    HPskeletondragon=3000
    
    HPgolem=10000
    HPminotaur=10000
    HPdemonlackey=12500
    HPwerewolf=12500
    
    HPsuccubi=15000
    
    HPkraken=15000
    HPmanticore=16000
    HPdarkelf=15000
    HPwyvern=16000
    HPtroll=15500
    
    HPphoenix=19000
    
    HPlich=17500
    HPvampire=20000
    HPgiant=25000
    HPchimera=30000
    HPdragon=50000
    
    HPDemonlord=100000
    
    HPg=HPgoblin
    HPh=HPhobgoblin
    HPs=HPslime
    HPgh=HPghoul
    HPd=HPdragon
    HPo=HPorc
    HPsp=HPspider
    HPl=HPlich
    HPss=HPskeletonsoldier
    HPsk=HPskeletonknight
    HPgo=HPgolem
    HPde=HPdemonlackey
if story==1:
    if classes==1:
        Job='Magician'
        strength=rnd.randint(7, 11)
        intellect=rnd.randint(12, 16)
        agility=rnd.randint(8, 12)
        stamina=rnd.randint(12, 16)
        luck=rnd.randint(8, 12)
        Unassigned_statpoints=rnd.randint(1, 3)
        skills=["Fireball, Heal, Electrocute"]
        Skills=["Fireball (2 mana; 2*intellect on 1 enemy), Heal (3 mana; heal yourself for 50 HP), Electrocute (3 mana; 1*intellect to all creatures), Hit (0 mana; 1*strength on 1 enemmy)"]
    if classes==2:
        Job='Warrior'
        strength=rnd.randint(12, 16)
        intellect=rnd.randint(7, 11)
        agility=rnd.randint(8, 12)
        stamina=rnd.randint(8, 12)
        luck=rnd.randint(12, 16)
        Unassigned_statpoints=rnd.randint(1, 3)
        skills=["Pierce, Slice, Strengthen, Hit"]
        Skills=["Pierce (2 energy; 2*strength on max 3 ennemies), Slice (3 energy; 4*strength on one enemmy), Strengthen (4 energy, augment your shield by 50 for 3 turns) or Hit (0 energy; 1*strength on 1 enemmy)"]
    if classes==3:
        Job='Archer'
        strength=rnd.randint(8, 12)
        intellect=rnd.randint(8, 12)
        agility=rnd.randint(12, 16)
        stamina=rnd.randint(7, 11)
        luck=rnd.randint(12, 16)
        Unassigned_statpoints=rnd.randint(1, 3)
        skills=["Hawkeye, Piercing arrow, Heavy arrow"]
    s=strength
    intel=intellect
    a=agility
    st=stamina
    l=luck
    usp=Unassigned_statpoints
    lvl=1
    XP=0
    maxXP=10
    HPh=10
    maxHP=10
    MPh=10
    maxMP=10
    ENh=10
    maxEN=10
    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp= load(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
    if lvl==1:
        name=str(input("Welcome Hero, what might your name be: "))
        print(f"Welcome {name}. You have been summoned to this world called Aether. Your goal is to reach level 100 and beat the demon lord. Good luck.")
        print("Say status. (You prounounce the word status. A screen appears in front of you)")
    else:
        print("Welcome back. Let's continue the game. Here are your stats!")
    f(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
    s, usp, intel, a, st, l=h(s, usp, intel, a, st, l)
    while lvl<10:
        if HPh<=0:
            break
        save()
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2=='Forest':
            d=0
            c=0
            b=0
            gob=rnd.randint(3, 6)
            if gob>=3:
                gob1=HPg
                gob2=HPg
                gob3=HPg
            if gob>=6:
                gob6=HPg
                d=1
            if gob>=5:
                gob5=HPg
                c=1
            if gob==4:
                gob4=HPg
                b=1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to a forest.")
            print("You arrive at a dense forrest known for it's weak monsters.")
            print("In the forrest, you see a goblin encampment.")
            print(f"After watching for a moment, you manage to see a total of {gob} goblins.")
            while gob>0:
                if classes==1:
                    attack=str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                    if attack=='Fireball' and MPh>=2:
                        MPh-=2
                        if l<10:
                            gob1=HPg-2*intel
                        elif 9<l<20:
                            crit=rnd.randint(1, 10)
                            if crit==10:
                                gob1=gob1-4*intel
                                print("You stumbled and shot a bit lower, the goblin tried avoiding your spell but the fireball hit the goblin in his face and did double the damage!")
                            else:
                                gob1=HPg-2*intel
                        elif 19<l<30:
                            crit=rnd.randint(1, 10)
                            if crit>=7:
                                gob1=gob1-4*intel
                                print("You stumbled and shot a bit lower, the goblin tried avoiding your spell but the fireball hit the goblin in his face and did double the damage!")
                            else:
                                gob1=HPg-2*intel
                        if gob1<=0:
                            print("Congratulations, you have killed a goblin. You received 7XP")
                            XP+=7
                            gob-=1
                            if gob==5:
                                d-=1
                                gob1=gob6
                            if gob==4:
                                c-=1
                                gob1=gob5
                            if gob==3:
                                b-=1
                                gob1=gob4
                            if gob==2:
                                gob1=gob3
                            if gob==1:
                                gob1=gob2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif gob1>0:
                            print(f"The goblin has {gob1} remaining")
                        at=gob*1
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
                    elif attack=='Heal' and MPh>=3:
                        HPh+=50
                        MPh-=3
                        if HPh>maxHP:
                            HPh=maxHP
                        else:
                            HPh=HPh
                        at=gob*1
                        HPh-=at
                        print(f'HP: {HPh}')
                    elif attack=='Electrocute' and MPh>=3:
                        MPh-=3
                        if d==1:
                            if l<10:
                                gob6=gob6-intel
                                gob5=gob6
                                gob4=gob6
                                gob3=gob6
                                gob2=gob6
                                gob1=gob6
                            elif 9<l<20:
                                crit=rnd.randint(1, 10)
                                if crit==10:
                                    gob6=gob6-2*intel
                                    gob5=gob6
                                    gob4=gob6
                                    gob3=gob6
                                    gob2=gob6
                                    gob1=gob6
                                    print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob6=gob6-intel
                                    gob5=gob6
                                    gob4=gob6
                                    gob3=gob6
                                    gob2=gob6
                                    gob1=gob6
                            elif 19<l<30:
                                crit=rnd.randint(1, 10)
                                if crit>=7:
                                    gob6=gob6-2*intel
                                    gob5=gob6
                                    gob4=gob6
                                    gob3=gob6
                                    gob2=gob6
                                    gob1=gob6
                                    print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob6=gob6-intel
                                    gob5=gob6
                                    gob4=gob6
                                    gob3=gob6
                                    gob2=gob6
                                    gob1=gob6
                            if gob6<=0:
                                print("Congratulations, you have killed 6 goblins. You received 42XP")
                                XP+=42
                                gob-=6
                                gob1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif c==1:
                            if l<10:
                                gob5=gob5-intel
                                gob4=gob5
                                gob3=gob5
                                gob2=gob5
                            elif 9<l<20:
                                crit=rnd.randint(1, 10)
                                if crit==10:
                                    gob5=gob5-2*intel
                                    gob4=gob5
                                    gob3=gob5
                                    gob2=gob5
                                    print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob5=gob5-intel
                                    gob4=gob5
                                    gob3=gob5
                                    gob2=gob5
                            elif 19<l<30:
                                crit=rnd.randint(1, 10)
                                if crit>=7:
                                    gob5=gob5-2*intel
                                    gob4=gob5
                                    gob3=gob5
                                    gob2=gob5
                                    print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob5=gob5-intel
                                    gob4=gob5
                                    gob3=gob5
                                    gob2=gob5
                            if gob5<=0:
                                print("Congratulations, you have killed 5 goblins. You received 35XP")
                                XP+=35
                                gob-=5
                                gob1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==1:
                            if l<10:
                                gob4=gob4-intel
                                gob3=gob4
                                gob2=gob4
                            elif 9<l<20:
                                crit=rnd.randint(1, 10)
                                if crit==10:
                                    gob4=gob4-2*intel
                                    gob3=gob4
                                    gob2=gob4
                                    print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob4=gob4-intel
                                    gob3=gob4
                                    gob2=gob4
                            elif 19<l<30:
                                crit=rnd.randint(1, 10)
                                if crit>=7:
                                    gob4=gob4-2*intel
                                    gob3=gob4
                                    gob2=gob4
                                    print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                else:
                                    gob4=gob4-intel
                                    gob3=gob4
                                    gob2=gob4
                            if gob4<=0:
                                print("Congratulations, you have killed 4 goblins. You received 28XP")
                                XP+=28
                                gob-=4
                                gob1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==0 and c==0 and d==0:
                            if gob==3:
                                if l<10:
                                    gob3=gob3-intel
                                    gob2=gob3
                                    gob1=gob3
                                elif 9<l<20:
                                    crit=rnd.randint(1, 10)
                                    if crit==10:
                                        gob3=gob3-2*intel
                                        gob2=gob3
                                        gob1=gob3
                                        print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob3=gob3-intel
                                        gob2=gob3
                                        gob1=gob3
                                elif 19<l<30:
                                    crit=rnd.randint(1, 10)
                                    if crit>=7:
                                        gob3=gob3-2*intel
                                        gob2=gob3
                                        gob1=gob3
                                        print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob3=gob3-intel
                                        gob2=gob3
                                        gob1=gob3
                                if gob1<=0:
                                    print("Congratulations, you have killed 3 goblins. You received 21XP")
                                    XP+=21
                                    gob-=3
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            if gob==2:
                                if l<10:
                                    gob1=gob1-intel
                                elif 9<l<20:
                                    crit=rnd.randint(1, 10)
                                    if crit==10:
                                        gob1=gob1-2*intel
                                        print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1=gob1-intel
                                elif 19<l<30:
                                    crit=rnd.randint(1, 10)
                                    if crit>=7:
                                        gob1=gob1-2*intel
                                        print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1-=intel
                                if gob1<=0:
                                    print("Congratulations, you have killed 2 goblins. You received 14XP")
                                    XP+=14
                                    gob-=2
                                    gob2=gob1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            if gob==1:
                                if l<10:
                                    gob1=gob1-intel
                                elif 9<l<20:
                                    crit=rnd.randint(1, 10)
                                    if crit==10:
                                        gob1=gob1-2*intel
                                        print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1=gob1-intel
                                elif 19<l<30:
                                    crit=rnd.randint(1, 10)
                                    if crit>=7:
                                        gob1=gob1-2*intel
                                        print("You shout a bit higher than usual, scaring the goblins. They were unable to block the attack and it did double the damage!")
                                    else:
                                        gob1-=intel
                                if gob1<=0:
                                    print("Congratulations, you have killed a goblin. You received 7XP")
                                    XP+=7
                                    gob-=1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        if gob1>0:
                            print(f"The goblin has {gob1}HP remaining")
                            if gob>1:
                                print(f"The other goblins have {gob2}HP remaining")
                        at=gob*1
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
        elif story_2=='Mountain':
            kob=rnd.randint(3, 6)
            d=0
            c=0
            b=0
            if kob>=3:
                kob1=HPkobolds
                kob2=HPkobolds
                kob3=HPkobolds
            if kob>=6:
                kob6=HPkobolds
                d=1
            if kob>=5:
                kob5=HPkobolds
                c=1
            if kob==4:
                kob4=HPkobolds
                b=1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to the mountains.")
            print("You arrive at a beginner mountain known for it's weak monsters.")
            print(f"While traveling, you get ambushed by a group of {kob} kobolts.")
            while kob>0:
                if classes==1:
                    attack=str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                    if attack=='Fireball' and MPh>=2:
                        MPh-=2
                        if l<10:
                            kob1=HPkobolds-2*intel
                        elif 9<l<20:
                            crit=rnd.randint(1, 10)
                            if crit==10:
                                kob1=HPkobolds-4*intel
                                print("The kobold tried to avoid your spell but ran into a wall, you having missed by little you spell, the fireball hit directly the kobold in his face and did double the damage!")
                            else:
                                kob1=HPkobolds-2*intel
                        elif 19<l<30:
                            crit=rnd.randint(1, 10)
                            if crit>=7:
                                kob1=HPkobolds-4*intel
                                print("The kobold tried to avoid your spell but ran into a wall, you having missed by little you spell, the fireball hit directly the kobold in his face and did double the damage!")
                            else:
                                kob1=HPkobolds-2*intel
                        if kob1<=0:
                            print("Congratulations, you have killed a Kobold. You received 15XP")
                            XP+=15
                            kob-=1
                            if kob==5:
                                d-=1
                                kob1=kob6
                            if kob==4:
                                c-=1
                                kob1=kob5
                            if kob==3:
                                b-=1
                                kob1=kob4
                            if kob==2:
                                kob1=kob3
                            if kob==1:
                                kob1=kob2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif kob1>0:
                            print(f"The kobold has {kob1} remaining")
                        at=kob*3
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
                    elif attack=='Heal' and MPh>=3:
                        HPh+=50
                        MPh-=3
                        if HPh>maxHP:
                            HPh=maxHP
                        else:
                            HPh=HPh
                        at=kob*3
                        HPh-=at
                        print(f'HP: {HPh}')
                    elif attack=='Electrocute' and MPh>=3:
                        MPh-=3
                        if d==1:
                            if l<10:
                                kob6=kob6-intel
                                kob5=kob6
                                kob4=kob6
                                kob3=kob6
                                kob2=kob6
                            elif 9<l<20:
                                crit=rnd.randint(1, 10)
                                if crit==10:
                                    kob6=kob6-2*intel
                                    kob5=kob6
                                    kob4=kob6
                                    kob3=kob6
                                    kob2=kob6
                                    print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob6=kob6-intel
                                    kob5=kob6
                                    kob4=kob6
                                    kob3=kob6
                                    kob2=kob6
                            elif 19<l<30:
                                crit=rnd.randint(1, 10)
                                if crit>=7:
                                    kob6=kob6-2*intel
                                    kob5=kob6
                                    kob4=kob6
                                    kob3=kob6
                                    kob2=kob6
                                    print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob6=kob6-intel
                                    kob5=kob6
                                    kob4=kob6
                                    kob3=kob6
                                    kob2=kob6
                            if kob6<=0:
                                print("Congratulations, you have killed 6 kobolds. You received 90XP")
                                XP+=90
                                kob-=6
                                kob1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif c==1:
                            if l<10:
                                kob5=kob5-intel
                                kob4=kob5
                                kob3=kob5
                                kob2=kob5
                            elif 9<l<20:
                                crit=rnd.randint(1, 10)
                                if crit==10:
                                    kob5=kob5-2*intel
                                    kob4=kob5
                                    kob3=kob5
                                    kob2=kob5
                                    print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob5=kob5-intel
                                    kob4=kob5
                                    kob3=kob5
                                    kob2=kob5
                            elif 19<l<30:
                                crit=rnd.randint(1, 10)
                                if crit>=7:
                                    kob5=kob5-2*intel
                                    kob4=kob5
                                    kob3=kob5
                                    kob2=kob5
                                    print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob5=kob5-intel
                                    kob4=kob5
                                    kob3=kob5
                                    kob2=kob5
                            if kob5<=0:
                                print("Congratulations, you have killed 5 kobolds. You received 75XP")
                                XP+=75
                                kob-=5
                                kob1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==1:
                            if l<10:
                                kob4=kob4-intel
                                kob4=kob4
                                kob3=kob4
                                kob2=kob4
                            elif 9<l<20:
                                crit=rnd.randint(1, 10)
                                if crit==10:
                                    kob4=kob4-2*intel
                                    kob4=kob4
                                    kob3=kob4
                                    kob2=kob4
                                    print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob4=kob4-intel
                                    kob3=kob4
                                    kob2=kob4
                            elif 19<l<30:
                                crit=rnd.randint(1, 10)
                                if crit>=7:
                                    kob4=kob4-2*intel
                                    kob3=kob4
                                    kob2=kob4
                                    print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                else:
                                    kob4=kob4-intel
                                    kob3=kob4
                                    kob2=kob4
                            if kob4<=0:
                                print("Congratulations, you have killed 4 kobolds. You received 60XP")
                                XP+=60
                                kob-=4
                                kob1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==0 and c==0 and d==0:
                            if kob==3:
                                if l<10:
                                    kob1=kob1-intel
                                    kob2=kob1
                                elif 9<l<20:
                                    crit=rnd.randint(1, 10)
                                    if crit==10:
                                        kob1=kob1-2*intel
                                        kob2=kob1
                                        print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1=kob1-intel
                                        kob2=kob1
                                elif 19<l<30:
                                    crit=rnd.randint(1, 10)
                                    if crit>=7:
                                        kob1=kob1-2*intel
                                        kob2=kob1
                                        print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1=kob1-intel
                                        kob2=kob1
                                if kob1<=0:
                                    print("Congratulations, you have killed 3 kobolds. You received 45XP")
                                    XP+=45
                                    kob-=3
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            elif kob==2:
                                if l<10:
                                    kob1=kob1-intel
                                elif 9<l<20:
                                    crit=rnd.randint(1, 10)
                                    if crit==10:
                                        kob1=kob1-2*intel
                                        print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1=kob1-intel
                                elif 19<l<30:
                                    crit=rnd.randint(1, 10)
                                    if crit>=7:
                                        kob1=kob1-2*intel
                                        print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1=kob1-intel
                                if kob1<=0:
                                    print("Congratulations, you have killed 2 kobolds. You received 30XP")
                                    XP+=30
                                    kob-=2
                                    kob2-=intel
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            elif kob==1:
                                if l<10:
                                    kob1=kob1-intel
                                elif 9<l<20:
                                    crit=rnd.randint(1, 10)
                                    if crit==10:
                                        kob1=kob1-2*intel
                                        print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1=kob1-intel
                                elif 19<l<30:
                                    crit=rnd.randint(1, 10)
                                    if crit>=7:
                                        kob1=kob1-2*intel
                                        print("You shout a bit higher than usual, scaring the kobolds. They were unable to reduce the attack and it did double the damage!")
                                    else:
                                        kob1=kob1-intel
                                if kob1<=0:
                                    print("Congratulations, you have killed a kobold. You received 15XP")
                                    XP+=15
                                    kob-=1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        if kob1>0:
                            print(f"The kobold has {kob1}HP remaining")
                            if kob>1:
                                print(f"The other kobolds have {kob2}HP remaining")
                        at=kob*3
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
        elif story_2=='Dungeon':
            zomb=rnd.randint(3,6)
            d=0
            c=0
            b=0
            if zomb>=3:
                zomb1=HPzombie
                zomb2=HPzombie
                zomb3=HPzombie
            if zomb>=6:
                zomb6=HPzombie
                d=1
            elif zomb>=5:
                zomb5=HPzombie
                c=1
            elif zomb==4:
                zomb4=HPzombie
                b=1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to a beginner dungeon.")
            print("You arrive at a dungeon where many beginners meet up to start a new adventure.")
            print(f"While walking around in the dungeon, you find a small group of {zomb} zombies.")
            while zomb>0:
                if classes==1:
                    attack=str(input(f"What attack will you use first? {Skills}: "))
                    if attack=='Fireball' and MPh>=2:
                        zomb1-=2*intel
                        MPh-=2
                        if zomb1<=0:
                            print("Congratulations, you have killed a zombie. You received 10XP")
                            XP+=10
                            zomb-=1
                            if zomb<=5:
                                d-=1
                                zomb1=zomb6
                            if zomb<=4:
                                c-=1
                                zomb1=zomb5
                            if zomb<=3:
                                b-=1
                                zomb1=zomb4
                            if zomb==2:
                                zomb1=zomb3
                            if zomb==1:
                                zomb1=zomb2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif gob1>0:
                            print(f"The zombie has {zomb1} remaining")
                        at=zomb*2
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
                    elif attack=='Heal' and MPh>=3:
                        HPh+=50
                        MPh-=3
                        if HPh>maxHP:
                            HPh=maxHP
                        else:
                            HPh=HPh
                        at=zomb*2
                        HPh-=at
                        print(f'HP: {HPh}')
                    elif attack=='Electrocute' and MPh>=3:
                        MPh-=3
                        if d==1:
                            zomb6=zomb6-intel
                            if zomb6<=0:
                                print("Congratulations, you have killed 6 zombies. You received 60XP")
                                XP+=60
                                zomb-=6
                                zomb1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif c==1:
                            zomb5=zomb5-intel
                            if zomb5<=0:
                                print("Congratulations, you have killed 5 zombies. You received 50XP")
                                XP+=50
                                zomb-=5
                                zomb1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==1:
                            zomb4=zomb4-intel
                            if zomb4<=0:
                                print("Congratulations, you have killed 4 zombies. You received 40XP")
                                XP+=40
                                zomb-=4
                                zomb1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==0 and c==0 and d==0:
                            if zomb==3:
                                zomb1-=intel
                                g()
                            if zomb==2:
                                zomb1-=intel
                                if zomb1<=0:
                                    print("Congratulations, you have killed 2 zombies. You received 20XP")
                                    XP+=20
                                    zomb-=2
                                    zomb2-=intel
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            if zomb==1:
                                zomb1-=intel
                                if zomb1<=0:
                                    print("Congratulations, you have killed a zombie. You received 10XP")
                                    XP+=10
                                    zomb-=1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        if zomb1>0:
                            print(f"The zombie has {zomb1}HP remaining")
                            if zomb>1:
                                print(f"The other zombies have {zomb2}HP remaining")
                        at=zomb*2
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
        elif story_2=='Plains':
            slime=rnd.randint(6, 9)
            d=0
            c=0
            b=0
            if slime>=6:
                slime1=HPslime
                slime2=HPslime
                slime3=HPslime
                slime4=HPslime
                slime5=HPslime
                slime6=HPslime
            if slime>=9:
                slime9=HPslime
                slime8=HPslime
                slime7=HPslime
                d=1
            elif slime>=8:
                slime8=HPslime
                slime7=HPslime
                c=1
            elif slime==7:
                slime7=HPslime
                b=1
            print("You have set out on your adventure.")
            print("After a moment of thinking, you decide to go to a plain.")
            print("You arrive at a wide plain where you can easily perceive monsters.")
            print(f"You perceive {slime} slimes. You engage in a combat.")
            while slime>0:
                if classes==1:
                    attack=str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                    if attack=='Fireball' and MPh>=2:
                        slime1-=2*intel
                        MPh-=2
                        if slime1<=0:
                            print("Congratulations, you have killed a slime. You received 2XP")
                            XP+=2
                            slime-=1
                            if slime==8:
                                d-=1
                                slime1=slime9
                            if slime==7:
                                c-=1
                                slime1=slime8
                            if slime==6:
                                b-=1
                                slime1=slime7
                            if slime==5:
                                slime1=slime6
                            if slime==4:
                                slime1=slime5
                            if slime==3:
                                slime1=slime4
                            if slime==2:
                                slime1=slime3
                            if slime1==1:
                                slime1=slime2
                            lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif slime1>0:
                            print(f"The slime has {slime1} remaining")
                        ac=rnd.randint(1,10)
                        if ac==10:
                            at=slime*5
                        elif 0<ac<10:
                            if slime==2 or slime==4 or slime==6 or slime==8:
                                at=slime*0.5
                            else:
                                at=(slime*0.5)+0.5
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
                    elif attack=='Heal' and MPh>=3:
                        HPh+=50
                        MPh-=3
                        if HPh>maxHP:
                            HPh=maxHP
                        else:
                            HPh=HPh
                        ac=rnd.randint(1,10)
                        if ac==10:
                            at=slime*5
                        elif 0<ac<10:
                            if slime==2 or slime==4 or slime==6 or slime==8:
                                at=slime*0.5
                            else:
                                at=(slime*0.5)+0.5
                        HPh-=at
                        print(f'HP: {HPh}')
                    elif attack=='Electrocute' and MPh>=3:
                        MPh-=3
                        if d==1:
                            slime9=slime9-intel
                            slime8=slime9
                            slime7=slime9
                            slime6=slime9
                            slime5=slime9
                            slime4=slime9
                            slime3=slime9
                            slime2=slime9
                            if slime9<=0:
                                print("Congratulations, you have killed 9 slimes. You received 18XP")
                                XP+=18
                                slime-=9
                                slime1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif c==1:
                            slime8=slime8-intel
                            slime7=slime8
                            slime6=slime8
                            slime5=slime8
                            slime4=slime8
                            slime3=slime8
                            slime2=slime8
                            if slime8<=0:
                                print("Congratulations, you have killed 8 slimes. You received 16XP")
                                XP+=16
                                slime-=8
                                slime1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==1:
                            slime7=slime7-intel
                            slime6=slime7
                            slime5=slime7
                            slime4=slime7
                            slime3=slime7
                            slime2=slime7
                            if slime7<=0:
                                print("Congratulations, you have killed 7 slimes. You received 14XP")
                                XP+=14
                                slime-=7
                                slime1=0
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        elif b==0 and c==0 and d==0:
                            if slime==6:
                                slime1-=intel
                                slime2-=intel
                                slime3-=intel
                                slime4-=intel
                                slime5-=intel
                                slime6-=intel
                                if slime1<=0 and slime2<=0 and slime3<=0:
                                    print("Congratulations, you have killed 6 slimes. You received 12XP")
                                    XP+=12
                                    slime-=6
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            if slime==5:
                                slime1-=intel
                                slime2-=intel
                                slime3-=intel
                                slime4-=intel
                                slime5-=intel
                                if slime1<=0 and slime2<=0 and slime3<=0 and slime4<=0 and slime5<=0:
                                    print("Congratulations, you have killed 5 slimes. You received 10XP")
                                    XP+=10
                                    slime-=5
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            if slime==4:
                                slime1-=intel
                                slime2-=intel
                                slime3-=intel
                                slime4-=intel
                                if slime1<=0 and slime2<=0 and slime3<=0 and slime4<=0:
                                    print("Congratulations, you have killed 4 slimes. You received 8XP")
                                    XP+=8
                                    slime-=4
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            if slime==3:
                                slime1-=intel
                                slime2-=intel
                                slime3-=intel
                                if slime1<=0 and slime2<=0 and slime3<=0:
                                    print("Congratulations, you have killed 3 slimes. You received 6XP")
                                    XP+=6
                                    slime-=3
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            elif slime==2:
                                slime1-=intel
                                slime2-=intel
                                if slime2<=0 and slime1<=0:
                                    print("Congratulations, you have killed 2 slimes. You received 4XP")
                                    XP+=4
                                    slime-=2
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                            elif slime==1:
                                slime1-=intel
                                if slime1<=0:
                                    print("Congratulations, you have killed a slime. You received 2XP")
                                    XP+=2
                                    slime-=1
                                    lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        if slime1>0:
                            print(f"The slime has {slime1}HP remaining")
                            if slime>1:
                                print(f"The other slimes have {slime2}HP remaining")
                        ac=rnd.randint(1,10)
                        if ac==10:
                            at=slime*5
                        elif 0<ac<10:
                            if slime==2 or slime==4 or slime==6 or slime==8:
                                at=slime*0.5
                            else:
                                at=(slime*0.5)+0.5
                        HPh-=at
                        print(f'HP: {HPh}')
                        if HPh<=0:
                            print("Game Over")
                            break
    if lvl==10:
        print("You have met your first boss, a Goblin King")
        mgob=3
        mgob1=50
        mgob2=mgob1
        mgob3=mgob1
        print(f"There are 3 mage goblins with him")
        while gob>0:
            if classes==1:
                attack=str(input(f"What attack will you use? {Skills} MP:{MPh}: "))
                if attack=='Fireball' and MPh>=2:
                    gob1=HPg-2*intel
                    MPh-=2
                    if mgob1<=0:
                        print("Congratulations, you have killed a goblin. You received 7XP")
                        XP+=7
                        mgob-=1
                        if mgob==2:
                            mgob1=mgob3
                        if mgob==1:
                            mgob1=mgob2
                        lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                    elif mgob1>0:
                        print(f"The goblin has {gob1} remaining")
                    at=mgob*5
                    HPh-=at
                    print(f'HP: {HPh}')
                    if HPh<=0:
                        print("Game Over")
                        break
                elif attack=='Heal' and MPh>=3:
                    HPh+=50
                    MPh-=3
                    if HPh>maxHP:
                        HPh=maxHP
                    else:
                        HPh=HPh
                    at=mgob*5
                    HPh-=at
                    print(f'HP: {HPh}')
                elif attack=='Electrocute' and MPh>=3:
                    MPh-=3
                    if mgob==3:
                        mgob1-=intel
                    if mgob1<=0:
                        print("Congratulations, you have killed 3 mage goblins. You received 60XP")
                        XP+=21
                        mgob-=3
                        mgob2-=intel
                        lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        if mgob==2:
                            mgob1-=intel
                            if mgob1<=0:
                                print("Congratulations, you have killed 2 mage goblins. You received 40XP")
                                XP+=14
                                mgob-=2
                                mgob2-=intel
                                lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp=g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                        if mgob==1:
                            mgob1-=intel
                            if gob1<=0:
                                print("Congratulations, you have killed a mage goblin. You received 20XP")
                                XP+=7
                                mgob-=1
                                g(lvl, XP, maxXP, HPh, maxHP, MPh, maxMP, s, intel, a, st, l, usp)
                    if gob1>0:
                        print(f"The goblin has {mgob1}HP remaining")
                        if gob>1:
                            print(f"The other goblins have {mgob2}HP remaining")
                    at=gob*1
                    HPh-=at
                    print(f'HP: {HPh}')
                    if HPh<=0:
                        print("Game Over")
                        break
    while 10<lvl<20:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    if lvl==20:
        print("You have met your second boss, a Spider Queen")
    while 20<lvl<30:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    while 30<lvl<40:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    while 40<lvl<50:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    while 50<lvl<60:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    while 60<lvl<70:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    while 70<lvl<80:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    while 80<lvl<90:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    while 90<lvl<100:
        story_2=str(input("Where will you go on your adventure? Mountain, Forest, Dungeon or Plains: "))
        if story_2==1:
            print("You have set out on a new adventure.")
        if story_2==2:
            print("You have set out on a new adventure.")
        if story_2==3:
            print("You have set out on a new adventure.")
    if lvl==100:
        print("You have arrived to the Demon king's palace.")