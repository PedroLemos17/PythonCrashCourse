# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

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
    
def check_quit(string):
    if (string=="q"):
        return True
    else:
        return False

print("We'll ask you about the album's information, digit q at any time to quit")
while(True):
    name=input("Artist name: ")
    if(check_quit(name)):
        break
    title=input("Title of the album: ")
    if(check_quit(title)):
        break
    answer=input("Do you want to include the number of songs? (y/n)\n")
    if(check_quit(answer)):
        break
    if(answer.lower()=="yes" or answer.lower()=="y"):
        nSongs=input("Enter the number of songs: ")
        nSongs=int(nSongs)
        if(check_quit(nSongs)):
            break
        album=make_album(name, title, nSongs)
    elif(answer.lower()=="no" or answer.lower()=="n"):
        album=make_album(name, title)
    else:
        print("Invalid answer, not adding number of songs!")
        album=make_album(name, title)
    print("\n")
    print_dictionary(album)   
    print("\n")
    
# Ok I guess this answer was a little bit too complex