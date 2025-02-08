# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/min-concats

num_words = int(input())
words = [input().strip() for _ in range(num_words)]
target_string = input().strip()

valid_prefixes = set()
for word in words:
    for length in range(1, len(word) + 1):
        valid_prefixes.add(word[:length])

target_length = len(target_string)
min_prefix_count = [float('inf')] * (target_length + 1)
min_prefix_count[0] = 0

for end in range(1, target_length + 1):
    for start in range(end):
        substring = target_string[start:end]
        if substring in valid_prefixes:
            min_prefix_count[end] = min(min_prefix_count[end], min_prefix_count[start] + 1)

result = min_prefix_count[target_length] if min_prefix_count[target_length] != float('inf') else -1
print(result)