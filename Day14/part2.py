from collections import Counter
from time import perf_counter

start_time = perf_counter()
with open('input.txt', 'r') as f:
    polymer, rules = f.read().split('\n\n')
occurs = dict(Counter(polymer))
new_polymer = {}
for i in range(len(polymer) - 1):
    if polymer[i:i + 2] in new_polymer:
        new_polymer[polymer[i:i + 2]] += 1
    else:
        new_polymer[polymer[i:i + 2]] = 1
polymer = new_polymer
rules = dict(map(lambda x: x.split(' -> '), rules.split('\n')))
for _ in range(40):
    new_polymer = {}
    for pair in polymer:
        freq = polymer[pair]
        if pair in rules:
            new_pairs = (pair[0] + rules[pair], rules[pair] + pair[1])
            if new_pairs[0] in new_polymer:
                new_polymer[new_pairs[0]] += freq
            else:
                new_polymer[new_pairs[0]] = freq
            if new_pairs[1] in new_polymer:
                new_polymer[new_pairs[1]] += freq
            else:
                new_polymer[new_pairs[1]] = freq
            if rules[pair] in occurs:
                occurs[rules[pair]] += freq
            else:
                occurs[rules[pair]] = freq
        else:
            new_polymer[pair] += freq
    polymer = new_polymer
print(max(occurs.values()) - min(occurs.values()))
print(perf_counter() - start_time)