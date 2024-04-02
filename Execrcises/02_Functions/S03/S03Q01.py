"""

Take 2 numbers from the user. 
Print which number is a 2 digit number, 
and which number is a 3 digit number. 
If it is neither, then print the number as it is

"""

# Implement the helper functions here

def perform_check(num1, num2):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    # Your solution code goes here
    # Invoke check_if_2digit and
    # check_if_3digit to check if the number
    # matches the criteria and print accordingly

    numbers = {num1, num2}
    for num in numbers:
        if num <= 9 :
            print("Number is single digit", num)
        elif num > 9 and num <= 99:
            print("Number is 2 digit", num)
        else:
            print("Number is 3 digit")         
            
            

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    number1 = int(input("Enter the number 1 "))
    number2 = int(input("Enter the number 2 "))
    return(number1, number2)

def main():
    '''
    Main function of the program
    '''
    (num1, num2) = get_number()
    perform_check(num1, num2)
    
# Main starts from here
main()
