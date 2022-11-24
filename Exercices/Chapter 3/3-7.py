# You just found out that your new dinner table won’t arrive in time for the dinner,
# and you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.

# Print a message to each of the two people still on your list, letting them
# know they’re still invited.

# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

guests=['John Lennon', 'George R.R. Martin', 'Ian Mackaye']

print(f"Dear {guests[0]}, I would like to invite you to a dinner with me, I'd like to know more about a certain walrus... Don't worry, Paul won't come.")
print(f"Mr. {guests[-2]}, Let's have a dinner, I will kill you just like I killed your father. Finish your fucking books you old prick.")
print(f"Hey {guests[2]}, how about you have a dinner with me while we listen to some old punk. Drugs are not allowed!")

print("\nWell, I found a bigger table so I'm going to invite some ladies\n")

guests.insert(0, 'Alison Brie')
guests.insert(2, 'Gisele Bündchen')
guests.append('Scarlett Johannson')

print(f"Dear {guests[0]}, I would like to invite you to a dinner with me and my friends.")
print(f"Mr. {guests[1]}, let's have a dinner! Bring Yoko")
print(f"Dear {guests[2]}, I'd like to have a dinner with you tonight! Alison is coming.\n")
print(f"Mr. {guests[3]}, let's talk about how you care more about Wild Cards than ASOIAF tonight in a dinner with my friends.")
print(f"Hey {guests[4]}, dinner tonight. My home. Straight Edge forever!")
print(f"Dear {guests[5]}, I would love to have the most beautiful woman in the world in my dinner with my friends")

print('\n Man, this is embarassing, but I can only invite two of you now\n')

excluded=guests.pop()
print(f"Sorry {excluded}, but there won't be a dinner tonight for you!")
excluded=guests.pop()
print(f"Sorry {excluded}, but there won't be a dinner tonight for you!")
excluded=guests.pop()
print(f"Sorry {excluded}, but there won't be a dinner tonight for you!")
excluded=guests.pop()
print(f"Sorry {excluded}, but there won't be a dinner tonight for you!")

print(f"\n{guests[0]} and {guests[1]}, you're still invited!\n")

del guests[:]# deletes all elements of the list
print(guests)