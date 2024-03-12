""" 
“Hello World” program to prompt for user’s name 
           and then wish the user by saying Hello followed by his name
"""

def get_username():
    inp = input("Enter your name :")
    return inp

def say_hello(user):
    greet = "Hello"
    print(greet, user , "!!!")

def main():
    name = get_username()
    say_hello(name)
    
# Main starts from below
main()
