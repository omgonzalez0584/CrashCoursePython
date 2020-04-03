#Sumar dos numeros

while True:
    num1 = input("Introduzca el primer numero('exit' para salir): ")
    num2 = input("Introduzca el segundo numero('exit' para salir): ")
    if num1 == 'exit' or num2 == 'exit':
        break
    else:
        try:
            suma = int(num1) + int(num2)
        except ValueError:
            print("Error, debe ingresar numeros! ")
        else:
            print("La suma es: " + str(suma))
