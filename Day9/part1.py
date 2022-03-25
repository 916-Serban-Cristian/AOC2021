with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
heights = [[-1] * (len(lines[0]) + 2)]
for line in lines:
    new_line = [-1]
    for height in line:
        new_line.append(int(height))
    new_line.append(-1)
    heights.append(new_line)
heights.append([-1] * (len(lines[0]) + 2))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
risk = 0
for i in range(1, len(lines) + 1):
    for j in range(1, len(lines[0]) + 1):
        current_height = heights[i][j]
        low = True
        for k in range(4):
            neighbour_height = heights[i + dx[k]][j + dy[k]]
            if neighbour_height == -1:
                continue
            if neighbour_height <= current_height:
                low = False
                break
        if low:
            risk += (current_height + 1)
print(risk)
