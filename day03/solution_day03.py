import numpy as np

infile = 'input.txt'

diagnostics = []

with open(infile, 'r') as f:
    data = f.readlines()

arr = np.asarray([[int(i[k]) for k in range(len(data[0])-1)] for i in data])

byte = 2**np.arange(arr.shape[-1], 0, -1)/2

res = np.round(arr.sum(axis=0)/len(arr))

mcb = res.copy().astype(int)

gamma = (byte*res).sum()
epsilon = np.sum(byte) - gamma

print (gamma, epsilon)
print(gamma*epsilon)

################# Second part ################

oxy = arr.copy()
co2 = arr.copy()

for i,k in enumerate(mcb):
    count = np.count_nonzero(oxy[:,i])
    if len(oxy) == 1:
        break
    else:
        if count >= len(oxy)/2:
            oxy = oxy[oxy[:,i] == 1]
        else:
            oxy = oxy[oxy[:,i] == 0]

for i,k in enumerate(mcb):
    count = np.count_nonzero(co2[:,i])
    if len(co2) == 1:
        break
    else:
        if count >= len(co2)/2:
            co2 = co2[co2[:,i] == 0]
        else:
            co2 = co2[co2[:,i] == 1]


oxy_rate = (byte*oxy).sum()
co2_rate = (byte*co2).sum()

lsr = oxy_rate * co2_rate
print(oxy_rate, co2_rate, lsr)

            

#break

#print(arr)
