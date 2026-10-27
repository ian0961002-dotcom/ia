import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines or len(lines) < 2:
        return
        
    G = int(lines[0].strip())
    steps = [int(x) for x in lines[1].split()]
    
    # 1. 總步數
    total_steps = sum(steps)
    
    # 2. 達標天數
    achieved_days = 0
    for s in steps:
        if s >= G:
            achieved_days += 1
            
    # 3. 最高步數出現的日期
    max_steps = max(steps)
    max_days = []
    for i in range(7):
        if steps[i] == max_steps:
            max_days.append(str(i + 1))
            
    # 4. 最長連續達標天數
    max_streak = 0
    current_streak = 0
    for s in steps:
        if s >= G:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0
            
    # 輸出結果
    print(total_steps)
    print(achieved_days)
    print(" ".join(max_days))
    print(max_streak)

if __name__ == '__main__':
    main()
