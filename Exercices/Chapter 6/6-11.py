# Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

new_york={'State': 'New York', 'Country': 'United States of America', 'Fun Fact': 'is the most populous city in the United States.',}
sao_paulo={'State': 'São Paulo', 'Country':'Brazil', 'Fun Fact':' listed by the GaWC as an alpha global city',}
tokyo={'Region':'Kantō', 'Country': 'Japan', 'Fun Fact': 'formerly known as Edo',}
cities={'New York':new_york, 'São Paulo': sao_paulo, 'Tokyo':tokyo,}

for city, information in cities.items():
    print(city.title())
    for key, value in information.items():
        print(f"\t{key.title()} : {value.title()}")
    print('\n')
        