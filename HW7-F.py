import sys

def best_total(prices, index, remaining):
    """
    純遞迴探索 0/1 背包狀態（不使用迴圈、DP、itertools 或 bitmask）
    """
    # 邊界情況：沒有商品可選，或剩餘預算為 0
    if index == len(prices) or remaining == 0:
        return 0
    
    # 分支 1：不選目前商品
    option1 = best_total(prices, index + 1, remaining)
    
    # 分支 2：若買得起，選擇目前商品
    option2 = 0
    if prices[index] <= remaining:
        option2 = prices[index] + best_total(prices, index + 1, remaining - prices[index])
        
    return max(option1, option2)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    budget = int(input_data[1])
    prices = [int(x) for x in input_data[2:2+n]]
    
    # 主程式直接呼叫 best_total(prices, 0, budget)
    result = best_total(prices, 0, budget)
    print(result)

if __name__ == '__main__':
    main()