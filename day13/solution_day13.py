import numpy as np
import matplotlib.pyplot as plt
infile = 'input.txt'

with open(infile, 'r') as f:
    data = f.readlines()


xmax = 0
ymax = 0
x_coords = []
y_coords = []
folds = []
for line in data:
    if not line.startswith('fold') and len(line)>1:
        l = line.strip().split(',')
        x = int(l[0])
        y = int(l[1])
        x_coords.append(x)
        y_coords.append(y)
        xmax = max(xmax, x)
        ymax = max(ymax, y)
    elif len(line)>1:
        l = line.strip().split()
        f = l[-1].split('=')
        folds.append((f[0], int(f[1])))


paper = np.zeros((ymax+1+ymax%2, xmax+1+xmax%2), dtype=int)
paper[y_coords, x_coords] = 1

def foldit(paper, fold):
    offset = np.asarray(paper.shape)%2
    if fold[0] == 'x':
        # new_paper = np.zeros((fold[1]+1, paper.shape[1]), dtype=int)
        new_paper = paper[:, :fold[1]] 
        old_paper = paper[:, fold[1]+1:] 
        new_paper = new_paper+old_paper[:, ::-1]
        new_paper[new_paper>0] = 1
    else:
        new_paper = paper[:fold[1], :]
        old_paper = paper[fold[1]+1:, :] 
        new_paper = new_paper+old_paper[::-1, :]
        new_paper[new_paper>0] = 1

    return new_paper


for i, fold in enumerate(folds):    
    paper = foldit(paper, fold)
    if i == 0:
        print(np.sum(paper))

plt.matshow(paper)
plt.show()
