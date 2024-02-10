from typing import TypedDict
from bartesian.enums.drink import Drink

class DataSheetRecord(TypedDict):
    drink: Drink
    image: bool
    Tequila: bool
    Vodka: bool
    Whiskey: bool
    Gin: bool
    Rum: bool
    Mocktail: float
    Light: float
    Regular: float
    Strong: float