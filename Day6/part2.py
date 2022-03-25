with open("input.txt", "r") as f:
    numbers = list(map(lambda x: int(x.strip()), f.read().split(',')))
lanternfish = {i: numbers.count(i) for i in range(9)}
for _ in range(256):
    new_lanternfish = {i: 0 for i in range(9)}
    for age in lanternfish:
        if age == 0:
            new_lanternfish[8] += lanternfish[age]
            new_lanternfish[6] += lanternfish[age]
        else:
            new_lanternfish[age - 1] += lanternfish[age]
    lanternfish = new_lanternfish
print(sum(lanternfish.values()))
