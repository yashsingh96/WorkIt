from _bisect import bisect


def main():
    is_mono = [(111, 5, 10), (88, 5, 10), (135, 5, 10)]
    print(monochromatic(is_mono))

    not_mono = [(40, 5, 10), (88, 5, 10), (135, 5, 10)]
    print(monochromatic(not_mono))


def monochromatic(colours):
    hue_vals = [15, 45, 65, 165, 180, 265, 300, 340, 360]
    colour_vals = 'ROYGCBPVR'

    curr_colour = bisect(hue_vals, colours[0][0])

    for colour in colours:
        H, S, L = colour

        if curr_colour != bisect(hue_vals, H):
            return False

    return True


def offspring(colours):
    pass


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
