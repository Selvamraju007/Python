#This code is to allow user 5 chances to guess the lucky number.

import random
lucky = random.randint(1,25)

guesses_left = 5
while guesses_left >0:
    guess = int(input("guess your value"))
    if guess < lucky:
        print("Too Low")
    elif guess > lucky:
        print("Too High")    
    elif guess == lucky:
          print ("your guess is correct")
          break
    guesses_left -= 1
else:
    print("your guess is not correct")
