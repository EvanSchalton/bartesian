from pathlib import Path
import cv2
from .utilities.barcode_search import barcode_search

def isolate_barcodes(input_dir: Path, output_dir: Path, glob_regex: str = "*.jpg") -> None:
    """
    Isolate barcodes from images in input_dir and save them to output_dir.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    for image_path in input_dir.glob(glob_regex):
        image = cv2.imread(str(image_path))
        barcodes = barcode_search(image)
        for index, barcode in enumerate(barcodes):
            output_name = f"{index}[{image_path.name.replace(image_path.suffix, '')}]{image_path.suffix}"
            output_name = output_dir / output_name
            cv2.imwrite(str(output_name), barcode)