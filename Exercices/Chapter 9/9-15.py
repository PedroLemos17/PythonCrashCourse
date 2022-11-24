# You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.

import random

here_we_go=[1,2,3,4,5,"a","b","c","d","e",6,7,8,9,10]

def new_ticket():
    """Makes new random ticket"""
    ticket=[]
    for x in range(0,4):
        ticket.append(random.choice(here_we_go))
    return ticket

def is_in_list(list, element):
    """Checks if element is in list"""
    if list.count(element)>0: #count() counts how many times the element is inside the list. If the count is zero, the element is not in the list
        return True
    else:
        return False
    
def check_ticket(winner, ticket):
    """Checks if the ticket is equal to the winner ticket"""
    hit=0
    for value in winner:
        if is_in_list(ticket, value):
            hit+=1
    if hit == 4:
        return True
    else:
        return False    

winner_ticket=[]
for x in range(0,4):
    winner_ticket.append(random.choice(here_we_go))

my_ticket=new_ticket()

count =0
while(check_ticket(winner_ticket, my_ticket) is False):
    my_ticket=new_ticket()
    count+=1

print(f"You got the winner ticket after {count} attempts")
    

    