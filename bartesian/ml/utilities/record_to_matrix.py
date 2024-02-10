from bartesian.configs import LIQUOR_ORDER, STRENGTH_ORDER
from bartesian.datasheet import DatasheetRecord


def record_to_matrix(record) -> list[list[float]]:
    try:
        return [
            [record[s] if record[l] else 0.0 for s in STRENGTH_ORDER]
            for l in LIQUOR_ORDER
        ]
    except:
        print(record)
        raise
