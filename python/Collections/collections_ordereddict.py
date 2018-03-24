
m collections import OrderedDict
dict = OrderedDict()
n = int(input())

l = [input().rpartition(' ') for i in range(n)]
for item, space, quant in l:
    dict[item] = dict[item] + int(quant) if item in dict else int(quant)
print("\n".join([" ".join([key, str(value)]) for key, value in dict.items()]))
