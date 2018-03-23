
m collections import OrderedDict
dict=OrderedDict()
for _ in range(int(input())):
    s=input()
    dict[s]=dict.get(s,0)+1
print(len(dict))
print(*[value for _,value in dict.items()])
