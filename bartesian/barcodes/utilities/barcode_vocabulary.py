from typing import TypedDict

class BarcodeVocabulary(TypedDict):
    barcodes: dict[str, list[int]]
    thickness: dict[int, int]
    