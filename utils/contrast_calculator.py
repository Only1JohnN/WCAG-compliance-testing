def hex_to_rgb(hex_color):
    """Convert HEX color code to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

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
