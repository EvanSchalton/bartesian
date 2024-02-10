import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_barcode(
    encoded_widths: dict[str, list[int]],
    pixel_width_lookup: dict[int, int],
    margin_ratio=0.3
):
    """
    Draw a barcode with specified left and right margins.
    
    Parameters:
    - encoded_widths: A list of numbers representing the encoded widths of the bars/spaces.
    - pixel_width_lookup: A dictionary mapping encoded numbers to pixel widths.
    - margin_ratio: The ratio of the total barcode width to be used as margin on each side.
    """
    # Calculate total width and margins
    total_width = sum([pixel_width_lookup[w] for w in encoded_widths])
    margin_width = total_width * margin_ratio
    
    # Create the figure and axis for drawing the barcode
    fig, ax = plt.subplots(figsize=(12, 2))
    ax.set_xlim([0, total_width + 2 * margin_width])
    ax.set_ylim([0, 1])

    # Start with the left margin
    current_x = margin_width
    
    # Draw the bars of the barcode
    for i, width_code in enumerate(encoded_widths):
        width = pixel_width_lookup[width_code]
        color = 'black' if i % 2 == 0 else 'white'  # Alternate bar colors
        rect = patches.Rectangle(
            (current_x, 0),
            width,
            1,
            linewidth=1,
            edgecolor='none',
            facecolor=color
        )
        ax.add_patch(rect)
        current_x += width
        
    # Remove y-axis and spines
    ax.axis('off')
    plt.show()