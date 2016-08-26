import os


dictionary = open('Dict.txt', 'r')     
print ("Welcome to Craig's Countdown Words solving tool!!")
cdwords = input("Enter all the letters as one big word")
word_length = len(cdwords) + 1

word_list = {}

for words in dictionary:
    if len(words) <= word_length:
        letter_count = 0
        for letters in cdwords:
            if letters in words:
                letter_count += 1
        word_list[words] = letter_count
        ##print (words + " " + str(letter_count))
    
word_list = sorted(word_list, key=word_list.__getitem__, reverse = True)
print (word_list)




   



