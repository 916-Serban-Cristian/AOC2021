def DFS(node):
    global visited, paths
    if node.islower():
        visited[node] += 1
    for neighbour in graph[node]:
        if neighbour.islower():
            if neighbour == 'end':
                paths += 1
                continue
            elif neighbour == 'start':
                continue
            if 2 not in visited.values():
                DFS(neighbour)
                visited[neighbour] -= 1
            else:
                if visited[neighbour] == 0:
                    DFS(neighbour)
                    visited[neighbour] -= 1
        else:
            DFS(neighbour)


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
visited = {node: 0 for node in graph}
paths = 0
DFS('start')
print(paths)
