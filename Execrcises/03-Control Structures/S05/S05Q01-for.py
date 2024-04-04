"""
Print the multiplication table of a given number using “for” and “while” loops.
"""

num = int(input("Display multiplication table of? "))
for i in range(12,22):
    print(num,'x',i,'=',num*i)
