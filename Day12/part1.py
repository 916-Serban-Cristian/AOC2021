def DFS(node):
    global visited, paths
    if node.islower():
        visited.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            if neighbour == 'end':
                paths += 1
            else:
                DFS(neighbour)
                if neighbour.islower():
                    visited.remove(neighbour)


with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
graph = {}
for line in lines:
    n1, n2 = line.split('-')
    if n1 in graph:
        graph[n1].append(n2)
    else:
        graph[n1] = [n2]
    if n2 in graph:
        graph[n2].append(n1)
    else:
        graph[n2] = [n1]
visited = []
paths = 0
DFS('start')
print(paths)
