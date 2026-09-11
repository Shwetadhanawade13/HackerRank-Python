# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
shoes = Counter(map(int, input().split()))

customers = int(input())

money = 0

for i in range(customers):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        money += price
        shoes[size] -= 1

print(money)