# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

both = english.intersection(french)

print(len(both))