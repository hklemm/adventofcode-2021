import numpy as np


def decode(indata, output):

    # The actual corect mappings
    numbers = {'abcefg' : 0,
               'cf' : 1,
               'acdeg' : 2,
               'acdfg' : 3,
               'bcdf' : 4,
               'abdfg' : 5,
               'abdefg' : 6,
               'acf' : 7,
               'abcdefg' : 8,
               'abcdfg' : 9}

    # count how often each letter appears
    nums = {i : 0 for i in ['a','b','c','d','e','f','g']}
    for i in indata:
        if len(i) == 2:
            one = i
        elif len(i) == 3:
            seven = i
        elif len(i) == 4:
            four = i
        for k in i:            
            nums[k] += 1
    
    res ={}

    for i,k in nums.items():
        if k == 4:
            res[i] = 'e'
        elif k == 6:
            res[i] = 'b'
        elif k == 7:
            if i in four:
                res[i] = 'd'
            else:
                res[i] = 'g'
        elif k == 8:
            if i in one:
                res[i] = 'c'
            else:
                res[i] = 'a'
        elif k == 9:
            res[i] = 'f'

    # decoded_output
    result = []
    for op in output:
        decoder = [res[i] for i in op]
        number = numbers[''.join(sorted(decoder))]
        result.append(number)            
            
    return result


infile = 'input.txt'

with open(infile, 'r') as f:
    data = f.readlines()

inputs = []
outputs = []


for d in data:
    a, b = d.strip().split('|')
    inputs.append(a.strip().split())
    outputs.append(b.strip().split())

inputs = [[''.join(sorted(i)) for i in k] for k in inputs]
outputs = [[''.join(sorted(i)) for i in k] for k in outputs]
    
ctr = 0
for i in outputs:
    for d in i:
        if len(d)==2 or len(d)==3 or len(d)==4 or len(d)==7:
            ctr += 1

print(ctr)

added = 0
for i, o in zip(inputs, outputs):
    print(i, o)
    res = decode(i,o)
    val = 1000*res[0] + 100*res[1] + 10*res[2] + res[3]
    print(val)
    added += val
            
'''
collection = []


def assign_possibles(i, possibles):
    if len(i) == 2:
        possibles[1].append(i)
    elif len(i) == 3:
        possibles[7].append(i)
    elif len(i) == 4:
        possibles[4].append(i)
    if len(i) == 5:
        possibles[2].append(i)
        possibles[3].append(i)
        possibles[5].append(i)
    if len(i) == 6:
        possibles[6].append(i)
        possibles[9].append(i)
        possibles[0].append(i)
    if len(i) == 7:
        possibles[8].append(i)
    return possibles

for ip,op in zip(inputs, outputs):
    possibles = {i : [] for i in range(0,10)}
    for s in ip:
        possibles = assign_possibles(s, possibles)
    for s in op:
        possibles = assign_possibles(s, possibles)
        
    collection.append(possibles)
'''


