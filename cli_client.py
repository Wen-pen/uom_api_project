import argparse
from fruit import Fruit
from apiclient import ApiClient

parser = argparse.ArgumentParser()

fruit_arg = parser.add_argument("fruit")
string_arg = parser.add_argument("-s")
dict_arg = parser.add_argument("-d")

def return_string_details(fruit: str) -> str:
    returned_fruit = ApiClient("https://www.fruityvice.com/api/fruit/", fruit).return_response()
    if returned_fruit is None:
        return ""
    else:
        return returned_fruit.__str__()

def return_dict_details(fruit: str) -> dict:
    returned_fruit = ApiClient("https://www.fruityvice.com/api/fruit/", fruit).return_response()
    if returned_fruit is None:
        return {}
    else:
        return returned_fruit.as_dict()
    
return_string_details("apple")
return_string_details("strawberry")