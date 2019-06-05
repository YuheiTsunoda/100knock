num_first_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
target = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

result = {}
words = target.split(" ")

for (num, word) in enumerate(words, 1):
    if num in num_first_only:
        result[word[0:1]] = num
    else:
        result[num] = word[0:2]

print(result)