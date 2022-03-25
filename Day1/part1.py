with open("input.txt", 'r') as f:
    depths = f.read().split('\n')
depths = list(map(lambda x: int(x.strip()), depths))
nr_inc = 0
for i in range(1, len(depths)):
    if depths[i - 1] < depths[i]:
        nr_inc += 1
print(nr_inc)
