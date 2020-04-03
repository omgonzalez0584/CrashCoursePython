from random import randint

class Dice():
    """ Clase que representa a un Dado"""

    def __init__(self,num_sides=6):
        """Assume a six-sided dice."""
        self.num_sides = num_sides

    def roll(self):
        """Roll Dice and return the result."""
        return randint(1,self.num_sides)
