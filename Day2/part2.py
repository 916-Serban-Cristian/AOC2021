with open("input.txt", 'r') as f:
    commands = f.read().split('\n')
horizontal = 0
depth = 0
aim = 0
for cmd in commands:
    tokens = cmd.strip().split()
    name = tokens[0].strip()
    val = int(tokens[1].strip())
    if name == 'forward':
        horizontal += val
        depth += aim * val
    elif name == 'down':
        aim += val
    elif name == 'up':
        aim -= val
print(horizontal * depth)
