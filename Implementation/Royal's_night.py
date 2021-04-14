"""
왕실 정원은 체스판과 같은 8X8 좌표 평면이다.
왕실 정원의 한 칸에 나이트가 서 있다. 나이트는 이동을 할 때 L 자 형태로만 이동이 가능하며
정원 밖으로는 나갈 수 없다.
나이트는 2가지 경우로 이동 할 수 있다.
1. 수평으로 두칸 이동 후 수직으로 한칸 이동
2. 수직으로 두칸 이동 후 수평으로 한칸 이동
행 위치를 표현할 때 1~8로 표현하고
열 위치는 a~h로 표현한다.

여기서 위치를 입력 받고 이동 할 수 있는 경우의 수를 출력하여라

"""

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])-96)

steps =[
    (-2, -1), 
    (-2, 1), 
    (2, -1), 
    (2, 1),
    (1, -2), 
    (1, 2), 
    (-1, -2), 
    (-1, 2),
]

result = 0
for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        result += 1

print(result)