from itertools import combinations_with_replacement

s, n = input().split()

for i in combinations_with_replacement(sorted(s), n):
    print("".join(i))
