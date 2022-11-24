# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
#
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(name, title, nSongs=None):
    album={}
    album["Artist"]= name.title()
    album["Title"]= title.title()
    if(nSongs):
        album["Number of Songs"]=nSongs
        return album
    else:
        return album

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key.title()}: {value}")
    print("\n")
        

album1=make_album("the beatles", "revolver")
album2=make_album("days n daze", "crustfall")
album3=make_album("descendents", "cool to be you", 14)

print_dictionary(album1)
print_dictionary(album2)
print_dictionary(album3)    