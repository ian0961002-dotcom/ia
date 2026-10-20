n = int(input())
if n == 0:
    print(0)
else:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    print(total)