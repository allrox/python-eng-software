import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color="red")

# plt.xticks(x)
plt.ylabel("Legenda do Eixo Y")
plt.xlabel("Legenda do Eixo X")
plt.title("Gráfico Python")
plt.show()
