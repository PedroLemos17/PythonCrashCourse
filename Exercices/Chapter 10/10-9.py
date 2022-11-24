# Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

def read_file(filename):
    """Reads file and prints its content"""
    try:
        with open(filename) as file:
            names=file.readlines()
    except FileNotFoundError:
            pass
    else:
        for name in names:
            print(name.rstrip())

dogs = "dogs.txt"
cats = "cats.txt"

read_file(dogs)
read_file(cats)
