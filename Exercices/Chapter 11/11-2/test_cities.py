import unittest
import city_functions as city

class CityTests(unittest.TestCase):
    def test_country_city_format(self):
        """City and Country formatted correctly?"""
        test_city=city.format_region("são paulo", "brazil")
        self.assertEquals(test_city, "São Paulo, Brazil")
    
    def test_city_country_population(self):
        """City and Country formatted correctly?"""
        test_city=city.format_region("são paulo", "brazil", "12 million")
        self.assertEquals(test_city, "São Paulo, Brazil - population 12 million")

if __name__ == '__main__':
    unittest.main()