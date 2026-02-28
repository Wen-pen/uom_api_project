from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from fruit import Fruit 
import json

class ApiClient:
    def __init__(self, url: str, fruit: str):
        self.url = url
        self.fruit = fruit

    def return_response(self) -> Fruit:
        try:
            print("Connecting to FruityVice....\n")
            with urlopen(self.url + self.fruit) as response:
                body = response.read()
        except HTTPError as e:
            status_code = e.code
            raise Exception(f"Error connecting, HTTP Code: {status_code}") from None 
        except URLError as e:
            raise Exception(f"Error connecting, URLError: {e.reason}") from None
        else:
            converted_response = json.loads(body)

            fruit_full_name = converted_response["name"]
            fruit_id = int(converted_response["id"])
            fruit_family = converted_response["family"]
            fruit_sugar = float(converted_response["nutritions"]["sugar"])
            fruit_carbs = float(converted_response["nutritions"]["carbohydrates"])

            return Fruit(fruit_full_name, fruit_id, fruit_family, fruit_sugar, fruit_carbs)
       