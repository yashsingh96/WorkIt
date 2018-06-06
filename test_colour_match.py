from unittest import TestCase

from colour_match import monochromatic, offspring


class TestColourMatch(TestCase):
    def test_monochromatic(self):
        is_mono = [(111, 35, 50), (88, 35, 90), (135, 35, 40)]
        self.assertTrue(monochromatic(is_mono))

    def test_monochromatic_false(self):
        not_mono = [(40, 35, 15), (88, 35, 50), (135, 35, 20)]
        self.assertFalse(monochromatic(not_mono))

    def test_offspring(self):
        is_offspring = [(61, 64, 64), (129, 44, 36)]
        self.assertTrue(offspring(is_offspring))

    def test_offspring_false(self):
        not_offspring = [(61, 64, 64), (292, 60, 60)]
        self.assertFalse(offspring(not_offspring))
