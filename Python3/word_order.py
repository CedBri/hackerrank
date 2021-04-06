from collections import OrderedDict
N = int(input())
word_list = {}
for _ in range(N):
    temp = input()
    if temp in word_list:
        word_list[temp] += 1
    else:
        word_list[temp] = 1
print(" ".join(word_list[x] for x in word_list))
