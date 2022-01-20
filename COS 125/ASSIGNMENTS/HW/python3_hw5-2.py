# NAME: William Poole
# ASSIGNMENT: hw5
# COLLABORATION: none

#Drop Dead

import random
def dice(num_dice, dice_amt):
    list=["empty"]*int(num_dice)
    for i in range(0,len(list),1):
        list[i]=random.randint(1,int(dice_amt))
    return list

def num_remover(list):
    for i in range(0,len(list),1):
        if 2 in list:
            list.remove(2)
        if 5 in list:
            list.remove(5)
    return list

def total(list):
    total=0
    for i in range(0,len(list),1):
        total=total+list[i]
    return total


score=[]
highest=0
place1=0
while(1):
    print("-"*len("Welcome to Drop Dead"))
    print("Welcome to Drop Dead")
    players=input("How many players? ")
    print("-"*len("Welcome to Drop Dead"))
    for count in range(1,int(players)+1,1):
        dice_roll=dice(5,6)
        net_total=0
        rolls=1
        while((len(dice_roll)>0) and ((dice_roll[0]!=2)or(dice_roll[0]!=5))):
            dice_roll=num_remover(dice_roll)
            net_total=net_total+total(dice_roll)
            for i in range(0,len(dice_roll),1):
                dice_roll[i]=random.randint(1,int(6))
            rolls+=1
        score.append(net_total)    
        print("Player ",count,": ",net_total, " in ", rolls," rolls.",sep="") 
        players=int(players)+1
    for place in range(0,len(score),1):
        if(int(score[place])>highest):
            highest=score[place]
            place1=place+1
    print("All players have dropped dead.")
    print("Player", place1, "wins.")
    print("-"*len("Welcome to Drop Dead"))
    break
