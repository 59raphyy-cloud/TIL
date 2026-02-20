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