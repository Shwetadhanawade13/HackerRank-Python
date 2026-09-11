# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split())

A = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    A[word].append(i)

for i in range(m):
    word = input()

    if word in A:
        print(*A[word])
    else:
        print(-1)