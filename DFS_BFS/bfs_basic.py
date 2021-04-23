from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    print('queue',queue)
    visited[start] = True
    while queue:
        v = queue.popleft()
        print('graph[v]', graph[v])
        for i in graph[v]:
            
            if not visited[i]:
                queue.append(i)
                print('queue 1 : ',queue)
                visited[i] = True        

graph = [
    [1, 2],
    [2, 3],
    [1, 4],
    [1, 2, 4],
    [3, 4]
]

visited = [False] * 5

bfs(graph, 0, visited)