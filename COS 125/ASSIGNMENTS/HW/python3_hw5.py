# NAME: William Poole
# ASSIGNMENT: hw5
# COLLABORATION: none

#Drop Dead

import random
def roller(num_dice, dice_amt):
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



while(1):
    net_total=0
    roll=1
    print("Welcome to Drop Dead")
    num_dice=(input("Enter the number of Dice: "))
    dice_amt=(input("Enter the dice amount (like 6 for a d6): "))
    dice_roll=roller(num_dice, dice_amt)
    print("here")
    while((len(dice_roll)>1)):
        print("Roll",roll,dice_roll,sep=" ",end=" ") 
        dice_roll=num_remover(dice_roll)
        net_total=net_total+total(dice_roll)
        print("-> Total =", net_total,sep=" ",end=" ")
        print()
        for i in range(0,len(dice_roll),1):
            dice_roll[i]=random.randint(1,int(dice_amt))
        roll+=1
    print("Net Total", net_total, "Number of rolls", roll)
            

