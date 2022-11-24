# Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurant:
    """Model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type ):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      
    def describe_restaurant(self):
        print(f"Name:{self.restaurant_name.title()}\nType:{self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!!!") 
        
restaurant1=Restaurant("Puzzle", "It's a secret")
restaurant2=Restaurant("Sanji's Bar", "Whiskey")
restaurant3=Restaurant("FFF", "XXX")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()