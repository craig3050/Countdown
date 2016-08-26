import os


def add_file():
    big_list = []
    write_list = ""
    for file_name in os.listdir(file_path):
       print(file_name)
       words = open(file_name)
       for item in words:
           big_list.append(item)
    big_list = sorted(big_list)#
    for item in big_list:
        write_list += item
    open('Dict.txt', 'w').write(write_list)        







print ("Welcome to Craig's add all text files to one big text file tool!\n\n")
file_path = input("Enter the Path Directory: ")
add_file()
