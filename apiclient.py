from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json

class ApiClient:
    def __init__(self, url: str, fruit: str):
        self.url = url
        self.fruit = self.return_response(fruit)

    def return_response(self, fruit)-> dict:
        try:
            with urlopen(self.url + fruit) as response:
                body = response.read()
                converted_response = json.loads(body)
                return converted_response
        except HTTPError as e:
            status_code = e.code
            raise Exception(f" Error connecting, HTTP Code: {status_code}") 
        except URLError as e:
            raise Exception(f"URLError: {e.reason}") 
        
    def return_details(self) -> dict:
        return self.fruit
    
    def return_details_str(self) -> str:
        name = self.fruit["name"]
        id = self.fruit["id"]
        return ""