import numpy as np

infile = 'input.txt'

def read_inputs(infile):
    with open(infile, 'r') as f:
        draws = f.readline()
        draws = draws.strip().split(',')
        draws = [int(i) for i in draws]

        f.readline()
        lines = f.readlines()

    boards = []
    board = []
    for line in lines:
        if line == '\n':
            boards.append(np.asarray(board).astype(float))
            board = []
        else:
            board.append([int(i) for i in line.strip().split()])
    boards.append(np.asarray(board).astype(float))
    return draws, boards


def draw_number(number, boards, replacement = np.nan):
    for b in boards:
        b[b==number] = replacement
    return boards

def check_winner(boards):
    for b in boards:
        if (np.isnan(b).all(axis=0).any()) or (np.isnan(b).all(axis=1).any()):
            return b
    return None

def check_loser(boards):
    remaining_boards = []
    for b in boards:
        if not ((np.isnan(b).all(axis=0).any()) or
                 (np.isnan(b).all(axis=1).any())):
            remaining_boards.append(b)

    if len(remaining_boards) > 0:        
        return True, remaining_boards
    else:
        return False, b

draws, boards = read_inputs(infile)
for d in draws:
    boards = draw_number(d, boards)
    res = check_winner(boards)
    if not res is None:
        print(res)
        break

score = res[np.isfinite(res)].sum() * d
print(score)


################# Second part - which board wins last ####################

draws, boards = read_inputs(infile)
for d in draws:
    
    boards = draw_number(d, boards)
    cont, boards = check_loser(boards)
    if cont == False:
        break

print(boards)
res = boards
score = res[np.isfinite(res)].sum() * d
print(score)
