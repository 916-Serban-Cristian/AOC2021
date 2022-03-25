with open('input.txt', 'r') as f:
    risks = list(map(lambda x: list(map(int, x)), f.read().split('\n')))
total_risks = list(map(lambda x: list(map(lambda y: float('inf'), x)), risks))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
queue = [(0, 0)]
total_risks[0][0] = 0
while len(queue):
    i, j = queue.pop(0)
    for k in range(4):
        next_i = i + dx[k]
        next_j = j + dy[k]
        if next_i < 0 or next_i >= len(risks) or next_j < 0 or next_j >= len(risks[0]):
            continue
        if total_risks[i][j] + risks[next_i][next_j] < total_risks[next_i][next_j]:
            total_risks[next_i][next_j] = total_risks[i][j] + risks[next_i][next_j]
            queue.append((next_i, next_j))
print(total_risks[-1][-1])
