""" 
    print the multiplication table 
           of any number desired by the user
"""

def get_number():   
    number = int(input("Enter a number :")) 
    return number


def print_mtable(num):
    print(f"table of {num} is ...")
    for index in range(1,11):
        print(f"{num} * {index} = {num* index}")    
   

def main():   
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()
