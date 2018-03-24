limit = int(input())
s = []
max_s = 0
for _ in range(limit):
    n = input()
    if n[0] == '1':
        i = int(n.split()[-1])
        if i > max_s:
            max_s = i
        s.append(i)
    elif n[0] == '2':
        if max_s == s.pop():
            max_s = max(s) if s else 0
    else:
        print(max_s)
