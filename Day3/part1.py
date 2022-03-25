from bitstring import BitArray

with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
ones = [0] * len(lines[0])
zeros = [0] * len(lines[0])
for nr in lines:
    for idx, bit in enumerate(nr):
        if bit == '0':
            zeros[idx] += 1
        else:
            ones[idx] += 1
gamma = [0] * len(lines[0])
epsilon = [0] * len(lines[0])
for idx, count in enumerate(ones):
    if count > zeros[idx]:
        gamma[idx] = 1
        epsilon[idx] = 0
    else:
        gamma[idx] = 0
        epsilon[idx] = 1
print(BitArray(gamma).uint * BitArray(epsilon).uint)
