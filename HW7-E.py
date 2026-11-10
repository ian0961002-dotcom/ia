import sys

def count_ways(step, n, blocked, memo):
    """
    純遞迴 + 記憶化（Memoization）計算到達第 n 階的走法數
    - 函式內完全不使用迴圈或推導式
    - step: 目前位置
    - n: 目標階數
    - blocked: 長度 n+1 的布林陣列，True 表示損壞階梯
    - memo: 長度 n+1 的整數陣列，記錄從 step 出發到 n 的走法數
    """
    # 邊界 1：超出目標階數，或踩到損壞階梯
    if step > n or blocked[step]:
        return 0
    
    # 邊界 2：成功到達終點第 n 階
    if step == n:
        return 1
    
    # 記憶化檢查：若已計算過則直接回傳
    if memo[step] != -1:
        return memo[step]
    
    # 純遞迴分支：嘗試走 1 階 與 走 2 階
    ways = count_ways(step + 1, n, blocked, memo) + count_ways(step + 2, n, blocked, memo)
    
    # 存入 memo 並回傳結果
    memo[step] = ways
    return ways

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # 初始化 blocked 與 memo 陣列 (長度皆為 n + 1)
    blocked = [False] * (n + 1)
    memo = [-1] * (n + 1)
    
    # 標記損壞階梯
    if k > 0:
        for i in range(k):
            b_idx = int(input_data[2 + i])
            if b_idx <= n:
                blocked[b_idx] = True
                
    # 主程式呼叫 count_ways(0, n, blocked, memo)
    result = count_ways(0, n, blocked, memo)
    print(result)

if __name__ == '__main__':
    main()