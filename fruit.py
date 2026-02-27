class Fruit:
    def __init__(self, full_name : str, id : int, family: str, sugar: float, carbs: float):
        self.full_name = full_name
        self.id = id
        self.family = family
        self.sugar = sugar
        self.carbs = carbs
    
    def __str__(self) -> str:
        return f"Fruit name: {self.full_name} \n ID: {self.id} \n Family: {self.family} \n Sugar: {self.sugar}g \n Carbs {self.carbs}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Fruit):
            return False
        return self.full_name == other.full_name and self.family == other.family
    
    def as_dict(self) -> dict:
        return {
            "full_name": self.full_name,
            "id": self.id,
            "family": self.family,
            "sugar": self.sugar,
            "carbs": self.carbs
        }