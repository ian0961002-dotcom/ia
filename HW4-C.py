a, b, c = map(int, input().split())
ans = a
if b > ans:
  ans = b
if c > ans:
  ans = c
print(ans)