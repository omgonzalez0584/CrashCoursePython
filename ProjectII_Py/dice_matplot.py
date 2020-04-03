#Trabajando con libreria matplotlib
import matplotlib.pyplot as plt
from dice import Dice

def tirar_dados(repeticiones):
    """ Funcion que retorna los resultados de lanzar un dado"""
    resultados_temp = []
    for roll in range(repeticiones):
        result_temp  = my_dice.roll()
        resultados_temp.append(result_temp)
    return resultados_temp


def analizar_resultados(resulados):
    """Funcion que retorna las frecuencia de los resultados obtenidos """
    frecuencias_temp = []
    for value in range(1,my_dice.num_sides+1):
        fre_temp = results.count(value)
        frecuencias_temp.append(fre_temp)
    return frecuencias_temp


def graficar_resultados(frecuencias):
    """Grafica los resultados en un Bar chart """
    sides = [i for i in range(1,my_dice.num_sides+1)]
    plt.bar(sides,frecuencias,color='green')
    plt.xlabel("Lados")
    plt.ylabel("Frecuencia")
    plt.title("Resultados de Lanzar un Dado")
    plt.show()


#MAIN DEL PROGRAMA
while True:
    my_dice = Dice() #Instanciando objeto
    results = tirar_dados(1000) #Lanzando dado
    frecuencias = analizar_resultados(results) #Analizando resultados
    graficar_resultados(frecuencias) #Generando Grafica de Barra

    mantener_ejecucion = input("Mostrar mas resultados?(s/n): ")
    if mantener_ejecucion == 'n':
        break


##
