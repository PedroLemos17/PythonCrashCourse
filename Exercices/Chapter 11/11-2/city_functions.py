# Modify your function so it requires a third parameter,
# population . It should now return a single string of the form City, Country –
# population xxx, such as Santiago, Chile – population 5000000. Run test
# _cities.py again. Make sure test_city_country() fails this time.

# Modify the function so the population parameter is optional. Run test
# _cities.py again, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that veri-
# fies you can call your function with the values 'santiago', 'chile', and
# 'population=5000000'. Run test_cities.py again, and make sure this new test
# passes.

def format_region(city, country, population=None):
    if population:
        formatted_string=f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_string=f"{city.title()}, {country.title()}"
    return formatted_string
