with open("input.txt", 'r') as f:
    lines = f.read().split('\n')
outputs = [item for sublist in list(map(lambda x: x.strip().split(), list(map(lambda x: x.split('|')[1], lines)))) for
           item in sublist]
print(len(list(filter(lambda x: len(x) in {2, 3, 4, 7}, outputs))))
