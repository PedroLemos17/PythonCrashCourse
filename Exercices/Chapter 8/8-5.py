# Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city, country="Brazil"):
    print(f"{city.title()} is in {country.title()}")
describe_city("são paulo")
describe_city("new york", "the united states of america")
describe_city("tokyo", "japan")
    
