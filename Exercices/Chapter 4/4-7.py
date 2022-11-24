# Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

multiples = []
for value in range(1,11):
    multiples.append(3*value)
for value in multiples:
    print(value)