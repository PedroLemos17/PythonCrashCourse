# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    
    def describe_user(self):
        print(f"First name: {self.first_name.title()}\nLast name: {self.last_name.title()}\n Age: {self.age}\nCountry: {self.country.title()}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()}")

# Ok I'm just creating one instance here

user = User("John", "Lennon", "40", "England")        
user.describe_user();
user.greet_user();