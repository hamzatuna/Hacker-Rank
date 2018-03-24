import sys


def isBalanced(s):
    l = []
    for c in s:
        if c in "{[(":
            l.append(c)
        elif len(l) == 0 and c in ")}]":
            return 'NO'
        elif (l[-1] + c) in ["{}", "[]", "()"]:
            l.pop()

    return 'YES' if len(l) == 0 else 'NO'


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
