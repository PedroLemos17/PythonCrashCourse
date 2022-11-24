#  One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

try:
    number1=input("Please enter two numbers:\n")
    number1=int(number1)
    number2=input()
    number2=int(number2)
    print(f"The sum is {number1 + number2}")
except ValueError:
    print("One or both the values provided are not a number!!")
