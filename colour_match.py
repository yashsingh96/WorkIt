from _bisect import bisect


def main():
    # im = Image.open("monochromatic.jpg")
    # pixels = list(im.getdata())
    #
    # width, height = im.size
    #
    # hsl_pixels = []
    #
    # for pixel in pixels:
    #     # print(pixel)
    #     h, l, s = rgb_to_hls(pixel[0] / 255, pixel[1] / 255, pixel[2] / 255)
    #     hsl_pixels.append((int(round(h * 359)), int(round(l * 100)), int(round(s * 100))))
    #
    # hue_vals = [15, 45, 65, 165, 180, 265, 300, 340, 360]
    # colour_vals = 'ROYGCBPVR'
    #
    # for i in range (0, height):
    #     str = ""
    #     for j in range (0, width):
    #         curr_colour = colour_vals[bisect(hue_vals, hsl_pixels[width * j + i][0])]
    #         str +=  curr_colour
    #
    #     print(str)
    #

    is_mono = [(111, 5, 10), (88, 5, 10), (135, 5, 10)]
    print(monochromatic(is_mono))

    not_mono = [(40, 5, 10), (88, 5, 10), (135, 5, 10)]
    print(monochromatic(not_mono))


def monochromatic(colours):
    hue_vals = [-10, -5, -2, 15, 45, 65, 165, 180, 265, 300, 340, 360]
    colour_vals = '0GROYGCBPVR'

    curr_colour = None

    for colour in colours:
        H, S, L = colour

        if S <= 10:
            H = -3

        if L <= 10:
            H = -6

        if L > 97:
            H = -13

        if curr_colour is None:
            curr_colour = bisect(hue_vals, H)

        elif curr_colour != bisect(hue_vals, H):
            return False

    return True


def offspring(colours):
    hue_vals = [-10, -5, -2, 15, 45, 65, 165, 180, 265, 300, 340, 360]

    min_hue = 500
    max_hue = 0
    min_lum = 100
    max_lum = 0
    min_sat = 100
    max_sat = 0

    for colour in colours:
        H, S, L = colour
        min_hue = min(min_hue, H)
        max_hue = max(max_hue, H)
        min_lum = min(min_lum, L)
        max_lum = max(max_lum, L)
        min_sat = min(min_sat, S)
        max_sat = max(max_sat, S)

    return max_hue - min_hue < 100 and max_lum - min_lum < 50 and max_sat - min_sat < 50


def analogous(colours):
    pass


def matches(colours):
    does_match = False

    # monochromatic
    if monochromatic(colours):
        return True

    # analogous
    if analogous(colours):
        return True

    # offspring
    if offspring(colours):
        return True

    return False


def classification(colour):
    H, S, L = colour


if __name__ == "__main__":
    main()
