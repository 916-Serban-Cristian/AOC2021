with open("input.txt", "r") as f:
    numbers = list(map(lambda x: int(x.strip()), f.read().split(',')))
# diffs = list(map(lambda x: sum(abs(x - nr)*(abs(x - nr) + 1)/2 for nr in numbers), numbers)) fucking luck this worked
# print(min(diffs))
median = int(sum(numbers) / len(numbers))
if len(numbers) % 2 == 1:
    median += 1
print(sum(map(lambda x: abs(x - median) * (abs(x - median)+1) / 2, numbers)))
