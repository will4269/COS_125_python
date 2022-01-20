f=open('cases_by_county.csv','r')
read_list=f.readlines()
del read_list[0]
split_list=[]
for i in range(len(read_list)):
    split_list.append(read_list[i].split(','))
    split_list[i][6].strip('\n')
    print(split_list[i][2], int(split_list[i][6])/int(split_list[i][3]), "%")
#2021-03-17,2021-03-16,Penobscot,4257,87,973,187
