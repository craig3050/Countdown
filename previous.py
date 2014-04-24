from random import randint

def check_target(list):
    x = len(list)
    count = 1
    total = list[0]
    final_list = [total]
    while count < x:
        op = operator()
        second = list[count]
        total = takes_two(total,second,op)
        count += 1
        final_list.append(op)
        final_list.append(second)
        final_list.append(" = ")
        final_list.append(total)
    return (total, final_list)

def takes_two(a,b,c):
    if c == "addition":
        return a + b
    if c == "subtraction":
        return a - b
    if c == "multiplication":
        return a * b
    if c == "division":
        return a / b


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

print check_target([2,4,6,8,10,12])
