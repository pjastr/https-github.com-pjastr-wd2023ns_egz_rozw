import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("ceny11.csv", sep=";", decimal=",")
pstrag = data[data["Rodzaje produktów"] == "pstrąg świeży niepatroszony - za 1 kg"]
morszczuk = data[data["Rodzaje produktów"] == "filety z morszczuka mrożone - za 1kg"]
sledz = data[data["Rodzaje produktów"] == "śledź solony, niepatroszony - za 1kg"]
rok = pstrag["Rok"]
plt.plot(rok, pstrag["Wartosc"], "--", linewidth=2, label="pstrąg")
plt.plot(rok, morszczuk["Wartosc"], ":", linewidth=4, label="morszczuk")
plt.plot(rok, sledz["Wartosc"], "-.", linewidth=3, label="śledź")
plt.title("Dane za ceny wybranych ryb")
plt.legend()
plt.xlabel("Lata")
plt.ylabel("Cena w zł")
plt.savefig("zad2.jpg")
plt.show()
