import numpy as np

def normalize_barcode_widths(
    barcode_widths_dict: dict[str, list[int]],
    vocabulary_size: int
) -> dict[str, list[int]]:
    """
    Coallesce the widths of all barcodes into a single vocabulary of `vocabulary_size` bins.
    
    Most barcode systems have a set vocabulary size (number of distinct bar thicknesses), this allows
    us to assert a vocabulary size and normalize all barcodes to that vocabulary.

    **One of the pods was scanable with a generic barcode scanner, though this was a fluke it led to the
    theory that the valid vocabulary size would be one where that same barcode could be scanned by the same
    scanner and return the same value. Using this function I normalized the target image to all vocabulary sizes
    between 4 and 20 and found that a vocabulary of 13 produced the same value as the original barcode.
    """

    # Flatten all widths to find the global min and max
    all_widths = [width for widths in barcode_widths_dict.values() for width in widths]
    min_width, max_width = min(all_widths), max(all_widths)

    # Create the vocabulary as equally spaced bins between min and max width
    vocab_bins = np.linspace(min_width, max_width, num=vocabulary_size, endpoint=False)

    # Function to map width to vocabulary
    def map_to_vocab(width, vocab_bins) -> int:
        # Find the closest bin
        bin_index = np.digitize(width, vocab_bins, right=False)
        # Map to the vocabulary by bin index
        return bin_index

    # Normalize each barcode's widths
    normalized_barcodes: dict[str, list[int]] = {}
    for filename, widths in barcode_widths_dict.items():
        normalized_widths = [map_to_vocab(width, vocab_bins) for width in widths]
        normalized_barcodes[filename] = normalized_widths

    return normalized_barcodes