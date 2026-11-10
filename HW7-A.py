import sys

def parking_fee(minutes):
    """
    計算單車停車費用
    - 每開始一個 30 分鐘區間收費 30 元（不足 30 分鐘算一個區間）
    - 0 分鐘不收費
    - 單次最高 200 元
    """
    if minutes == 0:
        return 0
    # (minutes + 29) // 30 實現無條件進位求區間數
    blocks = (minutes + 29) // 30
    fee = blocks * 30
    return min(fee, 200)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    times = [int(x) for x in input_data[1:n+1]]
    
    # 對每筆紀錄呼叫 parking_fee
    fees = [parking_fee(t) for t in times]
    total_fee = sum(fees)
    
    print(*(fees))
    print(total_fee)

if __name__ == '__main__':
    main()