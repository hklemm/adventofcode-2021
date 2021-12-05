import numpy as np

dtype = [('direction', 'S10'), ('amount', 'i8')]
a = np.loadtxt('input.txt', dtype=dtype)

forward = np.sum(a['amount'][a['direction']==b'forward'])
depth = np.sum(a['amount'][a['direction']==b'down']) - np.sum(a['amount'][a['direction']==b'up'])
print(forward*depth)


############# Second part################
aim = 0
forward = 0
depth = 0

for i in a:
    if i['direction'] == b'forward' :
        forward += i['amount']
        depth += i['amount']*aim
    elif i['direction'] == b'up' :
        aim -= i['amount']
    elif i['direction'] == b'down' :
        aim += i['amount']

print(forward, depth, aim, forward*depth)        

