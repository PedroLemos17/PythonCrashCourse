# Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary={'list':'A collection of items in a particular order', 'tuple':'An immutable list', 'slice':'A part of a list',
'string':'A collection of letters', 'float':'Any number with a decimal point',}

for key, value in glossary.items():
    print(f"{key.title()}: {value}")
# I'm not gonna add five more words