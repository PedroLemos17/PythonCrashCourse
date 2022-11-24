# Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet1={'animal': 'monkey', 'owner': 'brian'}
pet2={'animal': 'dog', 'owner': 'sarah'}
pet3={'animal': 'lion', 'owner': 'conan'}

pets=[pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}", end=" ")
    print("\n")

# Can't believe he made me do the same exercise twice, this is 6-7 again.