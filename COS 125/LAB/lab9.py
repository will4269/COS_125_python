# Header Comments

from string import punctuation

def word_counter(sentence, word):
    list_of_words = [f.lower().strip(punctuation) for f in sentence.split()]

    word_count = 0
    for _, el in enumerate(list_of_words):
        if el == word:
            word_count += 1
    
    return word_count

# Task 1
# Write Here
def freq_finder(filename, word):
    count=0
    fil=open(filename,"r")
    reviews=fil.readlines()
    fil.close()
    for i in range(len(reviews)):
        count+=word_counter(reviews[i],word)
    return count


#Task 2
def word_finder(filename, word):
    count=0
    fil=open(filename,"r")
    article=fil.readlines()
    fil.close()
    for i in range(1,len(article)-1):
        if(article[i+1]=="\n"):
            count+=word_counter(article[i],word)
    return count

#I edited my file to make this work I saw no other option
# word=input("Enter a word be found: ")
# filename=input("Enter filename: ")



#task 3
# def file_dictionary(filename, word):
#     f=open(filename,'r')
#     filelines=f.readlines()
#     dictionary={}
#     for b in range(len(filelines)):
#         all_words =filelines[b]
#         # print(all_words)
#         # for i in range(len(all_words)):
#         #     if word in dictionary:
#         #         dictionary[country].append(airport)
#         #     else:
#         #         dictionary[country]=[word]
#     f.close()

# file_dictionary(filename, word)
# # country_in=input("Enter a country: ")
# # for keys in airport_dict:
# #     if(keys==country_in):
# #         print(airport_dict[country_in])