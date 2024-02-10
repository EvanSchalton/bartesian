from .strip_barcode import strip_barcode
from .normalize_barcode_widths import normalize_barcode_widths
from .barcode_vocabulary import BarcodeVocabulary

def normalize_barcodes(
    barcode_widths_dict: dict[str, int],
    vocabulary_size: int
) -> BarcodeVocabulary:
    BARCODE_SIZE = 37
    stripped_barcode_widths_dict = {}
    for k,v in barcode_widths_dict.items():
        barcode = strip_barcode(v)
        # print(f"{Path(k).name:<32}: {barcode}")
        stripped_barcode_widths_dict[k] = barcode

    # filter our invalid barcodes
    stripped_barcode_widths_dict = {k:v for k,v in stripped_barcode_widths_dict.items() if len(v) == BARCODE_SIZE}

    normalized_barcode_widths: dict[str, list[int]] = normalize_barcode_widths(stripped_barcode_widths_dict.copy(), vocabulary_size)
    # for k,barcode in normalized_barcode_widths.items():
        # print(f"{Path(k).name:<32}: {barcode}")

    thickness_dict = {}
    for k,v in stripped_barcode_widths_dict.items():
        i = normalized_barcode_widths[k]
        for (j,k) in zip(i,v):
            thickness_dict.setdefault(j, []).append(k)
    thickness_dict = {k:sum(v)//len(v) for k,v in thickness_dict.items()}

    flattened_values = [i for v in stripped_barcode_widths_dict.values() for i in v]
    counts = {k: flattened_values.count(k) for k in set(flattened_values)}

    return {"barcodes": normalized_barcode_widths, "thickness": thickness_dict}