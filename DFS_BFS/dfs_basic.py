"""
DFS는 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

"""
# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, v, visited)

def dfs(graph, v, visited):
    visited[v] = True
    print(visited)
    for i in graph[v]:
        
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [1, 4],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 0, visited)




