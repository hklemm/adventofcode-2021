import numpy as np
from skimage import measure
from skimage import filters

infile = 'input.txt'
# infile = 'test.txt'
with open(infile, 'r') as f:
    d = f.readlines()

nums = np.asarray([[int(l) for l in line.strip()] for line in d])
x_delta = np.diff(nums, axis=1)
y_delta = np.diff(nums, axis=0)

x_likelies = np.zeros_like(nums)
y_likelies = np.zeros_like(nums)


for i in range(x_delta.shape[1]):
    if i == 0:
        x_likelies[:,i] = x_delta[:,i]>0
    else:
        x_likelies[:,i] = (x_delta[:,i-1]<0)&(x_delta[:,i]>0) 

x_likelies[:,-1] = x_delta[:,-1]<0

for i in range(y_delta.shape[0]):
    if i == 0:
        y_likelies[0] = y_delta[i]>0
    else:
        y_likelies[i] = (y_delta[i-1]<0)&(y_delta[i]>0) 

y_likelies[-1] = y_delta[-1]<0

lows = x_likelies*y_likelies
risk_pts = nums[lows.astype(bool)]
risk_score = np.sum(risk_pts+1)

print('Risk score : %d'%risk_score)

basin_boundaries = nums==9

basin_map = np.ones_like(nums)
basin_map[basin_boundaries] = 0

lowpoints = np.argwhere(lows)

basins, labels = measure.label(basin_map,
                               background = 0,
                               return_num=True,
                               connectivity=1)

plt.matshow(basins)
plt.colorbar()
plt.show()

basin_sizes = [basins[basins==l].size for l in range(1, labels+1)]
basin_sizes.sort()

result = basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]
print (result)

    
