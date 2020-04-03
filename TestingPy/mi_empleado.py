#Creacion de un objeto Employee

#Importando clase
from employee import Employee

mi_empleado = Employee('omar','gonzalez',3000)

#Imprimiendo atributos
print(mi_empleado.fname)
print(mi_empleado.lname)
print(mi_empleado.anual_salary)

#Llamando metodos de la clase
mi_empleado.give_raise()
print("New Anual Salary: " + str(mi_empleado.anual_salary))
