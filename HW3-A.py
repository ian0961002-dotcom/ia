N = int(input().strip())

# 拆解百位、十位、個位
hundreds = N // 100
tens = (N // 10) % 10
units = N % 10

# 計算總和、乘積與反轉值
digit_sum = hundreds + tens + units
digit_product = hundreds * tens * units
reversed_num = int(str(N)[::-1])

print(f"{hundreds} {tens} {units}")
print(digit_sum)
print(digit_product)
print(reversed_num)