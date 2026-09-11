# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = map(int, input().split())

lists = []
for i in range(k):
    data = list(map(int, input().split()))
    lists.append(data[1:])

maximum = 0

for combination in product(*lists):
    value = sum(x * x for x in combination) % m

    if value > maximum:
        maximum = value

print(maximum)