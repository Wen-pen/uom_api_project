import unittest
import cli_client

class CliClientTest(unittest.TestCase):
    def test_correct_string_details(self):
        answer = cli_client.return_string_details("strawberry")
        self.assertEqual(answer, "Fruit name: Strawberry \n ID: 3 \n Family: Rosaceae \n Sugar: 5.4g \n Carbs: 5.5g \n")

    def test_correct_string_details_2(self):
        answer = cli_client.return_string_details("persimmon")
        self.assertEqual(answer, "Fruit name: Persimmon \n ID: 52 \n Family: Ebenaceae \n Sugar: 18.0g \n Carbs: 18.0g \n")

    def test_correct_dict_details(self):
        answer = cli_client.return_dict_details("strawberry")
        self.assertEqual(answer,  {
            "full_name": "Strawberry",
            "id": 3,
            "family": "Rosaceae",
            "sugar": 5.4,
            "carbs": 5.5
        })

    def test_correct_dict_details_2(self):
        answer = cli_client.return_dict_details("persimmon")
        self.assertEqual(answer, {
            "full_name": "Persimmon",
            "id": 52,
            "family": "Ebenaceae",
            "sugar": 18,
            "carbs": 18
        })

    def test_wrong_dict_details(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = cli_client.return_dict_details("wineberry")
    
    def test_wrong_dict_details_2(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = cli_client.return_dict_details("bannanna")

    def test_wrong_string_details(self):
        with self.assertRaises(Exception) as context:
            wrong_correction = cli_client.return_dict_details("wineberry")

    def test_wrong_string_details_2(self):
       with self.assertRaises(Exception) as context:
            wrong_correction = cli_client.return_dict_details("bannanna")
        
if __name__ == "__main__":
    unittest.main()