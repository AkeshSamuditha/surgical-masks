str = input()
n = len(str)
res = ""
max_len = 0
start = 0
char_index = {}

for end in range(n):
    if str[end] in char_index and char_index[str[end]] >= start:
        start = char_index[str[end]] + 1

    char_index[str[end]] = end

    if end - start + 1 > max_len:
        max_len = end - start + 1
        res = str[start:end+1]

print(res)