#!/usr/bin/python
#qpy:console

from random import randint, choice
from datetime import datetime


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
    return choice(("addition", "subtraction", "division", "multiplication"))


def takes_two(a, b, operation):
    operations  = {"addition": float(a + b),
                   "subtraction": float(a - b),
                   "multiplication": float(a * b),
                   "division": float(a / b)}
    return operations[operation]

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

        final_list.extend((op, second, " = ", float(total)))
    return (total, final_list)




def main():

    print "********************************"
    print "*** Welcome to the Countdown ***"
    print "***   Number Puzzle Solver   ***"
    print "********************************"

    numbers_dictionary = {} # Empty

    prompts = ["first", "second",
              "third", "fourth",
              "fifth", "sixth"]
    for i, prompt in enumerate(prompts, start=1):
        full_prompt = "Enter {} number:".format(prompt)
        numbers_dictionary[i] = raw_input(full_prompt)

    target = int(raw_input("Enter the Target Number: "))
    startTime = datetime.now()
    total = 0

    while target != total:
        num_to_try = randint(1,6)
        (total , final_list) = check_target(return_list(num_to_try,numbers_dictionary))
        print total


    print final_list
    print(datetime.now()-startTime)

if __name__ == '__main__':
    main()
