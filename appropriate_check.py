from PIL import Image
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import LabColor, sRGBColor


def too_revealing(image, gender="M"):
    image = Image.open("images/good/analogous.jpg")

    w, h = image.size
    # image = image.crop((w / 4, h / 5, w * 3 / 4, h * 4 / 5))
    # w, h = image.size


    pixelSize = (w * h) / 10000

    image = image.resize((round(image.size[0] / pixelSize), round(image.size[1] / pixelSize)), Image.NEAREST)
    w, h = image.size
    image.save("output.png")

    all_colours = list(image.getdata())

    # Convert from RGB to Lab Color Space
    white_skin = [convert_color(sRGBColor(255, 224, 189), LabColor), convert_color(sRGBColor(255, 205, 148), LabColor),
                  convert_color(sRGBColor(239, 175, 139), LabColor), convert_color(sRGBColor(142, 81, 62), LabColor),
                  convert_color(sRGBColor(126, 76, 62), LabColor), convert_color(sRGBColor(174, 127, 109), LabColor),
                  convert_color(sRGBColor(60, 27, 12), LabColor)]

    total_skin = 0

    for colour in all_colours:
        # Convert from RGB to Lab Color Space
        color2_lab = convert_color(sRGBColor(colour[0], colour[1], colour[2]), LabColor)

        min_dist = 200

        # Find the color difference
        for tone in white_skin:
            min_dist = min(delta_e_cie2000(tone, color2_lab), min_dist)

        # print(min_dist)

        if min_dist < 30:
            total_skin += 1

    total_skin = total_skin / (w * h)

    # debug
    print(total_skin)

    # male
    if total_skin > .12 and gender == "M":
        return True

    # female
    if total_skin > .20 and gender != "M":
        return True

    return False


def main():
    print(too_revealing("hi", "M"))


if __name__ == "__main__":
    main()
