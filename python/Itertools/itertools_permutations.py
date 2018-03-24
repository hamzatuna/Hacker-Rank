from itertools import permutations
S, n = input().split()
print("\n".join(map("".join, list(permutations(sorted(S), int(n))))))
