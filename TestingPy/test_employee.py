#Testing de la clase empleado

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Prueba el funcionamiento de la clase Employee."""

    def setUp(self):
        """Setea los atributos y objetos para realizar pruebas."""
        self.my_employee = Employee('omar','gonzalez',3000)

    def test_give_default_raise(self):
        """Prueba aumento de salario por default."""
        self.my_employee.give_raise()
        self.assertEqual(8000,self.my_employee.anual_salary)

    def test_give_custom_raise(self):
        """Prueba que el amuento realizado manualmente este funcionado."""
        self.my_employee.give_raise(2000)
        self.assertEqual(5000,self.my_employee.anual_salary)

unittest.main()
