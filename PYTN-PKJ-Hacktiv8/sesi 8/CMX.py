import numpy as np
import matplotlib.pyplot as plt


def visualCM(cm):
  n = len(cm)
  fig, ax = plt.subplots(figsize=(n+1, n+1))
  ax.imshow(cm)
  ax.grid(False)
  ticks = tuple(np.arange(n))
  ax.xaxis.set(ticks=ticks)
  ax.yaxis.set(ticks=ticks)
  ax.set_ylim(n-0.5, -0.5)
  for i in range(n):
      for j in range(n):
          ax.text(j, i, cm[i, j], ha='center', va='center', color='red', fontsize=12)
  plt.xlabel("predicted")
  plt.ylabel("actual")
  plt.title("Confusion Matrix")
  plt.show()