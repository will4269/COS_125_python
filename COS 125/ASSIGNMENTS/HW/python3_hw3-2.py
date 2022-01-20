#part 2
z=0
c=int(0)
retry="pp"
num =int(input("Enter starting number: "))
while(1):
    z=0
    p = input("Enter a Divisor or 'p'")
    for c in range(int(2),int(num),int(1)):
        if(num%c==0):
            z=z+1
    if(p=="p"):
        if(z>0):
            print("you were wrong ", num, "is not prime")
            retry =input("If you want to play again type either 'y' or 'n'")
        elif(z==0):
            print("you win")
            retry =input("If you want to play again type either 'y' or 'n'")
    else:
        print(num, "divided by ", p, "is ", num/int(p))
        if((num/int(p))!=int((num/int(p)))):
            print("you lose you divided by a bad divisor")
            retry =input("If you want to play again type either 'y' or 'n'")
        if(z==0):
            print("you lose you divided a prime number")
            retry =input("If you want to play again type either 'y' or 'n'")

        num= int(num/int(p))

           
    if (retry=="y"):
        num = float(input("Enter starting number: "))
        retry="pp"
    elif(retry=="n"):
        print("bye bye")
        break

