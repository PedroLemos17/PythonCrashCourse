# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers

favorite_numbers={'john':[17, 19], 'paul':[20, 9, 5], 'ringo':[27, 45, 67, 8, 9, 10], 'george':[6, 1], 'billy':[30],}

for key, value in favorite_numbers.items():
    print(key.title(), end=": ")
    for number in value:
        print(number, end=" ")
    print("\n")
    