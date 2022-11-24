# An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """Model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type ):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      
    def describe_restaurant(self):
        print(f"Name:{self.restaurant_name.title()}\nType:{self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!!!") 

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=flavors
    def display_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor.title()}")

flavors=["strawberry", "chocolate", "coconut nut"]
my_ice = IceCreamStand("My Ice", "Ice cream", flavors)        
my_ice.display_flavors()