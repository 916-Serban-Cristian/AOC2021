with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
octopuses = []
for line in lines:
    new_line = []
    for octopus in line:
        new_line.append([int(octopus), False])
    octopuses.append(new_line)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
flashes = 0
for _ in range(100):
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            octopuses[i][j][0] += 1
    done_flashing = False
    while not done_flashing:
        done_flashing = True
        for i in range(len(octopuses)):
            for j in range(len(octopuses[0])):
                current_octopus = octopuses[i][j]
                if current_octopus[0] > 9 and not current_octopus[1]:
                    flashes += 1
                    done_flashing = False
                    current_octopus[1] = True
                    for k in range(8):
                        next_i = i + dx[k]
                        next_j = j + dy[k]
                        if next_i < 0 or next_i >= len(octopuses) or next_j < 0 or next_j >= len(octopuses[0]):
                            continue
                        neighbour_octopus = octopuses[next_i][next_j]
                        neighbour_octopus[0] += 1
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            if octopuses[i][j][1]:
                octopuses[i][j] = [0, False]
print(flashes)
