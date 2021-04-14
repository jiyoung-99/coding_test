"""
문제
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오
예를 들어 1을 입력했을때 1시 59분 59초까지 3이 하나라도 포함되는 경우의 수를 구한다.
===========================
주의할 검 전체 데이터 수가 100만개 이하이면 완전탐색을 써도 된다.
"""


input_time = int(input())

count = 0
for i in range(input_time+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
