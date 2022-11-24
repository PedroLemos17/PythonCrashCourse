# Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”

# Combine the two programs from Exercise 10-11 into one file. 
# If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.


import json

filename = "favorite_numbers.json"

def get_number():
    try:
        with open(filename) as file:
            number=json.load(file)
    except FileNotFoundError:
        return None
    else:
        return number

def save_number():
    number=input("Enter your favorite number\n")
    with open(filename, "w") as file:
        json.dump(number, file)
    print("We'll remember your number next time!")
    
if get_number()==None:
    save_number()
else:
    number=get_number()
    print(f"Your favorite number is {number}")