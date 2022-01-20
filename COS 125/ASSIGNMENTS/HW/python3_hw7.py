# NAME: William Poole
# ASSIGNMENT: HW7
# COLLABORATION: NONE

# new: ’n’ creates a new to-do list.
# load: ’l’ loads a to-do list.
# save: ’s’ saves the current to-do list.
# add: ’a’ adds an item to the to-do list.
# print: ’p’ prints the whole to-do list.\n\r
# quit: ’q’ quits the program. no function just break

listing=[1,5,3,2,5,4,7]
def sort(alist):
    for i in range(len(alist)-1):
        if(alist[i]>alist[i+1]):
            b=alist[i+1]
            alist[i+1]=alist[i]
            alist[i]=b
            return sort(alist)
    return alist[1]
