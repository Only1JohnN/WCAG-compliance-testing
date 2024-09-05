def hex_to_rgb(hex_color):
    """Convert HEX color code to RGB tuple."""
    # Remove '#' if present
    hex_color = hex_color.lstrip('#')
    
    # Validate HEX color length
    if len(hex_color) != 6:
        raise ValueError("Invalid HEX color format. Should be 6 characters long.")
    
    # Convert HEX to RGB
    try:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    except ValueError as e:
        raise ValueError(f"Invalid HEX color value: {e}")


def luminance(rgb):
    """Calculate luminance of an RGB color."""
    r, g, b = [x / 255.0 for x in rgb]
    r, g, b = [((x / 12.92) if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4) for x in [r, g, b]]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def calculate_color_contrast(color1, color2):
    """Calculate the contrast ratio between two colors."""
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    lum1 = luminance(rgb1)
    lum2 = luminance(rgb2)
    return (max(lum1, lum2) + 0.05) / (min(lum1, lum2) + 0.05)
