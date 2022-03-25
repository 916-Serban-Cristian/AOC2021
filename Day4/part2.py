from copy import deepcopy

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
numbers = lines[0].split(',')
raw_boards = list(filter(lambda x: x != '', lines[1:]))
boards = []
while len(raw_boards):
    board = []
    for _ in range(5):
        temp_line = raw_boards.pop(0).split()
        line = list(map(lambda x: [x.strip(), False], temp_line))
        board.append(line)
    boards.append(board)
winners = []
winners_indexes = []
for nr in numbers:
    for board in boards:
        for line in board:
            for pair in line:
                if pair[0] == nr:
                    pair[1] = True
    for idx, board in enumerate(boards):
        if idx not in winners_indexes:
            winner = False
            for line in board:
                filtered_true = list(filter(lambda x: x[1] is True, line))
                if filtered_true == line:
                    winner = True
                    break
            cols = [list(map(lambda x: x[i], board)) for i in range(5)]
            for col in cols:
                filtered_true = list(filter(lambda x: x[1] is True, col))
                if filtered_true == col:
                    winner = True
                    break
            if winner:
                winners.append([deepcopy(board), nr])
                winners_indexes.append(idx)
s = 0
for line in winners[-1][0]:
    s += sum(map(lambda x: int(x[0]), list(filter(lambda x: x[1] is False, line))))
print(s * int(winners[-1][1]))
