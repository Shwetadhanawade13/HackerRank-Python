import re

s = input()

pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

result = re.findall(pattern, s)

if result:
    for x in result:
        print(x)
else:
    print(-1)

