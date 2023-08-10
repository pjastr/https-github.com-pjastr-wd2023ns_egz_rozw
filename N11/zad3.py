import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_excel("gastro11.xlsx", header=None).T
dane2 = dane.iloc[1:, ].copy()
dane2.columns = dane.iloc[0,]
dane2["Rok"] = pd.Series(dane2["Rok"], dtype=int)
dane2["Wartosc"] = pd.Series(dane2["Wartosc"], dtype=int)
restauracje = dane2[dane2["Typy placówek"] == "restauracje"]
bary = dane2[dane2["Typy placówek"] == "bary"]
stolowki = dane2[dane2["Typy placówek"] == "stołówki"]
pg = dane2[dane2["Typy placówek"] == "punkty gastronomiczne"]
lata = restauracje["Rok"]
plt.bar(lata - 0.3, restauracje["Wartosc"], width=0.2, label="restauracje")
plt.bar(lata - 0.1, bary["Wartosc"], width=0.2, label="bary")
plt.bar(lata + 0.1, stolowki["Wartosc"], width=0.2, label="stołówki")
plt.bar(lata + 0.3, pg["Wartosc"], width=0.2, label="punkty gastronomiczne")
plt.xticks(lata)
plt.title("Dane o gastonomii")
plt.ylabel("Ilość punktów")
plt.legend()
plt.tight_layout()
plt.savefig("zad3.pdf")
plt.show()
