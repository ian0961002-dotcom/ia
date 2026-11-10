import sys

def is_prime(n):
    """
    試除法判斷質數，僅檢查至整數開根號範圍
    """
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    R = int(input_data[1])
    
    primes = []
    for num in range(L, R + 1):
        if is_prime(num):
            primes.append(num)
            
    if primes:
        print(*primes)
        print(f"{len(primes)} {sum(primes)}")
    else:
        print("NONE")
        print("0 0")

if __name__ == '__main__':
    main()