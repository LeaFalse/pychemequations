from bs4 import BeautifulSoup
from pychemequations.equation import Equation


class Parser:
    """
    Chemical Equations parser
    """

    @staticmethod
    def getEquation(response: str) -> Equation | list[Equation] | None:
        """
        Parse chemical reactions from site response

        :param response: HTML site response
        :return: Equation or list of equations
        """
        soup = BeautifulSoup(response, 'html.parser')
        # get string equation by .equation
        string_equation = soup.find(class_="equation").get_text()
        equation = Equation(string_equation)
        if equation.products == ["?"]:
            # find all equations in tbody by <a>
            tbody = soup.find("tbody")
            if not tbody:
                return None
            equations: list[Equation] = [
                Equation(e.get_text())
                for e in tbody.findAll("a")
            ]
            return equations
        return equation

