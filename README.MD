# pychemequations
A small package for working with chemical equations. 

Actually, it's a parser of this site: https://chemequations.com/en/

## Getting products and coefficents of reaction by reactants.

```python
from pychemequations.chemequations import ChemicalEquations
from pychemequations.equation import Equation

ce = ChemicalEquations()

equation: list[Equation] | Equation = ce.getEquation(reaction)

```
As you can see, the ```getEquation(reaction)``` method may return both a equation and a list of equations. 

## Getting random reaction
Just use getRandomReaction() method for this. It return Equation object as well.
```python
equation = ce.getRandomReaction()
print(equation.equation)
```


### to be continued
