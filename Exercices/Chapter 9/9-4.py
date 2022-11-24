# Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any num-
# ber you like that could represent how many customers were served in, say, a
# day of business.

class Restaurant:
    """Model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type ):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      self.number_served = 0
      
    def describe_restaurant(self):
        print(f"Name:{self.restaurant_name.title()}\nType:{self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!!!") 
    
    def set_number_served(self, number):
        self.number_served=number
    
    def increment_number_served(self):
        self.number_served+= 1

restaurant = Restaurant("Puzzle", "it's a secret!")
print(restaurant.number_served)
restaurant.number_served=10 
print(restaurant.number_served)
restaurant.set_number_served(14)
print(restaurant.number_served)
restaurant.increment_number_served()
print(restaurant.number_served)
