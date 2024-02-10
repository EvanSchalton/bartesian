from pathlib import Path
from bartesian.enums.drink import Drink
from bartesian.datasheet.datasheet_record import DatasheetRecord
from ..interfaces import TrainingData
from .record_to_matrix import record_to_matrix


def create_training_data(
    barcodes: dict[str, list[int]],
    file_name_to_drink: dict[str, Drink],
    data: dict[Drink, DatasheetRecord],
) -> list[TrainingData]:
    training_data: list[TrainingData] = []
    for k, v in barcodes.items():
        try:
            target_file = Path(k).name.replace("0[", "").replace("].jpg", ".jpg")
            drink = file_name_to_drink[target_file]
            training_data.append(
                TrainingData(filename=k, input=v, output=record_to_matrix(data[drink]))
            )
        except KeyError:
            pass
    return training_data
