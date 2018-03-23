
from collections import deque
d=deque()
for _ in range(int(input())):
    slist=input().split()
    getattr(d,slist[0])(*slist[1] if len(slist)>1 else [] )
print(*d)
