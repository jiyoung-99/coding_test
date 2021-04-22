from itertools import combinations
from itertools import permutations
from itertools import product

list1 = [1, 2, 3, 4, 5]
list2 = ['a1b', 'c2d', 'f3g']

print('!!!!',*list2)

# combination을 쓰면 갯수 별로 조합을 반복 할 수 있다.
is_combination = list(combinations(list1, 2))

# 각각의 숫자를 중복을 허용하지 않고 모든 경우의 수를 구하는 것
print('is_combination : ', is_combination)

# 각각의 숫자를 중복을 허용하지 않고 모든 경우의 수를 구하는 것, 1부터 is_combination의 길이까지
for i in range(len(is_combination)):
    print(list(combinations(is_combination, i+1)))


# permutations 을 쓰면 중복을 허용하고 모든 경우의 수를 구한다.
is_permutation = list(permutations(list1))
print('is_permutation',is_permutation)

# product 두개 이상의 리스트의 모든 조합을 구할 때 사용된다. repeat2를 하면 2개를 묶을 때 사용
is_product = list(product(list2, repeat=2))
print('is_product', is_product)

# 앞에 *을 쓰면 하나의 글자씩 조합한다.
is_product_star = list(product(*list2))
print('is_product_star', is_product_star)