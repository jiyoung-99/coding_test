
"""
음료수 얼려 먹기
NXM크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 있는 부분은 1로 표시괸다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어있는 것으로 간주한다.
이 때 얼음 틀의 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오
"""
# 얼음틀의 크기 입력
n, m = map(int, input().split())

# 얼음틀 정의
graph = []

# 얼음틀의 모양 입력
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        print('x : ', x,'y : ',  y, 'graph[x][y]', graph[x][y])
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대해서 음료수 채우기
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)

# 모든 노드에 대해서 음료수 채우기 
