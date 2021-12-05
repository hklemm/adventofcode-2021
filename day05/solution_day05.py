import numpy as np

infile = 'input.txt'

def read_input(infile):
    with open(infile, 'r') as f:
        lines = f.readlines()

    start_pts = []
    end_pts = []
    for l in lines:
        ll = l.strip().split('->')
        start_pts.append([int(i) for i in ll[0].split(',')])
        end_pts.append([int(i) for i in ll[1].split(',')])
    return np.asarray(start_pts), np.asarray(end_pts)

start_pts, end_pts = read_input(infile)


max_x = max(start_pts[:,0].max(), end_pts[:,0].max())
max_y = max(start_pts[:,1].max(), end_pts[:,1].max())

res_matrix = np.zeros((max_x+1, max_y+1))

for i in range(len(start_pts)):
    s = start_pts[i]
    e = end_pts[i]
    if (s[0] == e[0]):
        # print(res_matrix)
        if s[1] <= e[1]:
            res_matrix[s[1]:e[1]+1,s[0]:e[0]+1]+=1
        else:
            res_matrix[e[1]:s[1]+1,s[0]:e[0]+1]+=1
    elif (s[1] == e[1]):
        # print(res_matrix)
        if s[0] <= e[0]:
            res_matrix[s[1]:e[1]+1,s[0]:e[0]+1]+=1
        else:
            res_matrix[s[1]:e[1]+1,e[0]:s[0]+1]+=1
    else:
        continue
        # print(res_matrix)

danger = res_matrix.max()
danger = 2

m0 = res_matrix.copy()

print(len(res_matrix[res_matrix>=danger]))

###################### Part two #####################

res_matrix = np.zeros((max_x+1, max_y+1))

for i in range(len(start_pts)):
    s = start_pts[i]
    e = end_pts[i]
    # print(s, e)
    if (s[0] == e[0]):
        # print(res_matrix)
        if s[1] <= e[1]:
            res_matrix[s[1]:e[1]+1,s[0]:e[0]+1]+=1
        else:
            res_matrix[e[1]:s[1]+1,s[0]:e[0]+1]+=1
    elif (s[1] == e[1]):
        # print(res_matrix)
        if s[0] <= e[0]:
            res_matrix[s[1]:e[1]+1,s[0]:e[0]+1]+=1
        else:
            res_matrix[s[1]:e[1]+1,e[0]:s[0]+1]+=1
    else:
        # print(s, e)
        # This is the diagonal bit
        if (s[0] <= e[0]):
            x_ind = np.arange(s[0], e[0]+1)
        else:
            x_ind = np.arange(s[0], e[0]-1, step=-1)
        if (s[1] <= e[1]):
            y_ind = np.arange(s[1], e[1]+1)
        else:
            y_ind = np.arange(s[1], e[1]-1, step=-1)
        # print(x_ind, y_ind)
        res_matrix[y_ind, x_ind] +=1

            
            # print(res_matrix)

print(len(res_matrix[res_matrix>=danger]))
