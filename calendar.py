# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

month, day, year = map(int, input().split())

day_name = calendar.day_name[calendar.weekday(year, month, day)]

print(day_name.upper())