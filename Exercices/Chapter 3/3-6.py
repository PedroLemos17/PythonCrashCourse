# You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

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

