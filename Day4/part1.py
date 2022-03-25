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
winner = False
for nr in numbers:
    for board in boards:
        for line in board:
            for pair in line:
                if pair[0] == nr:
                    pair[1] = True
    for board in boards:
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
            s = 0
            for line in board:
                s += sum(map(lambda x: int(x[0]), list(filter(lambda x: x[1] is False, line))))
            print(s * int(nr))
            break
    if winner:
        break
