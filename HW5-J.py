s, d, t = map(int, input().split())
days = 0
curr = s
while curr < t:
    curr += d
    days += 1
print(days)