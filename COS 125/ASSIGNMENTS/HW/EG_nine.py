print("You walk to the edge of the forest and arrive on a fork.")
path=input("Enter (1) or (2) to go left or right respectively.")
option=input("Enter a number between 1-7.")
path=int(path)
option=int(option)
if(path==1):
    print("You arrived at an abandoned mine.")
    if(option==1):
        print("You looked around and found out the mine is unstable.")
    if(option==2):
        print("You looked around and found a strange book in a building. (+1 strange book)")
    if(option==3):
        print("You noticed a TNT detonator pressed with a wire leading into the abandoned mine shaft. (Quest started: Deep Dark Boom)")
    if(option==4):
        print("You noticed foot steps heading back towards the path. (Quest started: Hidden in Stone)")
    if(option==5):
        print("You notice an animal caught in some rubble.")
    if(option==6):
        print("You have found 100 GP. (+100 GP)")
    if(option==7):
        print("you find a man sobbing near the enterance of the cave.")
if(path==2):
    print("You arrived in a strange ghost town.")
    if(option==1):
        print("You notice a strange rune on a pillar. (ten rodents of unusual size spawn)")
    if(option==2):
        print("You notice a stone door left open. (Quest started: Mystic Hideway)")
    if(option==3):
        print("You find a stone button near an gazeboo. (Quest avaliable: A strange trip)")
    if(option==4):
        print("You fall down into a collapsed underground area. (Begin ruin combat 1)")
    if(option==5):
        nory=input("You found an ancient gem locked in a statue, do you take it out (y) or (n).")
        if(nory=="y"):
            print("A grinding of bones can be heard. (Begin ruin combat 2) (One Gem added)")
        else:
            print("you walk away.")
    else:
        print("You find nothing but an empty book. (+1 empty book)")


