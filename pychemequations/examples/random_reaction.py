from pychemequations.chemequations import ChemicalEquations

ce = ChemicalEquations()

equation = ce.getRandomReaction()
print(equation.equation)
