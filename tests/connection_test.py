import unittest
from fruit import Fruit
from apiclient import ApiClient

class ApiConnectionTest(unittest.TestCase):

    def test_correct_connection(self):
        correct_connection = ApiClient("https://www.fruityvice.com/api/fruit/", "strawberry")
        self.assertEqual(correct_connection.return_response(), Fruit("Strawberry", 3, "Rosaceae" , 5.4, 5.5))
    
    def test_correct_connection_2(self):
        correct_connection = ApiClient("https://www.fruityvice.com/api/fruit/", "kiwi")
        self.assertEqual(correct_connection.return_response(), Fruit("Kiwi", 66, "Actinidiaceae", 15, 9))

    def test_incorrect_connection(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = ApiClient("https://www.fruityvice.com/api/fruit/", "wineberry").return_response()

    def test_incorrect_connection_2(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = ApiClient("https://www.fruityvice.com/api/fruit/", "bannanna").return_response()

    def test_incorrect_connection_3(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = ApiClient("https://this-website-is-entirely-fictional-and-broken.com", "irrelevant_fruit").return_response()
        

if __name__ == "__main__":
    unittest.main()