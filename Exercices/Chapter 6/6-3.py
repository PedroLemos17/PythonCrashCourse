# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.

# Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character ( \n) to insert a blank line between each word-meaning
# pair in your output.

glossary={'list':'A collection of items in a particular order', 'tuple':'An immutable list', 'slice':'A part of a list',
'string':'A collection of letters', 'float':'Any number with a decimal point',}

print(f"List\n\t{glossary['list']}")
print(f"Tuple\n\t{glossary['tuple']}")
print(f"Slice\n\t{glossary['slice']}")
print(f"String\n\t{glossary['string']}")
print(f"Float\n\t{glossary['float']}")