# Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

def define_items(*list):
    for value in list:
        print(value.title())
    print()

define_items("a", "b", "c")
define_items("a")
define_items("a", "b", "c", "d", "e", "f")