import matplotlib.pyplot as plt

x = [27, 48, 28, 24, 49]
lab = ["A", "B", "C", "D", "E"]
col = ["honeydew", "tomato", "orchid", "navy", "darkred"]
plt.pie(x, startangle=90, labels=x, colors=col)
plt.legend(lab, loc=2)
plt.tight_layout()
plt.savefig("zad1.png")
plt.show()
