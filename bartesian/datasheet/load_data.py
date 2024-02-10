from pathlib import Path

DATA_FILENAME = "data.tsv"
DATA_PATH = Path(__file__).parent / DATA_FILENAME

from .hearder_config import HEADER_TYPES, set_type
from .datasheet_record import DataSheetRecord


def load_data(path: Path | None = DATA_PATH) -> list[DataSheetRecord]:
    with path.open() as in_data:
        raw_excel_data = in_data.read()

    records_lines = [r.split("\t") for r in raw_excel_data.strip().split("\n")]
    header = records_lines[0]


    all_record_json: list[DataSheetRecord] = [
        {k:set_type(v, HEADER_TYPES[k]) for k,v in i.items()}
        for i in [dict(zip(header, r)) for r in records_lines[1:]]
    ]

    return all_record_json
