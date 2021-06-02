"""
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
"""

def fib(n, list_):
    # print(n, list_ )
    if n == 0:
        list_[0] += 1
        
    elif n == 1:
        list_[1] += 1
        
    else:
        return fib(n-1, list_) + fib(n-2, list_)

    return list_
amount = int(input())
num_list = []

for one in range(amount):
    num = int(input())
    num_list.append(num)


for num in num_list:
    result = fib(num, [0, 0])
    print(result[-2:])
    
    
    


