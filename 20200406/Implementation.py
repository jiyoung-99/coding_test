"""
NXN크기의 정사각형이 있다. 이 공간은 1X1크기의 정사각형으로 나누어져 있다. 맨 위 왼쪽 좌표는 1, 1 이고 오른쪽 맨 밑은 NXN이다. 
L : left
R : right
U : up
D : down
정사각형의 범위를 벗어나면 움직임은 무시된다. 
첫째줄에는 공간의 크기를 나타내는 N이 주어지고
둘째줄에는 이동할 방향의 내용이 주어진다.
최종 도착할 지점의 좌표를 공백으로 구분해서 출력하여라
"""
n = int(input())
x, y, nx, ny = 1, 1, 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']
for plan in plans:
    
    for index, value in enumerate(move_types):
        if plan == value:
            nx = x + dx[index]
            ny = y + dy[index]
            print('x : ', x)
            print('y : ', y)
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny


print(x, y)