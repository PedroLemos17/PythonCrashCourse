# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(text="I love python", size="Large"):
    print(f"The size of the shirt is: {size}\nThe text printed on it is: {text.title()}\n")
    
make_shirt()
make_shirt(size="M")
make_shirt("Corporation t-shirt", "X")
