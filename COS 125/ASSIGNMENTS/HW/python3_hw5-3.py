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



while(1):
    complete=[]
    sum_score=0
    sum_roll=0
    largest_score=0
    highest_rolls=0
    score_index=0
    roll_index=0
    number_of_games=int(input("Enter Number of games: "))
    for count in range(0,number_of_games,1):
        dice_roll=dice(5,6)
        net_total=0
        rolls=1
        while((len(dice_roll)>0) and ((dice_roll[0]!=2)or(dice_roll[0]!=5))):
            dice_roll=num_remover(dice_roll)
            net_total=net_total+total(dice_roll)
            for i in range(0,len(dice_roll),1):
                dice_roll[i]=random.randint(1,int(6))
            rolls+=1
        complete.append(rolls)
        complete.append(net_total) 
    for score in range(1,len(complete),2):
        sum_score=sum_score+complete[score]
        if(complete[score]>largest_score):
            largest_score=complete[score]
            score_index=score-1
    print("Avg score per game", sum_score/(len(complete)/2))
    for roll in range(0,len(complete),2):
        sum_roll=sum_roll+complete[roll]
        if(complete[roll]>highest_rolls):
            highest_rolls=complete[roll]
            roll_index=roll+1
    print("Avg roll per game", sum_roll/(len(complete)/2))
    print("max score in one game with rolls",largest_score,complete[score_index])
    print("max rolls in one game with score",highest_rolls, complete[roll_index])
    while(1):
        higher=0
        sample_score=int(input("Enter sample score: "))
        if(sample_score==-1):
            break
        for scores in range(1,len(complete),2):
            if(complete[scores]>sample_score):
                higher+=1
        probability=((higher/(len(complete)/2)))*100
        print("The probability of being higher than sample score is", probability,"%")
        
    break
