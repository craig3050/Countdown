#-------------------------------------------------------------------------------
# Name:        Countdown Number Puzzle Solver
# Purpose:
#
# Author:      Craig Cuninghame
#
# Created:     13/04/2014
# Copyright:   (c) Craig Cuninghame 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint


def return_list(num_to_try,numbers_dictionary):

    first = randint(1,6)
    list_fig = [int(numbers_dictionary[first])]
    called = [first]
    x = 1
    while x < num_to_try:
            y = randint(1,6)
            if y not in called:
                list_fig.append(int(numbers_dictionary[y]))
                called.append(y)
                x += 1
    return list_fig


def operator():
    x = randint(1,4)
    if x == 1:
        return "addition"
    if x == 2:
        return "subtraction"
    if x == 3:
        return "multiplication"
    if x == 4:
        return "division"


def takes_two(a,b,c):
    if c == "addition":
        return float(a + b)
    if c == "subtraction":
        return float(a - b)
    if c == "multiplication":
        return float(a * b)
    if c == "division":
        return float(a / b)


def check_target(list):
    x = len(list)
    count = 1
    total = list[0]
    final_list = [float(total)]
    while count < x:
        op = operator()
        second = list[count]
        total = takes_two(total,second,op)
        count += 1
        final_list.append(op)
        final_list.append(second)
        final_list.append(" = ")
        final_list.append(float(total))
    return (total, final_list)




def main():

    print "********************************"
    print "*** Welcome to the Countdown ***"
    print "***   Number Puzzle Solver   ***"
    print "********************************"

    numbers_dictionary = {} # Empty

    numbers_dictionary[1] = raw_input("Enter first number")
    numbers_dictionary[2] = raw_input("Enter second number")
    numbers_dictionary[3] = raw_input("Enter third number")
    numbers_dictionary[4] = raw_input("Enter fourth number")
    numbers_dictionary[5] = raw_input("Enter fifth number")
    numbers_dictionary[6] = raw_input("Enter sixth number")
    target = int(raw_input("Enter the Target Number"))
    total = 0

    while target != total:
        num_to_try = randint(1,6)
        (total , final_list) = check_target(return_list(num_to_try,numbers_dictionary))
        print total

    print total
    print final_list

if __name__ == '__main__':
    main()
