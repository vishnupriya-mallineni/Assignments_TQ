import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(50, 101, 50)

plt.hist(data, bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
