n = int(input())
scores = list(map(int, input().split()))
total = 0
pass_count = 0
for score in scores:
    total += score
    if score >= 60:
        pass_count += 1
avg = total / n
print(f"{avg:.2f}")
print(pass_count)