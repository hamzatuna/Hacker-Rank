m, n = map(int, input().split())
for tp in zip(*[map(float, input().split()) for i in range(n)]):
    print(sum(tp) / float(len(tp)))
