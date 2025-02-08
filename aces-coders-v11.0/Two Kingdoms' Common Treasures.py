# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/two-kingdoms-common-treasures

from collections import Counter

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

count1 = Counter(list1)
count2 = Counter(list2)

common_items = []

for item in count1:
    if item in count2:
        common_items.extend([item] * min(count1[item], count2[item]))

if common_items:
    print(" ".join(map(str, sorted(common_items))))
else:
    print("NONE")