from collections import Counter

with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
out_sum = 0
for line in lines:
    line = line.split('|')
    inputs = line[0].strip().split()
    outputs = line[1].strip().split()
    digits = {i: "" for i in range(10)}
    signals = {i: None for i in "abcdefg"}
    digits[1] = [s for s in inputs if len(s) == 2][0]
    digits[4] = [s for s in inputs if len(s) == 4][0]
    digits[7] = [s for s in inputs if len(s) == 3][0]
    digits[8] = [s for s in inputs if len(s) == 7][0]
    inputs.remove(digits[1])
    inputs.remove(digits[4])
    inputs.remove(digits[7])
    inputs.remove(digits[8])
    signals['a'] = set(digits[7]).difference(set(digits[1])).pop()
    freqs = dict(Counter(''.join(inputs)))
    signals['e'] = list(freqs.keys())[list(freqs.values()).index(min(freqs.values()))]
    freqs.pop(signals['e'])
    signals['g'] = {letter for letter in freqs if freqs[letter] == 6}.difference(signals['a']).pop()
    possible_b = [letter for letter in freqs if freqs[letter] == 4]
    signals['b'] = possible_b[0]
    signals['c'] = possible_b[1]
    if len(set(digits[1]).difference(signals['c'])) == 2:
        signals['b'] = possible_b[1]
        signals['c'] = possible_b[0]
    signals['f'] = set(digits[1]).difference(signals['c']).pop()
    signals['d'] = set(digits[4]).difference({signals['b'], signals['c'], signals['f']}).pop()
    for letter in "abcefg":
        digits[0] += signals[letter]
    for letter in "acdeg":
        digits[2] += signals[letter]
    for letter in "acdfg":
        digits[3] += signals[letter]
    for letter in "abdfg":
        digits[5] += signals[letter]
    for letter in "abdefg":
        digits[6] += signals[letter]
    for letter in "abcdfg":
        digits[9] += signals[letter]
    inv_digits = {frozenset(v): k for k, v in digits.items()}
    out = ""
    for output in outputs:
        out += str(inv_digits[frozenset(output)])
    out_sum += int(out)
print(out_sum)
