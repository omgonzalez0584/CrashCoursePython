#Grafica las variaciones de temperatura de San Francisco
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'san_fran.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [] , [] , []
    for row in reader:
        #Extract Dates
        current_date = datetime.strptime(row[0], "%m/%d/%Y").date()
        dates.append(current_date)

        #Extract Highs Tempeture
        high = int(row[1])
        highs.append(high)

        #Extract lows Tempeture
        low = int(row[3])
        lows.append(low)

#Graficar data
plt.plot(dates,highs,c='red',alpha = 0.5)
plt.plot(dates,lows,c='blue',alpha = 0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#formato de la grafica
plt.title("Temperaturas altas y bajas en San Francisco - 2014")
plt.xlabel("Fechas")
plt.ylabel("Temperaturas(F)")


plt.show()
