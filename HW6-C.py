import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
        
    N = int(lines[0].strip())
    
    names = []
    subtotals = [] # 儲存整單折扣前的各商品優惠後小計
    
    for i in range(1, N + 1):
        name, price_str, qty_str = lines[i].split()
        price = int(price_str)
        qty = int(qty_str)
        
        # 買滿 3 件，其中 1 件免費 -> 每 3 件少算 1 件的錢
        # 免費件數 = qty // 3
        paid_qty = qty - (qty // 3)
        item_subtotal = paid_qty * price
        
        names.append(name)
        subtotals.append(item_subtotal)
        
    # 計算整張帳單折扣前的總金額
    raw_total = sum(subtotals)
    
    # 滿 1000 元折 100 元（整張帳單限折一次）
    if raw_total >= 1000:
        final_total = raw_total - 100
    else:
        final_total = raw_total
        
    # 尋找花費最多的商品（最高小計以整單折扣前的商品小計比較）
    # 同額選輸入較早者
    max_val = -1
    top_product = ""
    for i in range(N):
        # 因為是 > 而非 >=，所以自然會保留同額中輸入較早（索引較小）的商品
        if subtotals[i] > max_val:
            max_val = subtotals[i]
            top_product = names[i]
            
    # 輸出結果
    for i in range(N):
        print(f"{names[i]} {subtotals[i]}")
    print(f"TOTAL {final_total}")
    print(f"TOP {top_product}")

if __name__ == '__main__':
    main()
