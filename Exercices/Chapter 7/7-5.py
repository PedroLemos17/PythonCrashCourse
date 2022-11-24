# A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

flag=True

while(flag):
    age=input("Digit your age please:\n")
    if(age=='quit'):
        flag=False
    else:
        age=int(age)
        if(age<3):
            print("The ticket is free for you\n")
        elif(age<12):
            print("The ticket is $10 USD for you\n")
        else:
            print("The ticket is $15 USD for you\n")
    