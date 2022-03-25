from collections import Counter

with open('input.txt', 'r') as f:
    polymer, rules = f.read().split('\n\n')
rules = dict(map(lambda x: x.split(' -> '), rules.split('\n')))
for _ in range(10):
    new_polymer = ""
    for i in range(len(polymer) - 1):
        new_polymer = new_polymer + polymer[i]
        if polymer[i:i + 2] in rules:
            new_polymer = new_polymer + rules[polymer[i:i + 2]]
    new_polymer = new_polymer + polymer[-1]
    polymer = new_polymer
print(max(Counter(polymer).values()) - min(Counter(polymer).values()))
