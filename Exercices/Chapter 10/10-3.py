# Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

name = input("What's your name?\n")
with open("guest.txt", "w") as file:
    file.write(name)