
import numpy as np

def check_syntax(line):
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']

    pairings = {')' : '(',
                ']' : '[',
                '}' : '{',
                '>' : '<',
                }

    close_pairing = {i[1] : i[0] for i in pairings.items()}
    
    current_open = []

    for l in line:
        if l in openers:
            current_open.append(l)
        elif l in closers:
            if current_open[-1] == pairings[l]:
                current_open.pop(-1)
            else:
                return l

    closing_string = [close_pairing[i] for i in current_open[::-1]]
            
    return closing_string


def calc_score(res):
    closing_scores = {')' : 1,
                      ']' : 2,
                      '}' : 3,
                      '>' : 4}
    score = 0
    for i in res:
        score*=5
        score+=closing_scores[i]
    return score




scores = {')' : 3,
          ']' : 57,
          '}' : 1197,
          '>' : 25137}



with open('input.txt', 'r') as f:
    nav = f.readlines()

results = []
score = 0
closing_scores = []
for line in nav:
    line = line.strip()
    res = check_syntax(line)
    if not isinstance(res, list):
        results.append(res)
        score+=scores[res]
    else:
        print(res)
        closing_scores.append(calc_score(res))

        
print('The error score is: %d'%score)
        
print('The Middle closing score is %d'%(np.median(closing_scores)))
