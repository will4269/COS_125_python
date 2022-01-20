# out put choose a door 1,2,3
# input (1,2,3)
#branch to doors
#open doors
user_input=0
print("Choose a door: 1,2, or 3")
user_input=input("Enter: ")
if user_input=="0":
    print("none selected")
elif user_input == "3":
    print("You win a goat.")
elif user_input =="2":
    print("You win $100.")
elif user_input =="1":
    print("you win a new computer.")

