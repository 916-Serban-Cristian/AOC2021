with open("input.txt", "r") as f:
    numbers = f.read().split(',')
lanternfish = list(map(lambda x: int(x.strip()), numbers))
for _ in range(80):
    new_lanternfish = lanternfish.copy()
    for idx, fish in enumerate(lanternfish):
        if fish == 0:
            new_lanternfish.append(8)
            new_lanternfish[idx] = 7
        new_lanternfish[idx] -= 1
    lanternfish = new_lanternfish
print(len(lanternfish))
