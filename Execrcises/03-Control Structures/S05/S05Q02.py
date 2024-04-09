"""
Ask the user to enter a number till he enters 0. 
Print the maximum and minimum values among all entered numbers. 
Print the number of single, two and three digit numbers entered.
"""


def minimum(mylist):
    print("The minimum number in the given list" , min(mylist))


def maximum(mylist):
    print("The maximum number in the given list" , max(mylist))


def digits(mylist):
    for i in mylist:
        if i <= 9:
            print("The given number is single digit")
        elif i > 9 and i <= 99:
            print("The given number is double digit")
        else:
            print("The given numver is three digit")



mylist = []
while True:
    num = int(input("Enter an integer (0 terminates): "))
    if num != 0:
        print(num)
        mylist.append(num)
        print(mylist)
    else:
        min(mylist)
        max(mylist)
        digits(mylist)
        break
