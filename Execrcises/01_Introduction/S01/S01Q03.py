"""
Modify program in S01Q02 to print the multiplication table 
of any number desired by the user
"""

num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
