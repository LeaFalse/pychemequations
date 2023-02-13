import requests
from equation import Equation
from pychemequations.chemeparser import Parser


class ChemicalEquations:
    """
    PyChemicalEquations main class to send requests and get equations
    """
    def __init__(self):
        self.url = "https://chemequations.com/ru/"

    def getEquation(self, reaction: str) -> Equation | list[Equation]:
        """
        Default chem equation search

        :param reaction: Chemical reaction. Something like this: Na + HCl

        :return: Equation or list of equations, if there's more than one
        """
        response = requests.get(self.url, {"s": reaction}).text
        return Parser.getEquation(response)

    def getRandomReaction(self) -> Equation:
        """
        Get random reaction

        :return: Random reaction
        """
        response = requests.get(f"{self.url}random", allow_redirects=True).text
        return Parser.getEquation(response)

    def advancedSearch(self, reactants: list = None, products: list = None) -> list[Equation]:
        """
        Advanced search of chemical reactions, by reactants and products.

        :param reactants: List of elements, which is reactants of reaction
        :param products: List of elements, which is products of reaction

        :return: List of  found reactions with this reactants and products
        """
