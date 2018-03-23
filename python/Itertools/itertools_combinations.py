from itertools import combinations
S,k=input().split()
for i in range(int(k)):
    print("\n".join(map("".join,list(combinations(sorted(S),i+1)))))
