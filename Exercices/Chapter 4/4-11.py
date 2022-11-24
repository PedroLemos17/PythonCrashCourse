# Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:

# Add a new pizza to the original list.

# Add a different pizza to the list friend_pizzas.

# Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list.

pizzas=["Neapolitan", "Sicilian", "Greek"]

for type in pizzas:
    print(f"The type is {type}")
    
friend_pizzas=pizzas[:]
pizzas.append("Detroit")
friend_pizzas.append("Chicago")

print("\nMy favorite pizzas are:")
for item in pizzas:
    print(item)
print("\nMy friend's favorite pizzas are:")
for item in friend_pizzas:
    print(item)
