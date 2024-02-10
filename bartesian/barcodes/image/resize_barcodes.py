from pathlib import Path
from .utilities import resize_image

def resize_barcodes(
    input_dir: Path,
    output_dir: Path,
    glob_regex: str = "*",
    resolution: tuple[int, int] | None = None
) -> None:
    """
    Resize the barcodes in input_dir and save them to output_dir.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    # List of image file paths
    for image_path in input_dir.glob(glob_regex):
        output_path = output_dir / image_path.name
        # Resize and save the image
        resize_image(image_path, output_path, resolution)