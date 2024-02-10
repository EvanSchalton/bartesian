from pathlib import Path
import cv2

DEFAULT_RESOLUTION = (1024, 530)

def resize_image(input_path: Path, output_path: Path, resolution: tuple[int, int] | None = None) -> None:
    """
    Resize the image at input_path and save it to output_path.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if resolution is None:
        resolution = DEFAULT_RESOLUTION

    # Read the image from file
    img = cv2.imread(str(input_path))
    # Resize the image
    resized_img = cv2.resize(img, resolution, interpolation=cv2.INTER_AREA)
    # Save the resized image
    cv2.imwrite(str(output_path), resized_img)