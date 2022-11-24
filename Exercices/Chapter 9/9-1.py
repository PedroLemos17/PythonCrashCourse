# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

class Restaurant:
    """Model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type ):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      
    def describe_restaurant(self):
        print(f"Name:{self.restaurant_name.title()}\nType:{self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!!!") 

restaurant = Restaurant("Puzzle", "it's a secret!")
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()