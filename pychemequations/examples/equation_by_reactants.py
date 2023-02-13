from pychemequations.chemequations import ChemicalEquations

ce = ChemicalEquations()

reaction = input("Input a chemical reaction (Br + H2O): ")
equation = ce.getEquation(reaction)
print(f"""
The equation is {equation.equation} 

The products of this reaction: {equation.products}
The reactants of this reaction: {equation.reactants}
""") # for example: 2hcl + na2o = 2nacl+h2o
     # products is [2nacl, h2o]
     # reactants is [2hcl, na2o]