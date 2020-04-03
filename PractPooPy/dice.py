
from random import randint #importando la funcion randint del modulo random

class Dice():
    """Clase que simula un dado"""
    def __init__(self):
        """Constructor que setea el atributo lado"""
        self.sides = 6

    def roll_dice(self):
        """Metodo que simula la tirada de un dado"""
        self.sides = randint(1,6)
        print("Tirando dados....")
        print("resultado: " + str(self.sides))


#Cuerpo principal del archivo

mi_dado = Dice()
print("\nResultados aleatorios de arrojar el dado")
for i in range(1,11):
    mi_dado.roll_dice()
