"""
Using the starting and ending values of your car’s odometer, 
and the measure of fuel consumed, 
calculate the number of stops one should make for refuelling 
while travelling from Bangalore to Goa, 
a distance of 560 kms.
"""

def get_points():
    """ 
    Prompt the start point and end point 
    Input : yes
    Output : Return the user input start and end point
    """
    startpoint = int(input("Enter the start point of the odometer"))
    endpoint = int(startpoint+560)
    tank_capacity = int(input("Enter the capacity of the tank"))
    return (startpoint,endpoint,tank_capacity)
    

def mileage(start, end, tc):
    '''
    This calculates the mileage
    '''
    z = (end - start) / tc
    print("mileage", z)
    y = z / tc
    print( "total number of stops", y)
    
def main():
    '''
    Main function of the program
    '''
    (value, s, e) = get_points()
    mileage(value, s , e)
    
# Main starts from below
main()
