def cipher(target):
    result = ""

    for c in target:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result

# 対象文字列の入力
target = input('文字列を入力してください--> ')

# 暗号化
result = cipher(target)
print('暗号化:' + result)

# 復号化
result2 = cipher(result)
print('復号化:' + result2)

# 復号化で元に戻っているかチェック
if result2 != target:
    print('元に戻っていない！？')