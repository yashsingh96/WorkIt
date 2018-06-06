from unittest import TestCase

from colour_match import monochromatic


class TestColourMatch(TestCase):
    def test_monochromatic(self):
        is_mono = [(111, 5, 10), (88, 5, 10), (135, 5, 10)]
        self.assertTrue(monochromatic(is_mono))

        not_mono = [(40, 5, 10), (88, 5, 10), (135, 5, 10)]
        self.assertFalse(monochromatic(not_mono))
