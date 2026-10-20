a, b, k = map(int, input().split())
count = 0
total = 0
for i in range(a, b + 1):
    if i % k == 0:
        count += 1
        total += i
print(f"{count} {total}")