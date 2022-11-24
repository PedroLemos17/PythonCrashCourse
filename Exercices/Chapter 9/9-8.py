# Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

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

class Privileges:
    def __init__(self, privileges):
        self.privileges=privileges
    
    def show_privileges(self):
        for value in self.privileges:
            print(f"{value.title()}")
        

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges=Privileges(["can add post", "can delete post", "can ban user",])
    
admin = Admin("Gerard", "Bolton", 44, "Tanúsia")
admin.privileges.show_privileges()