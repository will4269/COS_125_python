# NAME: William Poole
# ASSIGNMENT: Hw6
# COLLABORATION: none

###############################################################################
# HW6 - COS125
# DUE: 3-19-21 at Midnight
#
# This is the starter file for HW6. It contains the data necessary to do
# the homework. You should add your code below.
###############################################################################

###############################################################################
# Data Key:
#   Name: First middle last. Might have a middle name, might not.
#   Birthday: in form Day/Month/Year
#   ID: starts with ss. Followed by four numbers.
#   Sales: 
#       fX - number of refrigerators sold
#       sX - number of stoves sold
#       mX - number of microwaves sold
#   Kilometers: Number of kilometers the salesperson drove. Xkm
###############################################################################

###############################################################################
# Instructions:
#   - Your program will accept two commands: 'b' and 'p'. Each command
#       will print infomation to the terminal in a tabular form. The program
#       should provide a simple main menu and ask for a command. 
#       It should create and print the required information. 
#       It does not need a loop. It should run once and quit.
#       It should ignore invalid commands.
#       The data in the tuple has a specific format. Look at it closely
#       before you start programming and take note of which symbols partition
#       the data.
#
#   - IMPORTANT: Your program must do all the work of slicing, combining and 
#       calculating the data, not you. This means, you
#       cannot type out a new tuple, list, etc. with the correct information. 
#       This will result in an automatic zero.
#
#   - 'b' stands for birthday. For this command your program will generate
#       from the data below a list of employee birthdays without the year.
#       The output should be in neat columns that are wide enough to print
#       the longest name. The name printed should be the first name. Day and
#       month should both be two digits (add zeros where necessary).
#       Example:
#           NAME        MONTH   DAY
#           Sabrina     01      03
#           Fergus      11      21
#           etc...
#
#   - 'p' stands for payday. This command calculates the monthly commission
#       each salesperson gets based on their sales and kilometers driven.
#       The formula is: commission = 
#           refrigerators * 50 + 
#           stoves * 75 +
#           microwaves * 25 +
#           kilometers * 0.5
#       The data should be printed in the following form. Again it should be
#       in neat columns.
#           ID      LAST    F   COMMISSION   
#           9387    BRYAN   S   $599.50
#           5246    ARCHER  F   $326.00
#           etc...
#       Note: the ID is just the numeric part. The last name is in ALL CAPS.
#           The commission amount has a $ and two decimal digits.
#
###############################################################################

data = (
    ('Sabrina Bryan,1/3/98,ss9387,f9;s1;m1,99km'),
    ('Fergus Connon Archer,11/21/89,ss5246,f1;s3,102km'),
    ('Adrian Harvey,3/3/78,ss1654,m5;s2,72km'),
    ('Patricia Abigail Wolf,9/5/00,ss0936,f3;s4;m8,134km'),
    ('Georgina Kramer,6/15/95,ss4837,f5;s2;m1,55km'),
    ('Glenn Julian Ayala,3/19/90,ss3689,s4;f3,152km'),
    ('Anita Davila,6/27/91,ss9367,f8,203km'),
    ('Gertrude Nunez,1/12/97,ss3948,s3;m1,34km'),
    ('Solomon Burton,8/5/88,ss7364,s2;f1,23km'),
    ('Rafael John Murray,10/19/01,ss9105,s9;f3,78km')
)

###############################################################################
# YOUR CODE GOES HERE
def birthday(data):
    index_longest_name=0
    length_name=[]
    names=[]
    begin_month=[]
    end_month=[]
    end_day=[]
    list_data=list(data)
    for i in range(len(list_data)): #finds longest first name
        if(index_longest_name<list_data[i].find(" ")):
            index_longest_name=list_data[i].find(" ") #stores max length
        length_name.append(list_data[i].find(" ")) #stores length of all first names
        begin_month.append(list_data[i].find(",")+1)
        end_month.append(list_data[i].find("/"))  
        end_day.append(list_data[i].index("/",end_month[i]+1))
    index_longest_name+=2
    print(f'{"Name":<{index_longest_name}}{"Month":<8}{"Day"}')
    for b in range(len(length_name)):
        names.append(data[b][0:length_name[b]]) #makes list of names
        if(begin_month[b]+1==end_month[b]):
            if(end_month[b]+2==end_day[b]):
                print(f'{names[b]:<{index_longest_name}}{"0"+ list_data[b][begin_month[b]]:<8}{"0"+list_data[b][end_month[b]+1]}')
            else:
                print(f'{names[b]:<{index_longest_name}}{"0"+ list_data[b][begin_month[b]]:<8}{list_data[b][end_month[b]+1:end_day[b]]}')
        else:
            if(end_month[b]+2==end_day[b]):
                print(f'{names[b]:<{index_longest_name}}{list_data[b][begin_month[b]:end_month[b]]:<8}{"0"+list_data[b][end_month[b]+1]}')
            else:
                print(f'{names[b]:<{index_longest_name}}{list_data[b][begin_month[b]:end_month[b]]:<8}{list_data[b][end_month[b]+1:end_day[b]]}')
    return "success"    

def payroll(data):
    index_longest_name=0
    begin_last_name=[]
    end_last_name=[]
    begin_id=[]
    kilometer_end=[]
    kilometer_begin=[]
    stove_begin=[]
    s=[]
    f=[]
    m=[]
    commission=[]
    list_data=list(data)
    for i in range(len(list_data)): #generates index of last name beginning and end
        end_last_name.append(list_data[i].find(","))
        begin_id.append(list_data[i].find("ss")) #finds ID while looking
        kilometer_end.append(list_data[i].find("km")) #End of kilometers
        stove_begin.append(list_data[i][begin_id[i]+2:len(list_data)].find("s"))
        b=end_last_name[i]-1
        j=kilometer_end[i]-2
        item_type=begin_id[i]+7
        s=0
        f=0
        m=0
        while(list_data[i][b:end_last_name[i]].islower()==True): #finds beginning of last name
            b-=1
            if(b<6):
                break
        begin_last_name.append(b)
        if((end_last_name[i]-b)>index_longest_name):
            index_longest_name=(end_last_name[i]-b)
        while(list_data[i][j:kilometer_end[i]].isnumeric()==True):#finds beginning of kilometer
            j-=1
            if(kilometer_end[i]-j>8):
                break
        kilometer_begin.append(j+1)
        while(list_data[i][item_type].isalpha()==True):
            sum_string=""
            if(list_data[i][item_type]=="f"): #detects length of fridge number and stores it
                item_type+=1
                while(list_data[i][item_type].isnumeric()==True):
                    sum_string+=list_data[i][item_type]
                    item_type+=1
                f=(int(sum_string))
            if(list_data[i][item_type]=="s"): #detects length of stoves number and stores it
                item_type+=1
                while(list_data[i][item_type].isnumeric()==True):
                    sum_string+=list_data[i][item_type]
                    item_type+=1
                s=(int(sum_string))
            elif(list_data[i][item_type]=="m"): #detects length of microwaves number and stores it
                item_type+=1
                while(list_data[i][item_type].isnumeric()==True):
                    sum_string+=list_data[i][item_type]
                    item_type+=1
                m=(int(sum_string))
            item_type+=1
        commission.append(50*f+75*s+25*m+(.5*float(list_data[i][kilometer_begin[i]:kilometer_end[i]])))
    print(f'{"ID":<8}{"LAST":<{index_longest_name+2}}{"F":<3}{"COMMISSION"}') #HEADER
    for j in range(len(list_data)):
        if(j%2==0):
            print(f'{list_data[j][begin_id[j]+2:begin_id[j]+6]:<8}{list_data[j][begin_last_name[j]:end_last_name[j]].upper():<{index_longest_name+2}}{"S":<3}{"$"+str(commission[j]):^10}')
        else:
            print(f'{list_data[j][begin_id[j]+2:begin_id[j]+6]:<8}{list_data[j][begin_last_name[j]:end_last_name[j]].upper():<{index_longest_name+2}}{"F":<3}{"$"+str(commission[j]):^10}')
    return "success"


    
while(1): #Main 
    function_call=input("b(birthday) or p(payday): ")
    if(function_call=="b"): #calls for birthday
        print("Birthday selected")
        birthday(data)
    elif(function_call=="p"): #calls for payroll/payday
        "Payday selected"
        payroll(data)
    else:
        print("Error not a function")
        break