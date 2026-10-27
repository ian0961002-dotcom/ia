import sys

def main():
    # 必須完整讀取一行，可能為空或只有空白
    line = sys.stdin.readline()
    if not line:
        return
    # 去除末尾的換行符
    if line.endswith('\n'):
        line = line[:-1]
    elif line.endswith('\r\n'):
        line = line[:-2]
        
    # 1. 依序移除頭尾的半形空白
    stripped_line = line.strip(' ')
    
    # 2. 把英文字母轉成小寫
    lower_line = stripped_line.lower()
    
    # 3. 將中間每一段連續半形空白改成一個底線
    # 利用 split() 不帶參數時，會自動將連續的空白字元視為單一分隔符切開
    words = lower_line.split()
    # 再用 '_' 將它們黏起來
    formatted_username = '_'.join(words)
    
    # 4. 檢查合法性
    is_valid = True
    
    # 檢查長度是否為 6 至 16
    if not (6 <= len(formatted_username) <= 16):
        is_valid = False
        
    # 檢查每個字元是否只能是 a-z、0-9 或底線，且開頭可為數字或底線（即開頭不能是英文字母嗎？不，題目是說「開頭可為數字或底線」，一般代表開頭也可以是字母，意思是說沒有限制開頭不能為數字/底線，只要滿足每個字元是 a-z, 0-9, _ 即可。再細讀題目：「開頭可為數字或底線」這句話是提示，因為有些系統帳號開頭不能是數字，而此題允許。）
    # 重新檢視題目：「每個字元只能是 a 至 z、0 至 9 或底線；開頭可為數字或底線。」這代表全部字元的合法集合就是 (a-z, 0-9, _)，開頭沒有額外排除。
    if is_valid:
        for i, char in enumerate(formatted_username):
            if not ('a' <= char <= 'z' or '0' <= char <= '9' or char == '_'):
                is_valid = False
                break
                
    # 輸出結果：第一行為整理後的帳號（若為空字串則輸出一空白行）
    print(formatted_username)
    if is_valid:
        print("VALID")
    else:
        print("INVALID")

if __name__ == '__main__':
    main()
