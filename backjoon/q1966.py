from collections import deque

input_nums = int(input())

for _ in range(input_nums):
    n, m = map(int, input().split())
    q_list = list(map(int, input().split()))
    check_list = [0 for _ in range(n)]
    check_list[m] = 1

    count = 0

    while True:
        # print('q_list',q_list)
        if q_list[0] == max(q_list):
            count += 1
            if check_list[0] == 1:
                print(count)
                break
            else:
                q_list.pop(0)
                check_list.pop(0)
        else:
            q_pop = q_list.pop(0)
            c_pop = check_list.pop(0)
            # print(q_pop, c_pop)
            q_list.append(q_pop)
            check_list.append(c_pop)



