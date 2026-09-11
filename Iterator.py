# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))

count = 0

for combination in all_combinations:
    if 'a' in combination:
        count += 1

print(count / len(all_combinations))