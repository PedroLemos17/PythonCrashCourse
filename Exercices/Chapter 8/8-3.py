# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, text):
    print(f"The size of the shirt is: {size}\nThe text printed on it is: {text.title()}\n")
    
make_shirt("x", "I don't believe in unity")
make_shirt(text="It must be pretty cool to be you", size="M")
