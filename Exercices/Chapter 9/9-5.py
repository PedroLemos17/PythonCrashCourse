# Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.login_attempts=0
    
    def describe_user(self):
        print(f"First name: {self.first_name.title()}\nLast name: {self.last_name.title()}\n Age: {self.age}\nCountry: {self.country.title()}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()}")
    
    def increment_login(self):
        self.login_attempts+=1
    
    def reset_login_attempts(self):
        self.login_attempts=0

user = User("John", "Lennon", "40", "England")        
print(user.login_attempts)

for i in range(51):
    user.increment_login()

print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)