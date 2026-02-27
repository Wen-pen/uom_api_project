import unittest
from apiclient import ApiClient
from urllib.error import HTTPError, URLError

class ApiConnectionTest(unittest.TestCase):

    def test_correct_connection(self):
        correct_connection = ApiClient("https://www.fruityvice.com/api/fruit/", "strawberry")
        self.assertEqual(correct_connection.return_response("strawberry"), {'name': 'Strawberry', 'id': 3, 'family': 'Rosaceae', 'order': 'Rosales', 'genus': 'Fragaria', 'nutritions': {'calories': 29, 'fat': 0.4, 'sugar': 5.4, 'carbohydrates': 5.5, 'protein': 0.8}})

    
    def test_correct_connection_2(self):
        correct_connection = ApiClient("https://www.fruityvice.com/api/fruit/", "kiwi")
        self.assertEqual(correct_connection.return_response("kiwi"), {"name":"Kiwi","id":66,"family":"Actinidiaceae","order":"Struthioniformes","genus":"Apteryx","nutritions":{"calories":61,"fat":0.5,"sugar":9.0,"carbohydrates":15.0,"protein":1.1}})


    def test_incorrect_connection(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = ApiClient("https://www.fruityvice.com/api/fruit/", "wineberry")

    def test_incorrect_connection_2(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = ApiClient("https://www.fruityvice.com/api/fruit/", "bannanna")

    def test_incorrect_connection_3(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = ApiClient("https://this-website-is-entirely-fictional-and-broken.com", "irrelevant_fruit")
        

if __name__ == "__main__":
    unittest.main()