import colorsys

def hex_to_rgb(hex):
    rgb = []
    for i in (0, 2, 4):
        rgb.append(int(hex[i:i+2], 16))
    return rgb

def rgb_to_hex(rgb):
    hex = ""
    for v in rgb:
        if v > 255:
            raise RuntimeError("Illegal color value: '%s' in %s" % (v, rgb))
        hex += format(int(v), '02x')
    return hex

class ColorRange:
    base_colors = {
        "blue": "3382fe",
        "green": "1c7d36",
        "red": "ac090a",
        "pink": "800ca2",
        "grey": "010101",
    }

    @staticmethod
    def known_colors():
        return list(ColorRange.base_colors.keys()) + ["rainbow"]

    def __init__(self, name):
        self.name = name
        if name != "test" and not name in ColorRange.known_colors():
            raise RuntimeError("Unknown color range '%s'" % name)

    def base_color(self):
        return ColorRange.base_colors[self.name]

    def color_range(self, index, total, range_fraction = None):
        if self.name == "test":
            return str(index+1) + "/" + str(total)
        elif self.name == "rainbow":
            rgb = []
            rgb_normalized = colorsys.hls_to_rgb(index / total, 0.5, 0.8)
            for v in rgb_normalized:
                rgb.append(v * 255)
            return rgb_to_hex(rgb)
        else:
            if range_fraction is None:
                range_fraction = total * 0.0165 + 0.447
            if range_fraction > 0.8:
                range_fraction = 0.8
            adjusted_color = []
            for c in hex_to_rgb(self.base_color()):
                value = int(c + ((255 - c) / (total - 1) * range_fraction * index))
                adjusted_color.append(value)
            return rgb_to_hex(adjusted_color)
