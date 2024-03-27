"""
Using the starting and ending values of your car’s odometer, 
and the measure of fuel consumed, 
calculate the number of stops one should make for refuelling 
while travelling from Bangalore to Goa, 
a distance of 560 kms.
"""

#Main starts form here
startpoint = int(input("Enter the starting point of the odometer "))
endpoint = int(startpoint+560)
tank_capacity = int(input("Eneter the capacity of the tank "))
x = (startpoint - endpoint) / tank_capacity
print("total no of milege", x)
y = x / tank_capacity
print("total no of stops", y)
