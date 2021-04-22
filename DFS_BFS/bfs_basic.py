from collections import deque




def bfs(graph, start, visited):
    queue = deque([start])
    print('queue',queue)
    visited[start] = True
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            print('i : ', i)
            if not visited[i]:
                queue.append(i)
                visited[i] = True        

graph = [
    [],
    [2, 3],
    [1, 4],
    [1, 2, 4],
    [3, 4]
]

visited = [False] * 5

bfs(graph, 1, visited)