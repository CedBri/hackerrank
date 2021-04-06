
# Enter your code here. Read input from STDIN. Print output to STDOUTfrom collections import OrderedDict
from collections import OrderedDict

N = int(input())
item_dict = OrderedDict()

for _ in range(N):
    temp = input().split()
    item, item_price = " ".join(temp[:-1]), int(temp[-1])
    if item_dict.get(item):
        item_dict[item] += item_price
    else:
        item_dict[item] = item_price

for i in item_dict.keys():

    print(i, item_dict[i])    
