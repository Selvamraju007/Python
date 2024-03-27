
""" 
Using the starting and ending values of your car’s odometer, 
            calculate its mileage
"""

def get_points():
    """ 
    Prompt the start point and end point 
    Input : yes
    Output : Return the user input start and end point
    """
    startpoint = int(input("Enter the start point of the odometer "))
    endpoint = int(input("Enter the end point of the odometer "))
    fuel = int(input("Enter the total number of fuel filled "))
    return (startpoint,endpoint,fuel)
    

def mileage(start, end, fuel):
    '''
    This calculates the mileage
    '''
    x = (start - end) / fuel
    print("total number of mileage", x)
  

def main():
    '''
    Main function of the program
    '''
    (value, s, e) = get_points()
    mileage(value, s , e)
    
# Main starts from below
main()
