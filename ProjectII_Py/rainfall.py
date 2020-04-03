import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates , rains = [] , []
    for row in reader:
        #Fechas
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)

        #Lluvias
        rain = float(row[19])
        rains.append(rain)


plt.bar(dates,rains,color='blue')
plt.title("Grafica de precipitaciones en Alaska - Julio",fontsize=24)
plt.xlabel("Dias de Lluvia",fontsize=15)
plt.ylabel("Indice de Precipitacion",fontsize=15)

plt.show()
