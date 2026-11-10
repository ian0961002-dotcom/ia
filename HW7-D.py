import sys

def gcd(a, b):
    """
    遞迴輾轉相除法求最大公因數（基底為 b == 0）
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def simplify_recipe(tea, milk, syrup):
    """
    計算三數之最大公因數並回傳最簡比例
    """
    g = gcd(gcd(tea, milk), syrup)
    return tea // g, milk // g, syrup // g

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    idx = 1
    for _ in range(n):
        tea = int(input_data[idx])
        milk = int(input_data[idx + 1])
        syrup = int(input_data[idx + 2])
        idx += 3
        
        ans_tea, ans_milk, ans_syrup = simplify_recipe(tea, milk, syrup)
        print(f"{ans_tea} {ans_milk} {ans_syrup}")

if __name__ == '__main__':
    main()