import csv #modulo csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv' #ruta del archivo
with open(filename) as f:
    reader = csv.reader(f) #Crea un objeto reader para abrir el archivo
    header_row = next(reader) # devuelve una lista con la siguiente linea

    #Imprime las cabeceras y posiciones
    for index , column_reader  in enumerate(header_row):
        print(index, column_reader)

    #Extra datos de cada columna
    dates , highs, lows = [] , [] , [] # Creando dos listas vacias

    for row in reader:
        #Manejo de excepciones cuando los datos viene vacios o incorrectos
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")#Formato de fecha
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "Missing Data...")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


    #Plotting data
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5) #alpha para colocar transparencia
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    #Format plott
    plt.title("Daily high and low tempetures - DeathValley 2014", fontsize=20)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate() #Colocar los datos de forma diagonal
    plt.ylabel('Tempeture(F)', fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()
