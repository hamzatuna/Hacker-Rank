from collections import namedtuple
n=int(input())
student=namedtuple('student',input())
print('{:05.2f}'.format(sum(map( lambda x: int(x.MARKS),[student(*input().split()) for i in range(n)]))/n))


