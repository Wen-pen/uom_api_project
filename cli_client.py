import argparse
from apiclient import ApiClient

parser = argparse.ArgumentParser(description="Searches and returns common facts of fruits for you!")

parser.add_argument("fruit", metavar="FRUIT", type=str, help="Enter what fruit you need")


parser.add_argument("-d", "--dict", action="store_true", dest="as_dict", 
                    help="Returns a dictionary representation of a fruit to standard output")

args = parser.parse_args()


def fetch_fruit(fruit_name: str):
    try:
        return ApiClient("https://www.fruityvice.com/api/fruit/", fruit_name).return_response()
    except Exception as e:
        print(f"Failed to retrieve fruit: {e}")
        return None

fruit_object = fetch_fruit(args.fruit)

if fruit_object:
    if args.as_dict:
        print(fruit_object.as_dict())
    else:
        print(fruit_object.__str__())