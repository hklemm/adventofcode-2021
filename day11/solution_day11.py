import numpy as np

with open('input.txt', 'r') as f:
    d = f.readlines()

data = np.array([[int(i) for i in l.strip()] for l in d])

def flash(data, i, j):
    mask = data > 0
    if i > 0:        
        data[i-1,j] += 1
        if j > 0:
            data[i-1,j-1] += 1
        if j < data.shape[1]-1:
            data[i-1,j+1] += 1
    if i < data.shape[0]-1:
        data[i+1,j] += 1
        if j > 0:
            data[i+1,j-1] += 1
        if j < data.shape[1]-1:
            data[i+1,j+1] += 1
    if j>0:
        data[i,j-1] += 1
    if j<data.shape[1]-1:
        data[i,j+1] += 1
    data[i,j] = 0
    data*=mask
    return data
            
            
            
def time_step(data):
    data += 1
    flashed_out = False
    while not flashed_out:
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if data[i,j] > 9:
                    data = flash(data, i,j)
        if (data<10).all():
            flashed_out = True
    return data

flashes = 0

i = 0
# for i in range(195):
while not (data==0).all():
    data = time_step(data)
    #flashes += np.sum(data==0)
    i+=1
print(i)
