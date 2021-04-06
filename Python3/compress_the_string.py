from itertools import groupby

s = input()
t = [list(g) for k, g in groupby(s)]
for i in t:
    print(f"({len(i)}, {int(i[0])})", end=" ")
