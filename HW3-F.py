a, b = map(int, input().split())
c, d = map(int, input().split())

# 計算行列式 det
det = a * d - b * c

inv11 = d / det
inv12 = -b / det
inv21 = -c / det
inv22 = a / det

print(f"{inv11:.4f} {inv12:.4f}")
print(f"{inv21:.4f} {inv22:.4f}")