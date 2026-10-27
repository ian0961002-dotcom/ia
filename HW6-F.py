import sys

def main():
    line = sys.stdin.readline()
    if not line:
        return
    parts = line.split()
    
    B = int(parts[0]) # 原餐費
    N = int(parts[1]) # 人數
    R = int(parts[2]) # 服務費百分比
    C = int(parts[3]) # 折價券金額
    
    # 服務費為原餐費乘以服務費百分比，不足 1 元的部分捨去 (整數除法)
    service_charge = (B * R) // 100
    
    # 應付總額 = 原餐費 + 服務費 - 折價券金額
    T = B + service_charge - C
    # 若小於 0，改為 0
    if T < 0:
        T = 0
        
    # 計算分攤：a 人各付 q 元，b 人各付 q+1 元
    # q 為 T 除以 N 的整數商，餘數就是必須多付 1 元的人數 (即 b)
    q = T // N
    b = T % N
    a = N - b
    
    # 輸出三行
    print(T)
    print(f"{q} {a}")
    print(f"{q+1} {b}")

if __name__ == '__main__':
    main()
