# Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a dif-
# ferent location on your system, and make sure the code in the except block
# executes properly.

def read_file(filename):
    """Reads file and prints its content"""
    try:
        with open(filename) as file:
            names=file.readlines()
    except FileNotFoundError:
        print(f"\nFile {filename} not found!!!\n")
    else:
        for name in names:
            print(name.rstrip())

dogs = "dogs.txt"
cats = "cats.txt"

read_file(dogs)
read_file(cats)
