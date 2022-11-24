# Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

def check_quit(value):
    """Checks if user entered q"""
    if value=='q':
        return True
    else:
        return False

while True:
    try:        
        number1=input("Please enter two numbers: (Enter q to quit)\n")
        if check_quit(number1):
            break
        number1=int(number1)
        number2=input()
        if check_quit(number2):
            break
        number2=int(number2)
    except ValueError:
        print("The value provided is not a number!!\n")
    else:
        print(f"The sum is {number1 + number2}")
