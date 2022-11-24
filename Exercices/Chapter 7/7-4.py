# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

flag=True
while(flag):
    topping=input("Enter the topping\n")
    if(topping=='quit'):
        flag=False
    else:
        print("I'll add that")
    