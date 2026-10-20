n = int(input())
if n == 0:
    print(0)
else:
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    print(rev)