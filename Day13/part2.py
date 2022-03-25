def print_paper():
    global paper
    for line in paper:
        for char in line:
            print(char, end='')
        print()


def fold_paper(fold):
    global paper, max_x, max_y
    fold[1] = int(fold[1])
    new_paper = []
    if fold[0] == 'y':
        for i in range(fold[1]):
            new_line = []
            for j in range(max_x + 1):
                new_line.append('#' if paper[i][j] == '#' or paper[max_y - i][j] == '#' else '.')
            new_paper.append(new_line)
        max_y = fold[1] - 1
    else:
        for i in range(max_y + 1):
            new_line = []
            for j in range(fold[1]):
                new_line.append('#' if paper[i][j] == '#' or paper[i][max_x - j] == '#' else '.')
            new_paper.append(new_line)
        max_x = fold[1] - 1
    paper = new_paper


with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')
dots = list(map(lambda x: tuple(map(int, x.split(','))), lines[0].split('\n')))
folds = list(map(lambda x: x.replace('fold along ', '').split('='), lines[1].split('\n')))
max_x = max(dots, key=lambda x: x[0])[0]
max_y = max(dots, key=lambda x: x[1])[1]
paper = []
for i in range(max_y + 1):
    new_line = []
    for j in range(max_x + 1):
        new_line.append('#' if (j, i) in dots else '.')
    paper.append(new_line)
for fold in folds:
    fold_paper(fold)
print_paper()
