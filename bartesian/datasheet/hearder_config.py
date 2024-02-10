from bartesian.enums.drink import Drink

HEADER_TYPES = {
    "drink": Drink,
    "image": bool,
    "Tequila": bool,
    "Vodka": bool,
    "Whiskey": bool,
    "Gin": bool,
    "Rum": bool,
    "Mocktail": float,
    "Light": float,
    "Regular": float,
    "Strong": float,
}

def set_type(value, type):
    if type == Drink:
        return Drink(value)
    if type == bool:
        return value == "TRUE"
    if type == float:
        return float(value)
    return value

__all__ = [
    HEADER_TYPES, set_type
]