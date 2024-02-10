import cv2
import numpy as np
from .preprocess import preprocess_image
from .validate import validate_barcode

def barcode_search(source_image: cv2.typing.MatLike):
    """
    Search for barcodes in an image.
    """
    results: list[cv2.typing.MatLike] = []

    # Convert source image to grayscale
    gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)

    # Preprocess the image and get contours
    contours = preprocess_image(gray)

    # Set validation parameters
    min_margin_proportion = 0.25
    min_vertical_lines = 10
    min_size = gray.shape[0] * gray.shape[1] * 0.01
    aspect_ratio_range = (1.8, 2.2)

    # Validate each contour and select the ones that match all criteria
    valid_barcodes: list[cv2.typing.MatLike] = []
    for contour in contours:
        if validate_barcode(contour, gray, min_margin_proportion, min_vertical_lines, min_size, aspect_ratio_range):
            valid_barcodes.append(contour)

    # Draw the valid barcodes on the image
    for contour in valid_barcodes:
        x, y, w, h = cv2.boundingRect(contour)

        cropped_image = source_image[y:y+h, x:x+w]
        results.append(cropped_image)

    return results
