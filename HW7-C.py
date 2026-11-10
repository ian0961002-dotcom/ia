import sys

def normalize(text):
    """
    整理字串：僅保留 ASCII 英文字母與數字，並將字母轉換為小寫
    """
    cleaned = []
    for ch in text:
        if ch.isalnum():
            cleaned.append(ch.lower())
    return "".join(cleaned)

def is_palindrome(text, left, right):
    """
    純遞迴判斷字串是否為回文（不使用迴圈、切片、reversed）
    """
    if left >= right:
        return True
    if text[left] != text[right]:
        return False
    return is_palindrome(text, left + 1, right - 1)

def main():
    # 需整行讀取原始密語
    line = sys.stdin.readline()
    if line.endswith('\n'):
        line = line[:-1]
    if line.endswith('\r'):
        line = line[:-1]
        
    cleaned_text = normalize(line)
    
    # 整理後長度 0 或 1 均視為回文
    if len(cleaned_text) <= 1:
        print("YES")
    else:
        if is_palindrome(cleaned_text, 0, len(cleaned_text) - 1):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()