from itertools import product
A=map(int,input().split())
B=map(int,input().split())
print(" ".join(map(str,list(product(A,B)))))
