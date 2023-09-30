#per ora lo script funziona solo con i file di tipo "L0", devo aggiungere l'implementazione (ovvero quali righe selezionare) per i file di tipo "L6"

import csv
import matplotlib.pyplot as plt
import os


def estraiData(file):
    giorno_gg = file[-6:-4]
    giorno_mm = file[-8:-6]
    giorno_aa = file[-10:-8]
    giorno = giorno_gg+'/'+giorno_mm+'/'+giorno_aa
    return giorno


def plot(filecsv):
    data = estraiData(filecsv)
    with open(filecsv, newline="", encoding="ISO-8859-1") as filecsv:
        lettore = csv.reader(filecsv,delimiter=",")
        #header = next(lettore)
        #print(header)
        dati = [(riga[0],riga[2],riga[4],riga[6]) for riga in lettore]
        #isola le colonne importanti che considero per i grafici
        #riga[0] (data e ora) serve perchè altrimenti i valori sull'asse x non sono in ordine
        #perciò devo considerarla e poi rimuovere la data

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
        fig.suptitle('Dati Centralina Meteo ' + data) 
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


