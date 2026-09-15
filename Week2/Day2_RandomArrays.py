import numpy as np

random_integers = np.random.randint(1, 101, size=10)

print("Random Integers:")
print(random_integers)
print("Minimum:", random_integers.min())
print("Maximum:", random_integers.max())

random_floats = np.random.uniform(0, 1, size=10)

print("\nRandom Floats:")
print(random_floats)
print("Minimum:", random_floats.min())
print("Maximum:", random_floats.max())
