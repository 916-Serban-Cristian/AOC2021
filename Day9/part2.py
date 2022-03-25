from math import prod


def flood(start_i, start_j):
    global visited, heights, current_basin
    current_basin += 1
    visited[start_i][start_j] = True
    current_height = heights[start_i][start_j]
    for k in range(4):
        neighbour_height = heights[start_i + dx[k]][start_j + dy[k]]
        if neighbour_height == -1 or visited[start_i + dx[k]][start_j + dy[k]]:
            continue
        if neighbour_height > current_height:
            flood(start_i + dx[k], start_j + dy[k])


with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
heights = [[-1] * (len(lines[0]) + 2)]
visited = [[True] * (len(lines[0]) + 2)]
for line in lines:
    new_line = [-1]
    new_visited = [True]
    for height in line:
        new_line.append(int(height))
        new_visited.append(False if new_line[-1] != 9 else True)
    new_line.append(-1)
    new_visited.append(True)
    heights.append(new_line)
    visited.append(new_visited)
heights.append([-1] * (len(lines[0]) + 2))
visited.append([True] * (len(lines[0]) + 2))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
lows = []
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
            lows.append((i, j))
basins = []
for low in lows:
    current_basin = 0
    flood(low[0], low[1])
    basins.append(current_basin)
print(prod(list(reversed(sorted(basins)))[:3]))
