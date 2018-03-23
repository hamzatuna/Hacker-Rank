from itertools import combinations_with_replacement as cmbn
S,k=input().split()
print("\n".join(map("".join,list(cmbn(sorted(S),int(k))))))
