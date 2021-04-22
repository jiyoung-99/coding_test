"""
어떤 나라에는 1~N 까지의 도시와 M개의 단방향 도로가 존재합니다.
모든 도로의 거리는 1입니다.
이때 특정한 도시 X로부터 출발하여 도달할 수 있는 도시 중에서 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요
또한 출발도시 X에서 출발도시 X로 가는 최단거리는 항상 0이라고 가정합니다.
예를 들면 N = 4, K = 2, X = 1일 때
1번 도시에서 출발하여 도달할 수 있는 도시 중에 최단 거리가 2인 도시는 4번 도시 뿐입니다.


입력조건
첫째 줄에 도시의 갯수 N, 도로의 갯수 M, 거리 정보 K, 출발 도시의 번호 X가 주어집니다.
둘쨰 줄부터 M개의 줄에 걸쳐서 두개이 자연수 A, B 가 주어지며 각 자연수는 공백으로 구분합니다.
이는 A번도시에서 B도시로 이동하는 단방향 도로가 존재한다는 의미입니다.

출력조건 
X로부터 출발하여 도달할 수 있는 도시 중에서 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력합니다.
"""
from collections import deque

# 입력 
n, m, k, x = map(int, input().split())
# 리스트 선언
graph = [[] for _ in range(n+1)]
# 리스트 받아옴
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대해 최단거리 초기화
visited = [-1] * (n + 1)
visited[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    print('now : ', now)
    print('graph : ', graph)
    for next_node in graph[now]:
        if visited[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(i, n+1):
    if visited[i] == k:
        print(i)
        check = True
if check = False:
    print(-1)






