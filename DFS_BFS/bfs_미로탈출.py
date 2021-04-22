"""
NXM크기의 직사각형 형태의 미로에 갖혀 있다.
미로에는 여러 마리의 괴물이 있어서 이를 피해 탈출해야 한다.
사람의 위치는 1, 1이고 미로의 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다.
이 때 괴물이 있는 부분은 0으로
괴물이 없는 부분은 1로 표시된다.
미로는 반드시 탈출할 수 있는 형태로 제시된다.
이때 탈출하기 위해 최소로 움직여야 하는 칸의 갯수를 구하시오

"""

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐 규현을 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        print('queue : ', queue)
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))





