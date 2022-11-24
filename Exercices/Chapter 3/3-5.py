# You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still
# in your list.

guests=['John Lennon', 'George R.R. Martin', 'Ian Mackaye']

print(f"Dear {guests[0]}, I would like to invite you to a dinner with me, I'd like to know more about a certain walrus... Don't worry, Paul won't come.\n")
print(f"Mr. {guests[-2]}, Let's have a dinner, I will kill you just like I killed your father. Finish your fucking books you old prick.\n")
print(f"Hey {guests[2]}, how about you have a dinner with me while we listen to some old punk. Drugs are not allowed!\n")

print(f"Well, apparently {guests[1]} is to much of a coward to show up and be murdered, guess I will be inviting somebody else\n")

del guests[-2]
guests.insert(1, 'Kentaro Miura')

print(f"Dear {guests[0]}, let's talk about how Yoko destroyed your band in a dinner together\n")
print(f"Hello {guests[1]}, different from some fat idiots I know, you are a guy who cares about your story and that died for it, Let's have a dinner and talk about the end of Berserk you were planning.\n")
print(f"Hey {guests[2]}, forget about sXe, let's get drunk in a dinner tonight!\n")
