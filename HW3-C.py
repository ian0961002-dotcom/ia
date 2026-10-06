x1, x2, x3 = map(int, input().split())

# 計算平均數
mean = (x1 + x2 + x3) / 3.0

# 計算母體變異數
variance = ((x1 - mean) ** 2 + (x2 - mean) ** 2 + (x3 - mean) ** 2) / 3.0

print(f"{mean:.2f}")
print(f"{variance:.2f}")