with open("input.txt", "r") as f:
    numbers = sorted(list(map(lambda x: int(x.strip()), f.read().split(','))))
# diffs = list(map(lambda x: sum(abs(x - nr) for nr in numbers), numbers)) fucking luck this worked
# print(min(diffs))
median = numbers[int(len(numbers) / 2)] if len(numbers) % 2 == 0 else (numbers[int(len(numbers) / 2)] + numbers[
    int(len(numbers) / 2 + 1)]) / 2
print(sum(map(lambda x: abs(x - median), numbers)))
