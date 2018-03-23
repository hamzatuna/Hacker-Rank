from itertools import combinations
n=int(input())
l=input().split()
k=int(input())
chars= list(combinations(l,k))
print(len([1 for x in chars if 'a' in x])/len(chars))

