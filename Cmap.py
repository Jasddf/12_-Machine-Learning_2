import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10,10)

plt.clf()
heatmap = plt.imshow(data, cmap="RdYlGn", aspect='auto')
plt.colorbar(heatmap)
plt.title('Heatmap Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()