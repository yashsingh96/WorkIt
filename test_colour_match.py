from unittest import TestCase

from colour_match import monochromatic, offspring, get_common_colours


class TestColourMatch(TestCase):
    def test_monochromatic(self):
        image = 'green-and-yellow.jpg'
        self.assertTrue(monochromatic(get_common_colours(image, True)))

    def test_monochromatic_false(self):
        image = 'green-and-yellow.jpg'
        self.assertFalse(monochromatic(get_common_colours(image)))

    def test_offspring(self):
        image = 'green-and-yellow.jpg'
        self.assertTrue(offspring(get_common_colours(image)))

    # def test_offspring_false(self):
    #     image = 'badoutfit.png'
    #     colours = get_common_colours(image, True)
    #     self.assertFalse(offspring(colours))
