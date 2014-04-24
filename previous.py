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

def main():
    from random import randint


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
    target = raw_input("Enter the Target Number")

    while total != target:
# Step 1 - How many numbers do we want to try
        num_to_try = randint(1,6)
        check_target(return_list(num_to_try))


# Step 2 - Call that many numbers out of our list
def return_list(x):
    list = [numbers_dictionary[randint(1,6)]]
    x = 0
    for num in x:
        #Call num_to_try random numbers
        while False:
        #Call a random value from dictionary
            y = randint(1,6)
        #Check if already been called
        #if called retry a different number, if not add to list
            if y in list:
                return False
            else:
                list.append(numbers_dictionary[y])
                return True
    return list

# Step 3 - function to generate random Add/Subtract/Multiply/Divide
def operator():
    x = randint(1,4)
    if x == 1:
        return addition
    if x == 2:
        return subtraction
    if x == 3:
        return multiplication
    if x == 4:
        return division

# Step 4 - Add / Subtract / divide / multiply and
def takes_two(a,b,c):
    if c == "addition":
        return a + b
    if c == "subtraction":
        return a - b
    if c == "multiplication":
        return a * b
    if c == "division":
        return a / b

#see if it matches target
def check_target(list):
    #1 op 2 op 3 op 4 op 5 op 6 or however many there are
    x = len(list)
    count = 1
    total = list[0]
    final_list = [total]
    while count < x:
        op = operator()
        total = takes_two(total,list[count],op)
        count += 1
        final_list.append(op)
        final_list.append(total)
    if total == target:
        print final_list
        return total
    else:
        return total


# Step 5 - if matches print finished & last file entry, if not retry with different combination









if __name__ == '__main__':
    main()
