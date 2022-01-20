#write a while loop that prints the powers of 2 from 2^0 to 2^20,inclusive
exponent = 0 #exponent of 2
while(exponent<=20): #up to 20
    print(2**exponent) #math to start at one
    exponent +=1 #up the counter


# end 1
user_input = str("p")
start = 0
end = 0

while user_input != "q":
   start = int(input("Enter a start integer: "))
   end = int(input("Enter an end integer: "))
   if (start >= end):
       print("start is larger or equal to end please make start smaller")
       end = int(input("Enter an end integer: "))
       start = int(input("Enter a start integer: "))
       while c=0:
           print("Sum :",start+end)
           c += c
