from copy import deepcopy
from bitstring import BitArray

with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
oxygens = deepcopy(lines)
co2s = deepcopy(lines)
pos = 0
while len(oxygens) != 1:
    zero = 0
    one = 0
    for nr in oxygens:
        if nr[pos] == '0':
            zero += 1
        else:
            one += 1
    temp_oxygens = []
    if one >= zero:
        for nr in oxygens:
            if nr[pos] == '1':
                temp_oxygens.append(nr)
    else:
        for nr in oxygens:
            if nr[pos] == '0':
                temp_oxygens.append(nr)
    oxygens = temp_oxygens
    pos += 1
pos = 0
while len(co2s) != 1:
    zero = 0
    one = 0
    for nr in co2s:
        if nr[pos] == '0':
            zero += 1
        else:
            one += 1
    temp_co2s = []
    if zero > one:
        for nr in co2s:
            if nr[pos] == '1':
                temp_co2s.append(nr)
    else:
        for nr in co2s:
            if nr[pos] == '0':
                temp_co2s.append(nr)
    co2s = temp_co2s
    pos += 1

print(BitArray(list(map(lambda x: int(x), oxygens[0]))).uint * BitArray(list(map(lambda x: int(x), co2s[0]))).uint)
