import cv2 
import numpy as np

def barcode_to_widths(image_path):
    """
    Convert a barcode image to a sequence of widths.

    Note: We start with this because we don't know the vocabulary
    size of the barcode yet.
    """
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Binarize the image, bars are black (0) and spaces are white (255)
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # Invert if necessary so that bars are black
    if np.mean(binary[:10]) > 128:
        binary = cv2.bitwise_not(binary)
    
    # Assume the barcode is horizontal and scan through the middle
    height, width = binary.shape
    mid = height // 2
    scan_line = binary[mid, :]
    
    # Measure the width of each bar and space
    widths = []
    current_color = 255  # Start with white (space)
    count = 0
    
    for pixel in scan_line:
        if pixel == current_color:
            count += 1  # Continue counting similar color
        else:
            widths.append(count)  # Save the count of the series
            count = 1  # Reset count for new color
            current_color = pixel  # Switch current color
    
    # Append the last count
    widths.append(count)
    
    # Return the sequence of widths
    return widths
