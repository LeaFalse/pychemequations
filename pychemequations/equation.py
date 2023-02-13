
class Equation:
    """
    It's just chemical equation object
    """
    def __init__(self, equation: str) -> None:
        filters = ["2\xa0", " ", "\n"]
        self.equation = equation
        for filter_ in filters:
            self.equation = self.equation.replace(filter_, "")
        self.scheme = self.equation.split("→")
        self.reactants = self.scheme[0].split("+")
        self.products = self.scheme[1].split("+")
