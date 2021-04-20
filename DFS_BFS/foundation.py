"""
스택 : 박스 쌓기, first come last out
"""
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(7)
stack.pop()

print('print stack', stack)
print('print stack -1 ', stack[::-1])


"""
큐 : 택시를 기다리는 사람들을 생각, first come first out
큐를 이용할 때는 deque 이용

"""
from collections import deque

queue = deque()

queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
queue.append(5)
queue.append(6)
queue.append(8)
queue.popleft()

print('queue', queue)
queue.reverse()
print('reverse queue', queue)

"""
재귀함수 : 자기 자신을 다시 호출하는 함수를 의미
"""
def recursive_function():
    print("print recursive")
    recursive_function()

recursive_function()    