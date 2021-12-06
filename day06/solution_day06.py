import numpy as np

d = np.loadtxt('input.txt', delimiter=',', dtype=int)

fishies = np.zeros(9, dtype=int)

for i in d:
    fishies[i] += 1


print(fishies)
days = 256
for i in range(days):

    birthers = fishies[0]
    fishies[:-1] = fishies[1:]
    fishies[-1] = birthers
    fishies[6] += birthers

print (fishies.sum())

