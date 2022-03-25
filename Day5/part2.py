with open("input.txt") as f:
    lines = f.read().split('\n')
diagram = {}
for line in lines:
    points = line.split(' -> ')
    point1 = tuple(map(lambda x: int(x.strip()), points[0].split(',')))
    point2 = tuple(map(lambda x: int(x.strip()), points[1].split(',')))
    if point1[0] == point2[0]:
        x = point1[0]
        y = min(point1[1], point2[1])
        while y <= max(point1[1], point2[1]):
            if (x, y) not in diagram:
                diagram[(x, y)] = 1
            else:
                diagram[(x, y)] += 1
            y += 1
    elif point1[1] == point2[1]:
        y = point1[1]
        x = min(point1[0], point2[0])
        while x <= max(point1[0], point2[0]):
            if (x, y) not in diagram:
                diagram[(x, y)] = 1
            else:
                diagram[(x, y)] += 1
            x += 1
    else:
        x = point1[0]
        y = point1[1]
        x_dir = -1 if x > point2[0] else 1
        y_dir = -1 if y > point2[1] else 1
        while (x, y) != point2:
            if (x, y) not in diagram:
                diagram[(x, y)] = 1
            else:
                diagram[(x, y)] += 1
            x += x_dir
            y += y_dir
        if point2 not in diagram:
            diagram[point2] = 1
        else:
            diagram[point2] += 1
print(len(list(filter(lambda x: x >= 2, diagram.values()))))
