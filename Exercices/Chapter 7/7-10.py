# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

places={}

flag=True
while(flag):
    name=input("What is your name?\n")
    place=input("If you could visit one place in the world, where would you go?\n")
    places[name]=place
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if(repeat=='no' or repeat=='n'):
        flag=False
for key, value in places.items():
    print(f"Name: {key.title()}\nPlace:{value.title()}\n")