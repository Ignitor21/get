import numpy as np
import matplotlib.pyplot as plt

# with open("settings.txt", "r") as settings:
#     tmp = [float(i) for i in settings.read().split('\n')]
#     print(tmp)

data_array = np.loadtxt("data.txt", dtype=int)
coef = np.loadtxt("settings.txt", dtype=float)

x = np.zeros(len(data_array))
y = data_array*coef[1]

for i in range(0, len(data_array)):
   x[i] = i*coef[0]


fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
#plt.scatter(x, y, marker="v", facecolor='r', edgecolor='k', linewidths = 0.5)
ax.plot(x, y, label="U(t)", color = "red", marker="o", markevery = 30)
ax.minorticks_on()
plt.grid(True)  
plt.xlabel("Время, с")
plt.ylabel("Напряжение на конденсаторе, В")
ax.set_title('Зависимость напряжение от времени в RC-цепи')
ax.set_xticks(np.arange(0, 13, 1))
ax.set_yticks(np.arange(0, 3, 0.25))
ax.text(7, 1.5, "Время зарядки: " + str(x[np.argmax(y)]))
ax.text(7, 2, "Время разраядки: " + str(12.05 - x[np.argmax(y)]))
ax.text
ax.legend()
fig.savefig("pic.png")
fig.savefig("pic.svg")
plt.show()