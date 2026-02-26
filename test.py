import sys

from itertools import permutations, combinations

print(type(range(5)))
print(permutations(range(5), 2))
print(type(permutations(range(5), 2)))
# for p in permutations(range(3), 2):
#     print(p)
#     print(type(p))
for p in permutations([1, 2, 3], 2):
    print(p)
    print(type(p))

# ===========================



# ===========================

result_1 = 'name'
result_2 = ['age', 'address']

print(list(result_1))  # ['n', 'a', 'm', 'e']
print([result_1])      # ['name']
print([result_2])      # [['age', 'address']]

for i in [result_1]:
    print(i)  # name

for j in [result_2]:
    print(j)  # ['age', 'address']

