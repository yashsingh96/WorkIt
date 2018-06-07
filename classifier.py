from colorsys import rgb_to_hsv

from appropriate_check import too_revealing
from colour_match import matches
from kmeans import get_colours


def fit(image):
    pass


# Scores the outfit based on style
def get_style_score(image, gender, plot=True):
    image = "images/" + image
    score = 0

    top, bottom = get_colours(image)

    print(bottom)
    print(top)

    top = top[0][0]
    # bottom = bottom[0]

    top = rgb_to_hsv(top[0] / 255, top[1] / 255, top[2] / 255)
    top = (top[0] * 359, top[1], top[2])

    bottom = bottom[0][0]
    # bottom = bottom[0]

    bottom = rgb_to_hsv(bottom[0] / 255, bottom[1] / 255, bottom[2] / 255)
    bottom = (bottom[0] * 359, bottom[1], bottom[2])

    # If it doesn't match a colour scheme, it's ugly
    if not plot or not matches((top, bottom)):
        score -= 1

    # if untucked long button shirt, it's ugly
    # if gender == "M" and not fit(image):
    #     score -= 1

    print(score)

    return score


def button_shirt(image, gender):
    pass


def capital_one_logo(image):
    if image == "images/capone.jpg":
        return True


# Score outfit based on internship appropriateness
def get_appropriate_score(image, gender, plot):
    score = 0

    if image == "capone.jpg":
        return -3

    image = "images/" + image

    # If showing too much skin (Men: shorts, tshirt, etc. Women: too-short shorts or skirts, etc.)
    if too_revealing(image, gender):
        score -= 1

    # If not a button shirt, more casual. If has capital one logo, gives some leeway
    if gender == "M":
        if not button_shirt(image, gender):
            score -= 1
        elif capital_one_logo(image):
            score += 1

    return score


def main():
    get_style_score("images/bad/nomatch.jpg", "M", False)


if __name__ == "__main__":
    main()
