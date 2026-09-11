# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()

for key, group in groupby(s):
    print((len(list(group)), int(key)), end=" ")