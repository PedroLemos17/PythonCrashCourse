# Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person1={'first name':'John', 'last name':'Lennon', 'age':82, 'city':'New York',}
person2={'first name':'Paul', 'last name':'McCartney', 'age':80, 'city':'Liverpool',}
person3={'first name':'George', 'last name':'Harrison', 'age':79, 'city':'Liverpool',}

people=[person1, person2, person3]

for person in people: #iterating through the list
    for key, value in person.items(): #iterating through the dictionaries of the list
        print(f"{key.title()}: {value}", end=" ") # on python 3, to avoid breaking a line in the end of a print we can use ,end=" "
    print("\n") # new line outside the dictionary for so the information of each person is printed in a different line
