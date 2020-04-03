
class Employee():
    """Crea un perfil de empleado """

    def __init__(self,fname,lname,anual_salary):
        """Inicializa atributos"""

        self.fname = fname
        self.lname = lname
        self.anual_salary = anual_salary

    def give_raise(self,add_salary=5000):
        """Anumenta el salario """
        self.anual_salary += add_salary
