import unittest

from chemequations import ChemicalEquations


class TestEquations(unittest.TestCase):
    def setUp(self) -> None:
        self.ch = ChemicalEquations()

    def test_getOneEquation(self):
        self.assertEqual(self.ch.getEquation("Na+HCl").equation, "2 Na + 2 HCl → 2 NaCl + H2")

    def test_unknownEquation(self):
        self.assertFalse(self.ch.getEquation("NaO+Br"))
