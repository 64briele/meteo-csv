#aggiugngere: unità di misura nelle ordinate, meno etichette nell'asse x, automatizzare la scelta del file da visualizzare, 

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np
import csv


with open("../app-meteo/csv/L0220525.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv,delimiter=",")
    #header = next(lettore)
    #print(header)
    dati = [(riga[0],riga[2],riga[4],riga[6]) for riga in lettore]
#isola le colonne importanti che considero per i grafici
#riga[0] (data e ora) serve perchè altrimenti i valori sull'asse x non sono in ordine
#per ciò devo considerarla e poi rimuovere la data


giorno = dati[2][0]
print(giorno)

minuti = 10
intervallo = int(minuti/10)


data_ora = [dati[i][0] for i in range(2, 146, intervallo)]
#ci sono un totale di 144 valori misurati in altrettanti tempi
#rimuove la data da ogni elemento della lista con data e ora_soltanto
ora_soltanto = [ora[8:] for ora in data_ora]


ora_corretta = []
for ora in ora_soltanto:
    if len(ora)==11:
        ora_corretta.append(ora[:5]+ora[-3:])
    else:
        ora_corretta.append(ora[:4]+ora[-3:])


print(ora_corretta)
print(len(ora_corretta))

xlist = ora_corretta

#riduce il range di valori considerati per il grafico
pa_10min = [float(dati[i][1]) for i in range(2, 146, intervallo)]
ta_10min = [float(dati[i][2]) for i in range(2, 146, intervallo)]        
rh_10min = [float(dati[i][3]) for i in range(2, 146, intervallo)]

fig, axs = plt.subplots(3)          
#array ad 1 dimensione di grafici
fig.suptitle('Dati Centralina Meteo 25/5/22')
axs[0].plot(xlist, pa_10min)
axs[0].set_title("Pressione Atmosferica")
axs[1].plot(xlist, ta_10min, 'tab:orange')
axs[1].set_title("Temperatura dell'aria")
axs[2].plot(xlist, rh_10min, 'tab:green')
axs[2].set_title("Umidità Relativa")

#rimuove i valori segnati sull'asse x di ogni grafico
#non può essere trasformato in una "lista" di comandi per qualche motivo
axs[0].set_xticks([])
axs[1].set_xticks([])  
axs[2].set_xticks([])   

plt.show()
