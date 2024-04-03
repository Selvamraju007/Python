"""
Ask the user to enter a number.
- If the number is a single digit number,
     add 7 to it, and print the number in its unit’s place
- If the number is a two digit number,
    raise the number to the power of 5, 
    and print the number in its unit’s place
- If the number is a three digit number, 
    ask the user to enter another number. 
    Add the 2 numbers and print the number in its unit’s place
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
            num = num+7       
            print("Number is single digit", num)
        elif num > 9 and num <= 99:
            num = num*5
            print("Number is 2 digit", num)
        else:
            num3 = int(input("Eneter an another number "))
            total = num+num3
            print("Number is 3 digit" , total)         
            
            

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
