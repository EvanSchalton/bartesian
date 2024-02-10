from .datasheet_record import DataSheetRecord
from ..configs import LIQUOR_ORDER, STRENGTH_ORDER


def review_datasheet(datasheet: list[DataSheetRecord]) -> None:
    """Review the dataset."""
    all_records = {i["drink"]: i for i in datasheet}
    records = {i["drink"]: i for i in datasheet if i["image"]}

    missing_images = [k for k, v in all_records.items() if not v["image"]]
    missing_ingredients = [
        k for k, v in all_records.items() if all([v[l] is False for l in LIQUOR_ORDER])
    ]
    missing_potency = [
        k for k, v in all_records.items() if any([v[l] < 0 for l in STRENGTH_ORDER])
    ]

    print(f"Missing Images:")
    for i in sorted(missing_images, key=lambda x: x.value):
        print(f"  - {i}")
    print(f"\nMissing Ingredients:")
    for i in sorted(missing_ingredients, key=lambda x: x.value):
        print(f"  - {i}")
    print(f"\nMissing Potency:")
    for i in sorted(missing_potency, key=lambda x: x.value):
        print(f"  - {i}")
