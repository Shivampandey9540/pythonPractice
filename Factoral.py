
# only  available to positive
# for negtive = NO
# for 0 : 1
# for example : 5

# first method
# 1*2*3*4*5
# second method
# 5*4*3*2*1

# number = 8
# factorial = 1
# if number < 0:
#     print("we don't  colculate negative factorials")
# elif number == 0:
#     print("this  result is 1 ")
# else:
#     for i in range(1, number + 1):
#         factorial = factorial * i
#     print("the Result is ", factorial)

number = 8

valuecheck = number

if number < 0:
    print("negitive value don't have factorial")
elif number == 0:
    print("The factorial is 1")
else:
    for i in range(1, number+1):
        number = number-1
        taken = number
        if (taken == 0):
            break
        valuecheck = valuecheck * taken
    print(valuecheck)
