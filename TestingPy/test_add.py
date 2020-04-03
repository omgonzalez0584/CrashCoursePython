#Testea la funcion add

import unittest #1. modulo unittest
import add as a#archivo que se va a testear

#Se crea una clase para la prueba
class TestAdd(unittest.TestCase):#Se hereda TestCase del modulo unittest

    def test_add_two_integers(self):
        self.assertEqual(4,a.add(2,2)) #Metodo que realiza la prueba
        self.assertEqual(0,a.add(2,-2))

    def test_add_two_floats(self):
        self.assertAlmostEqual(4,a.add(1.999,2.002),places = 2)

#programa principal
unittest.main()
