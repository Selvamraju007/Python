"""
Print the multiplication table of a given number using “for” and “while” loops.
"""



num = int(input("Display multiplication table of? "))
i = 0
while i < 11:
    print(num,'x',i,'=',num*i)
    i = i+1
