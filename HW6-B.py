import sys

def main():
    line = sys.stdin.readline()
    if not line:
        return
    if line.endswith('\n'):
        line = line[:-1]
    elif line.endswith('\r\n'):
        line = line[:-2]
        
    # 1. 依序移除頭尾的半形空白
    stripped_line = line.strip(' ')
    
    # 2. 把英文字母轉成小寫
    lower_line = stripped_line.lower()
    
    # 3. 將中間每一段連續半形空白改成一個底線
    words = lower_line.split()
    formatted_username = '_'.join(words)
    
    # 4. 檢查合法性
    is_valid = True
    
    # 檢查長度是否為 6 至 16
    if not (6 <= len(formatted_username) <= 16):
        is_valid = False
        
    # 檢查每個字元是否合法
    if is_valid:
        for char in formatted_username:
            if not ('a' <= char <= 'z' or '0' <= char <= '9' or char == '_'):
                is_valid = False
                break
                
    # 輸出結果
    print(formatted_username)
    if is_valid:
        print("VALID")
    else:
        print("INVALID")

if __name__ == '__main__':
    main()
