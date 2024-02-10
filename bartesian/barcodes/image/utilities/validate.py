import cv2
import numpy as np

def validate_barcode(contour, gray_image, min_margin_proportion, min_vertical_lines, min_size, aspect_ratio_range):
    # Validation function: check for margins, vertical lines, size, and aspect ratio
    x, y, w, h = cv2.boundingRect(contour)
    if w * h < min_size:
        return False
    aspect_ratio = w / float(h)
    if not (aspect_ratio_range[0] <= aspect_ratio <= aspect_ratio_range[1]):
        return False
    cropped = gray_image[y:y+h, x:x+w]
    margin_width = int(w * min_margin_proportion)
    if np.mean(cropped[:, :margin_width]) > 200 or np.mean(cropped[:, -margin_width:]) > 200:
        return False
    edges = cv2.Sobel(cropped, cv2.CV_64F, 1, 0, ksize=-1)
    edges = cv2.convertScaleAbs(edges)
    _, edges = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    vertical_lines = np.sum(edges // 255, axis=0) > 0
    if np.sum(vertical_lines) < min_vertical_lines:
        return False
    if np.sum(cropped[-1, :] < 128) == 0:
        return False
    return True