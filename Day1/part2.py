with open("input.txt", 'r') as f:
    depths = f.read().split('\n')
depths = list(map(lambda x: int(x.strip()), depths))
windows = [depths[i] + depths[i + 1] + depths[i + 2] for i in range(len(depths) - 2)]
nr_inc = 0
for i in range(1, len(windows)):
    if windows[i - 1] < windows[i]:
        nr_inc += 1
print(nr_inc)
