# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/the-quest-of-the-magic-array/
def longest_magic_sequence(arr):
    if not arr:
        return 0
    max_len = 1
    current_len = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1

    max_len = max(max_len, current_len)
    return max_len

N = int(input())
arr = list(map(int, input().split()))

print(longest_magic_sequence(arr))