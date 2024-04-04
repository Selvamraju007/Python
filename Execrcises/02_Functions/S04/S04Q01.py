""" A Chemical plant has a tank for storing ethanol.
- When the tank is more than 80% full, it
     should raise an alarm to close the valve.
- When the tank is less than 20% full, it
     should send an SMS to buy more liquid.
- The total tank capacity is 900 litres.
- Write a program to simulate this.
- Ask user to enter current level of ethanol in the tank.
- Print the appropriate action based on value entered
"""

def do_action(userinput):
    capacity = 900
    percent = (userinput/capacity)*100
    if percent >=int(80):
        print("close the valve")
    elif percent <=int(20):
         print("Buy more liquid to full the tank")
    else:
        print("Do nothing")       
      
  
def get_current_level():
    # Get value from user
    # Return integer
    userinput = int(input("Enter current level of ethanol in the tank "))
    do_action(userinput)

# Main starts from here
get_current_level()
