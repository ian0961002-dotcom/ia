import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
        
    # 1. 讀取菜單
    M = int(lines[0].strip())
    menu_drinks = []
    menu_prices = []
    for i in range(1, M + 1):
        drink, price = lines[i].split()
        menu_drinks.append(drink)
        menu_prices.append(int(price))
        
    # 2. 讀取訂單
    N = int(lines[M + 1].strip())
    
    # 用於紀錄每種飲料的總杯數 (與菜單順序一致)
    drink_counts = [0] * M
    
    # 用於紀錄學生的首次出現順序與獨立累計金額
    student_names = []
    student_totals = []
    
    # 先跑第一次訂單：統計每種飲料的總杯數，並記錄學生出現順序
    start_order_idx = M + 2
    orders = []
    for i in range(start_order_idx, start_order_idx + N):
        student, drink, qty = lines[i].split()
        qty = int(qty)
        orders.append((student, drink, qty))
        
        # 統計飲料總杯數
        d_idx = menu_drinks.index(drink)
        drink_counts[d_idx] += qty
        
        # 記錄學生（若未出現過則加入平行串列）
        if student not in student_names:
            student_names.append(student)
            student_totals.append(0)
            
    # 3. 計算每種飲料的優惠後單價
    final_prices = []
    for i in range(M):
        if drink_counts[i] >= 10:
            final_prices.append(menu_prices[i] - 5)
        else:
            final_prices.append(menu_prices[i])
            
    # 4. 計算每個學生的應付總額
    for student, drink, qty in orders:
        d_idx = menu_drinks.index(drink)
        cost = final_prices[d_idx] * qty
        s_idx = student_names.index(student)
        student_totals[s_idx] += cost
        
    # 5. 依要求輸出結果
    # 輸出 DRINK
    for i in range(M):
        print(f"DRINK {menu_drinks[i]} {drink_counts[i]}")
        
    # 輸出 STUDENT
    for i in range(len(student_names)):
        print(f"STUDENT {student_names[i]} {student_totals[i]}")
        
    # 輸出 TOTAL 全班總額
    total_all = sum(student_totals)
    print(f"TOTAL {total_all}")

if __name__ == '__main__':
    main()
