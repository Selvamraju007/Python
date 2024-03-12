"""
Print the multiplication table of 17
"""

def print_mtable(num):
    print(f"table of {num} is ...")
    for index in range(1,11):
        print(f"{num} * {index} = {num* index}")

number = int(input("Enter a Number :"))
    

# Main starts from here
print_mtable(number)
    
  
