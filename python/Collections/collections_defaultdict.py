from collections import defaultdict
m,n=map(int,input().split())
dict=defaultdict(list)
for i in range(m):
    dict[input()].append(i+1)

keys=[input() for i in range(n)]
for key in keys:
    print(*dict[key]) if key in dict else print(-1)
