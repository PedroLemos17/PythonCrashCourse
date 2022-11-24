# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:
# 
# "Santiago, Chile"
# 
# Call your function with at least three city-country pairs, and print the
# values that are returned.

def city_country(city, country):
    formatted = f"{city.title()}, {country.title()}"
    return formatted
print(city_country("são paulo", "brasil"))
print(city_country("baghdad", "iraq"))
print(city_country("santiago","chile"))