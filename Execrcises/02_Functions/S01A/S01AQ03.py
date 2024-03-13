""" 
     print the multiplication table 
           of any number desired by the user
"""

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    number = int (input("Enter number "))# Write code to prompt the user for a number
    # Check out your code behaviour by commenting the line below
    #number = int(number) # What happens if you dont perform this operation ?
    return number


def print_mtable(n):
    """ 
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """
    # Your solution code goes in here
    for i in range(1,11):
        # multiples from 1 to 10
        print ("%d * %d = %d" % (n, i, n * i))
    

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()
