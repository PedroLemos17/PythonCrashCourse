# Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.

from random import choice

here_we_go=[1,2,3,4,5,"a","b","c","d","e",6,7,8,9,10]

new_list=[]

for x in range(0,4):
    new_list.append(choice(here_we_go))

print("Any ticket matching the following numbers/letters wins a prize!!!")
for value in new_list:
    print(value)