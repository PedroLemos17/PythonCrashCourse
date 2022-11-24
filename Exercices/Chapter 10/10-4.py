# Write a while loop that prompts users for their name. [
# When they enter their name, print a greeting to the screen 
# and add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

flag = True
print("Enter q when you want to quit\n")
while(flag):
    name=input("What is your name?\n")
    if name == 'q':
        flag=False
    else:
        with open("guest_book.txt", 'a') as file:
            file.write(f"{name.title()}\n")
        print(f"Hello {name.title()}")