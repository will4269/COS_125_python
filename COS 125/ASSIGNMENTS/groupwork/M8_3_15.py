########################
# FILE IO - Revisited. #
########################

#########################
# Where to put the file

# Put in the same directory
#   as your code.

#########################
# Open
FILENAME = 'data.txt'



f = open(FILENAME)


#########################
# Mode

#'w' -> write
#'r+' -> read/write
#'r' -> read
#'a' -> append

#########################
# Close

f.close()

#########################
# Reading

# read() -> reads the entire file as a string.
# contents = f.read()
# print(contents)

# readline() -> reads a single line
# line = f.readline()
# print(line)

# readlines() -> reads the entire file
#   separates lines into individual strings
#   stores all the strings in list
# contents = f.readlines()
# print(contents)

# for loop method
# for line in f:
#     print(line.strip())

#########################
# Writing

# write() -> writes a string to the file.

# f = open('myfile.txt','w')
# f.write('hello world\n')

# var = "Hello world"
# f.write(var+"\n")

# var2 = 7
# f.write(str(var2)+"\n")

# f.close()

# f2 = open('myfile.txt','a')
# f2.write("This is appended to the file.\n")

#########################
# Extended Example

def AverageAge(data):
    total = 0
    for d in data:
        total += d[1]
    print("Avg age of all emps: ", total/len(data))


f = open('data.txt','r')
data_list = []

for line in f:
    data_list.append( line.strip().split() )

f.close()

for sublist in data_list:
    sublist[1] = int(sublist[1])
    sublist[2] = float(sublist[2])

AverageAge(data_list)


