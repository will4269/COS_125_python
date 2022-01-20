# NAME: William Poole
# ASSIGNMENT: hw4
# COLLABORATION: none
list=[]
listb=[]
quantity=[]
cost=[]

while(1):
    c=0.0
    cost_of_item=0
    action = input("(a) to add, (d) to delete, (p) prints, (q) quits, (s) swaps, (c) cost: ")
    if(action=="a"): #works
        print("a choosen")
        item= input("name of item: ")
        quantityb = int(input("How many?: "))
        if(item=="fish"):
            cost_of_item= quantityb*5
        elif(item=="hammer"):
            cost_of_item= quantityb*6
        elif(item=="crackers"):
            cost_of_item= quantityb*0.25
        elif(item=="salami"):
            cost_of_item= quantityb*5.50
        
        print("cost is $",cost_of_item)
        list.append(item)
        quantity.append(quantityb)
        cost.append(cost_of_item)
         
    if(action=="d"): #works
        print("d")
        print("please select index off of list range of 0 to,",len(list)-1, "use name to enter removal", list)
        number= int(input())
        if(number<=len(list)):
            print(list[number], "will be removed")
            list.pop(number)
            quantity.pop(number)
            cost.pop(number)
            print("index removed")
            print("new list:", list)
        else:
            print("error index entered as", number, "does not exist try again")
        
    if(action=="p"): #works
        print("p")
        i=0
        for i in range(0,len(list)):
            print("item:", i,list[i],",", "x",quantity[i],",","$",cost[i])          

    if(action=="q"): #works
        print(list)
        break

    if(action=="s"):
        print("s")
        a=int(input("first item to change: "))
        b=int(input("second item to change: "))
        listb.append(list[a])
        listb.append(quantity[a])
        listb.append(cost[a])
        listb.append(list[b])
        listb.append(quantity[b])
        listb.append(cost[b])
        list[a]=listb[3]
        list[b]=listb[0]
        quantity[a]=listb[4]
        quantity[b]=listb[1]
        cost[a]=listb[5]
        cost[b]=listb[2]
        listb.clear()

    if(action=="c"): #works
        print("c")
        i=0
        for i in range(0,len(cost)):
            c=c+cost[i]
        print("Net cost is $",c)

            
        

