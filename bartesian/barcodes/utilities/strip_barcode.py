def strip_barcode(widths: list[int]) -> list[int]:
    """
    Strips the whitespace from the beginning and end of a barcode.
    """
    MIN_WHITESPACE_WIDTH_PIXELS: int = 200

    result: list[int] = []
    for i in widths:
        if len(result) == 0 and i < MIN_WHITESPACE_WIDTH_PIXELS: continue
        if len(result) > 0 and i > MIN_WHITESPACE_WIDTH_PIXELS:
            result.append(i)
            return result[1:-1]
        result.append(i)

    return result