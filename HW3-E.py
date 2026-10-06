a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g, h = map(int, input().split())

# 矩陣相乘 C = A * B
c11 = a * e + b * g
c12 = a * f + b * h
c21 = c * e + d * g
c22 = c * f + d * h

print(f"{c11} {c12}")
print(f"{c21} {c22}")