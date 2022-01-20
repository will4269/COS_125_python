
#Password verification program

# ask for new password
new_password=input("Enter new password: ")

# try:

def passwordlength(password): #jakob check
    if(len(password) > 8 and len(password) < 32):
        
        return True
    else:
        print("failed the length test")
        return False 



def symbolcheck(password): #kempton check
    mylist = ['$', '#', '%', '?', '!']
    trueCount = 0
    for x in mylist:
        if x in password:       # if char in set is in pass
            trueCount +=1       # increment up counter
    if trueCount >= 2:      # if at least two
        return True             # check passed
    else:
        print("Password must include at least two characters from the set: $#%?!")
        return False

def numeric_check(password): #Apurba
    count = 0
    for i in range(len(password)):
        if(password[i].isdigit()==True):
            count += 1
    if count >= 2:
        return True
    else: 
        print('Password needs at least 2 numbers.')
        return False

def lower_check(password):#will check
    num=0
    for i in range(len(password)):
        if(password[i].islower()==True):
            num+=1
    if(num>=2):
        return True
    else:
        print("No capitals")
        return False

    
def upper_check(password): #erica check
    counter = 0
    for letter in range(len(password)):
        if(password[letter].islower()==True):
            counter+=1
    if counter >= 2:
        return True

def duplicateCheck(password): # Kempton
    characters = []
    for x in password:      # for each char in password
        if x in characters:     # if character is a duplicate
            print("Password cannot contain duplicate characters.")
            return False            # check failed
        else:
            characters.append(x)
    return True

def function_test(password):
    a=[True]*6
    a[0]=numeric_check(password)
    a[1]=symbolcheck(password)
    a[2]=upper_check(password)
    a[3]=lower_check(password)
    a[4]=duplicateCheck(password)
    a[5]=passwordlength(password)
    for i in range(len(a)):
        if(a[i]==False):
            return False
    return True

b=bool(1)
try:
    b=function_test(new_password)       
except b==False:
    print(fail)
