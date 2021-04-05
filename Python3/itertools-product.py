from itertools import product

first_set = list(map(int, input().split()))
second_set = list(map(int, input().split()))

complet_set = [first_set, second_set]

print(", ".join(list(product(*complet_set))))


