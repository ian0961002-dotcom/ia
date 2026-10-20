m = int(input())
coins = 0
curr = m
while curr > 0:
    if curr >= 50:
        curr -= 50
    elif curr >= 10:
        curr -= 10
    elif curr >= 5:
        curr -= 5
    else:
        curr -= 1
    coins += 1
print(coins)