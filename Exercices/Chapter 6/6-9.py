# Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favorite_places={'brian':['movie theather', 'mall', 'house'], 
                 'olivia':['beach', 'house', 'school'],
                 'neil':['house', 'college', 'gym'],}

for key, value in favorite_places.items():
    print(key.title(), end=": ")
    for place in value:
        if place == value[-1]:
            print(place.title())
        else:
            print(place.title(), end=", ")
        