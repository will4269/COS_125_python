###################################33
# FILE IO
# NOTE: I have left most everything
#   commented out.
#####################################

######################################################################
# ANNOUNCEMENTS MONDAY
#   File IO this week. Monday & Wednesday
#   HW6: string manip due Friday.
#   Next week: No lab Tues -> Thursday everyone
#   Next week: No Wed lecture


######################################################################
# ANNOUNCEMENTS WEDNESDAY
#   HW6 Friday
#       - My error that's not really an error.
#   Book: Files Ch13
#   Friday: Review. Covered a lot. Bring your questions.
#   Monday: Debugger, and some other trash (Book APPENDIX A, too).
#   Friday: Dictionaries.
#   
#   And I will rerecord Monday.


######################################################################
# Where to put the file.

# In the same directory for now.


######################################################################
# Opening a file

# f = open('data.txt')

# print(f.closed)
######################################################################
# Closing a file

# f.close()


######################################################################
# Test if file is closed or open

# print(f.closed)


######################################################################
# Mode

# r: read
# w: write
# r+: read/write
# a: append

# f = open('data.txt','mode goes here')

######################################################################
# reading

# read()
# readline() -> limit param
# readlines() -> hint ?
# for-loop

# f = open('data.txt','r')

# for line in f:
#     print(line.strip())
#     f.readline()

# contents = f.read()
# print(contents)

# line = f.readline()
# line2 = f.readline()
# print(line, line2)

# contents = f.readlines()
# print(contents)

# for line in f:
#     print(line.strip())

# Use strip() to remove newlines

######################################################################
# writing
# mylist = ['hello','world','spam','eggs','foo']

# f = open('myfile.txt','w')

# for x in mylist:
#     f.write(x+"\n")

# f.writelines(mylist)

# f.close()

# Must add newlines

######################################################################
# seek
# Only from the start

# f = open('data.txt')

# line = f.readline()
# print(line)

# line = f.readline()
# print(line)

# f.seek(5)

# line = f.readline()
# print(line)


######################################################################
# tell

# f = open('data.txt')
# print(f.tell())

# line = f.readline()
# print(len(line))

# print(f.tell())


######################################################################
# try-except



# try:
#     f = open('data.txt')
#     f.close()
#     f.read()
# except IOError:
#     print("Did not find hello.txt file.")
# except ValueError:
#     print("Hello.txt is not open.")


######################################################################
# You must close your file handles.
# f = open('data2.txt','w')

# for i in range(10000):
#     f.write(str(i)+"\n")

# f.close()

# f2 = open('data2.txt','r')
# for l in f2:
#     print(l,end="")

# Read or write, close, open for some other purpose.
######################################################################
# Path

# Relative and Absolute Path

########################
# RELATIVE
# f = open('otherdata.txt')
# print(f.read())
# f.close()

# f = open('lab5/data.txt')
# print(f.read())
# f.close()


# f = open('../junk_java/Junk.java')
# print(f.read())
# f.close()
########################
# DO NOT USE ABSOLUTE PATHS FOR HW/Projects.
# ABSOLUTE
# f = open('/home/zax/Projects/Code/COS125LAB/fileIO/otherdata.txt')
# print(f.read())
# f.close()

# f = open('/home/zax/Projects/Code/COS125LAB/fileIO/lab5/data.txt')
# print(f.read())
# f.close()


# f = open('/home/zax/Projects/Code/COS125LAB/Junk.java')
# print(f.read())
# f.close()

######################################################################

# Enum
# import enum


# Enumerate


# Ternary Ops

