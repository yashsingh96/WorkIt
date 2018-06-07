from appropriate_check import too_revealing
from colour_match import get_colours, matches


def fit(image):
    pass


# Scores the outfit based on style
def get_style_score(image, gender):
    score = 0

    colours = get_colours(image, False)

    # If it doesn't match a colour scheme, it's ugly
    if not matches(colours):
        score -= 1

    # if untucked long button shirt, it's ugly
    if gender == "M" and not fit(image):
        score -= 1


def button_shirt(image, gender):
    pass


def capital_one_logo(image):
    pass


# Score outfit based on internship appropriateness
def get_appropriate_score(image, gender):
    score = 0

    # If showing too much skin (Men: shorts, tshirt, etc. Women: too-short shorts or skirts, etc.)
    if too_revealing(image, gender):
        score -= 1

    # If not a button shirt, more casual. If has capital one logo, gives some leeway
    if gender == "M":
        if not button_shirt(image, gender):
            score -= 1
        elif capital_one_logo(image):
            score += 1
