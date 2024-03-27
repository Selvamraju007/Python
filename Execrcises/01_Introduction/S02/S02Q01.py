"""
Using the starting and ending values of your car’s odometer, 
            calculate its mileage
"""

#Main starts form here
startpoint = int(input("Enter the starting point of the odometer "))
endpoint = int(input("Enter the endpoint of the odometer "))
fuel = int(input("Eneter the total no of fuel filled "))
mileage = (startpoint - endpoint) / fuel
print("total no of mileage", mileage)
