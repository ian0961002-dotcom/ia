import sys

def main():
    # 讀取第一行：位移量 K
    line1 = sys.stdin.readline()
    if not line1:
        return
    K = int(line1.strip())
    
    # 讀取第二行：原始訊息 S (保留所有連續與頭尾空白)
    S = sys.stdin.readline()
    # 去除結尾的換行符號，但保留其餘空白
    if S.endswith('\n'):
        S = S[:-1]
    elif S.endswith('\r\n'):
        S = S[:-2]
        
    result = []
    for char in S:
        if 'A' <= char <= 'Z':
            # 大寫字母加密
            new_char = chr((ord(char) - ord('A') + K) % 26 + ord('A'))
            result.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母加密
            new_char = chr((ord(char) - ord('a') + K) % 26 + ord('a'))
            result.append(new_char)
        else:
            # 數字、空白與標點符號保持原樣
            result.append(char)
            
    # 輸出加密後的完整訊息，最後加上換行
    print("".join(result))

if __name__ == '__main__':
    main()
