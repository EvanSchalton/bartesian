import cv2

def preprocess_image(image: cv2.typing.MatLike):
    # Preprocessing function: Gaussian blur and thresholding
    blurred = cv2.GaussianBlur(image, (9, 9), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours