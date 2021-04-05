from itertools import permutations

user_input = input().split()

#remove duplicates
user_input[0] = sorted(list(set(user_input[0])))
perm_list = list(permutations(user_input[0], int(user_input[1])))


print("\n".join("".join(i) for i in perm_list))
